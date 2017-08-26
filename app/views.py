import json
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from models import Product

class ProductDataApi(APIView):

	def post(self, request):

		title = request.data.get('title', None)
		sku = request.data.get('sku', None)
		product_type = request.data.get('product_type', None)
		brand = request.data.get('brand', None)
		category = request.data.get('category', None)
		sub_category = request.data.get('sub_category', None)
		price = request.data.get('price', None)
		discount = request.data.get('discount', None)
		source = request.data.get('source', None)
		mrp = request.data.get('mrp', None)

		if title and sku and product_type and category and price and source and brand and mrp:
			try:
				Product.objects.create(title=title, sku=sku, product_type=product_type,
											category=category, sub_category=sub_category, 
											price=price, discount=discount, source=source,
											brand=brand, mrp=mrp
										)
				return Response({}, status=status.HTTP_201_CREATED)
			except Exception as e:
				print e
				return Response({}, status=status.HTTP_400_BAD_REQUEST)
			
		else:
			return Response({}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, category=None, brand=None, sub_category=None, source=None, title=None, sku=None):

		try:
			title = request.data.get('title', None)
			sku = request.data.get('sku', None)
			brand = request.data.get('brand', None)
			category = request.data.get('category', None)
			sub_category = request.data.get('sub_category', None)
			source = request.data.get('source', None)

			if category or sub_category or brand or source:
				product = Product.objects.filter(Q(category=category) | Q(sub_category=sub_category) |
													Q(source=source) | Q(brand=brand)
												)
			if title or sku:
				product = Product.objects.filter(Q(title__icontains=title) | Q(sku__icontains=sku))

			if not category and not sub_category and not source and not title and not sku and not brand and not source:
				product = Product.objects.all()
			product = list(product.values('title','sku','brand','category','sub_category','source','price','discount'))
			return Response (json.dumps(product), status=status.HTTP_200_OK)
		except:
			return Response({}, status=status.HTTP_400_BAD_REQUEST)

	def put(request):
		try:
			products = Product.objects.filter()
			for product in products:
				product.discount = ((product.mrp - product.price)/product.mrp) * 100
				product.save()
			return Response({}, status=status.HTTP_200_OK)
		except:
			return Response({}, status=status.HTTP_400_BAD_REQUEST)

class DiscountBucketApi(APIView):
	
	def get(self, request):
		discount_range_0  = Product.objects.filter(discount=(0)).count()
		discount_range_10  = Product.objects.filter(discount__range=(0,10)).count()
		discount_range_30  = Product.objects.filter(discount__range=(10,30)).count()
		discount_range_50  = Product.objects.filter(discount__range=(30,50)).count()
		discount_range_gt_50  = Product.objects.filter(discount__gt=(50)).count()

		data = {
			'discount_range_0': discount_range_0,
			'discount_range_10': discount_range_10,
			'discount_range_30': discount_range_30,
			'discount_range_50': discount_range_50,
			'discount_range_gt_50': discount_range_gt_50
		}

		return Response(json.dumps(data), status=status.HTTP_200_OK)

		



