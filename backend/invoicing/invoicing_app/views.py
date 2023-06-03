from django.shortcuts import render
from django.views import View
from .serializers import *
from django.http import JsonResponse
from .data import *
import json
import uuid

# Create your views here.

# ****************INVOICE API***********************

#Get the list of invoices
class InvoiceListView(View):
    def get(self, req):
        serialized_invoices = InvoiceSerializer(invoices, many=True).data
        return JsonResponse(serialized_invoices, safe=False, status=200)
 
 
# Get invoice by Id   
class InvoiceView(View):
    def get(self, req, id):
        for each in invoices:
            if each['invoice_id'] == id:
                serialized_invoice = InvoiceSerializer(each).data
                return JsonResponse(serialized_invoice, safe=False)
        else:
            return JsonResponse({'message': 'Invoice not found'})
        

# Create new invoice
class NewInvoiceView(View):
    def post(self, req):
        invoice_data = json.loads(req.body)
        invoice_data['invoice_id'] = len(invoices) + 1
        invoice_data['items'] = []
        
        serialized_invoice = InvoiceSerializer(data = invoice_data)
        
        if serialized_invoice.is_valid():
            invoices.append(serialized_invoice.data)
            return JsonResponse(serialized_invoice.data, safe=False, status = 201)
        else:
            return JsonResponse({'message':'Something went wrong!'}, status=500)


# *******************INVOICE ITEMS API*************************   

# Adds new items to invoice
class NewItemView(View):
    def post(self, req, invoiceId):
        itemData = json.loads(req.body)
        
        serialized_item = ItemSerializer(data = itemData)
        
        if serialized_item.is_valid():           
            for each in invoices:
                if each["invoice_id"] == invoiceId:
                    each["items"].append(serialized_item.data)
            return JsonResponse({"message":"New Item added"}, status=201)
        else:
            return JsonResponse({"message":"Something went wrong! Cannot add the item."}, status=400)


class SignUpView(View):
    def post(self, req):
        userData = json.loads(req.body)
        for user in users:
            if user["email"] == userData["email"]:
                return JsonResponse({"message":"Account already exist", "state":False})
        userData["user_id"] = len(users) + 1
        serialized_user = UserSerializer(data = userData)
        
        if serialized_user.is_valid():
            users.append(serialized_user.data)
            return JsonResponse({"message":"Sign up successful!","state":True}, status=201)
        else:
            return JsonResponse({"message":"Something went wrong!","state":False})
        
class LoginView(View):
    def post(self, req):
        user_data = json.loads(req.body)
        for index, item in enumerate(users):
            if (item["email"] == user_data["email"] and item["password"] == user_data["password"]):
                token = uuid.uuid4()
                return JsonResponse(
                    {
                        "message":"Sign in successful",
                        "token":token,
                        "state":True
                    }, 
                    status = 200
                )
        
        return JsonResponse(
             {
                "message":"Invalid email or password",
                "state":False
            }, 
            
        )
        
            
        
        
        
                
            
