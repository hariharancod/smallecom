from ecom_app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from rest_framework import status
import jwt,json
from datetime import datetime, timedelta
from django.conf import settings
from .utils import decode_jwt

class Index(APIView):
   def post(self,request):
      print("reach success")
      userid=request.POST.get('userid')
      cart_items = Addshopping.objects.filter(user_id=userid).values()
      data = Product.objects.all().values('id','name', 'price', 'image')
      products=data 
      product_dict = {product["id"]: product for product in products}
      # Update products to set "add_cart" status based on cart_items
      for item in cart_items:
       product_id = item["product_id"]
       if product_id in product_dict:
        product_dict[product_id]["add_cart"] = True
        # Convert dictionary back to list if needed
      products = list(product_dict.values())
      return Response(products)
   
class Index_react(APIView):
    def get(self,request):
        return Response()

class Accounts(APIView):
    def post(self,request,format=None):
        print("reach account class")
        if request.method=='POST':
          username=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user is None:
            new_user=User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            return JsonResponse({'messages':'Registered successfully'})
          else:
           return JsonResponse({'messages':"Already registered"})
    

class Login_auth(APIView):
    def post(self,request):
     if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1),  # Token expiration time
            'iat': datetime.utcnow()  # Token issued at time
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return JsonResponse({'token':token,'user_id':user.id})
        else:
            return Response("something wrong")
     return Response("error")
     
      
class Logout_auth(APIView):
    def logout_view(request):
     if request.user.is_authenticated:
      logout(request)
     return redirect('home')         
    

class Products(APIView):
    parser_classes=[MultiPartParser,FormParser]
    def post(self,request,format=None):
        if(request.data):
         serial=ProductSerializer(data=request.data)
         if serial.is_valid():
          serial.save()
          return Response('saving successfully')
        else:
           data=Product.objects.all().values('id','name', 'price', 'image')
           return Response(data)
        return Response('error')


class Addcarts(APIView):
      def post(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
          try:
            token = auth_header.split(' ')[1]
            decoded = decode_jwt(token)
            if decoded:
                user_id = decoded.get('user_id')
                product_id=request.data.get('product_id',[])
                serial=AddshoppingSerializer(data={'product_id':product_id,'user_id':user_id})
                if Addshopping.objects.filter(user_id=user_id, product_id=product_id).exists():
                   return Response("This user-product combination already exists.")
                elif serial.is_valid():
                   serial.save()
                   return JsonResponse({'user_id': user_id})
            else:
                return JsonResponse({'error': 'Invalid or expired token'}, status=401)
          except IndexError:
            return JsonResponse({'error': 'Invalid token header format'}, status=401)


class Deletes(APIView):
   def post(self,request):
      data=json.loads(request.body)
      product_id=data.get('product_id')
      item=get_object_or_404(Product,id=product_id)
      if request.method=='POST':
         item.delete()
         return Response("successfully deletes")
      else:
         return Response("no delete")
      

class Updates(APIView):
   parser_classes = (MultiPartParser, FormParser)
   def post(self,request,format=None):
      if request.method == 'POST':
        try:
         record = get_object_or_404(Product, pk=request.data.get('id'))
        except Product.DoesNotExist:
         return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        form = ProductSerializer(instance=record,data=request.data,partial=True)
        if form.is_valid():
            for field, value in form.validated_data.items():
                if value is not None and value != '':
                    setattr(record, field, value)
            record.save()
            return JsonResponse({'status': 'success', 'message': 'Record updated'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
      return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


class My_cart(APIView):
   def post(self,request):
         user_id=request.data.get("userid")
         user = get_object_or_404(User, id=user_id)
         if(user):
          cart_items = Addshopping.objects.filter(user_id=user_id)   
          sets=set()
          for val in cart_items:
            sets.add(val.product_id)
         filtered_products = Product.objects.filter(id__in=sets)
         product_list = list(filtered_products.values('id', 'name','image', 'price'))
         return JsonResponse(product_list, safe=False)

         
class Add_deletes(APIView):
   def post(self,request):
      print("sucess reach")
      product_id=request.data.get("product_id")
      user_id=request.data.get("user_id")
      try:
       item = Addshopping.objects.get(user_id=user_id, product_id=product_id)
      except Addshopping.MultipleObjectsReturned:
         return Response("No data available")
      if request.method=='POST':
         try:
            item.delete()
            return JsonResponse({'success': 'Item deleted successfully.'}, status=200)
         except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
      else:
         return Response("no delete")

      
        
