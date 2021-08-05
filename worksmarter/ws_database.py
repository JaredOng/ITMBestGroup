import json
#Admin Database
f = open("Admin_List.json")
admin = json.load(f)

def get_user(username):
    try:
       return admin[username]
    except KeyError:
       return None

#Sales Log Database
g = open("Sales_Log.json")
sales_log = json.load(g)

def get_sales_log():
    sales_log_list = []

    sales_log_dict={}
    for i,v in sales_log.items():
        for k in v:
            sales_log_dict[i]={"date":i,"product":k,"quantity":v[k]["Quantity"],"price":v[k]["Price"]}
            log = sales_log_dict[i]
            sales_log_list.append(log)

    return sales_log_list

#Purchase Log Database
h = open("Purchase_Log.json")
purchase_log = json.load(h)

def get_purchase_log():
    purchase_log_list = []

    purchase_log_dict={}
    for i,v in purchase_log.items():
        for k in v:
            purchase_log_dict[i]={"date":i,"product":k,"quantity":v[k]["Quantity"],"price":v[k]["Price"]}
            log = purchase_log_dict[i]
            purchase_log_list.append(log)

    return purchase_log_list

#Supplier Database
m = open("Supplier_Database.json")
supplier_info = json.load(m)

def get_supplier_pricing():
    supplier_pricing_list = []

    supplier_pricing_dict={}
    for i,v in supplier_info.items():
        for j,k in v["Products_CostsPHP"].items():
            supplier_pricing_dict={"product":j,"price":k}
            product = supplier_pricing_dict
            supplier_pricing_list.append(product)


    return supplier_pricing_list

#Product Database
n = open("Product_List.json")
product_list = json.load(n)
def get_price(product_name):
    price = product_list[product_name]
    return price

def get_store_pricing():
    store_pricing_list = []
    store_pricing_dict={}
    for i,j in product_list.items():
        store_pricing_dict={"product":i,"price":j}
        product = store_pricing_dict
        store_pricing_list.append(product)
    return store_pricing_list

def input_sales(date,product_name,qty,price):
    if date not in sales_log:
        sales_log[date]={product_name:{"Quantity": qty,"Price": price}}
    else:
        if product_name not in sales_log[date]:
            sales_log[date][product_name]={"Quantity": qty,"Price": price}
        elif product_name in sales_log[date]:
            qty = qty + sales_log[date][product_name]["Quantity"]
            sales_log[date][product_name]={"Quantity": qty,"Price": price}
    with open("Sales_Log.json","w") as log:
        log.write(sales_log)

def price_change(product,value):
    product_list[product] = value

    with open('Product_List.json',"w")as d:
        json.dump(product_list,d,indent=4)