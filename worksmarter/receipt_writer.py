#Guide to Receipt Content:
# Receipt Content - a temp dict to hold the content of the receipts
# Purchase Receipt Content Format:
#{
#    "kind":"Purchase",
#    "Supplier":"{NAME_OF_SUPPLIER}",
#    "Order":{
#        "{PRODUCT_NAME}":{PRODUCT_QTY}
#    }
#}
#Sales Receipt Content Format:
#{
#    "kind":"Sales",
#    "Order":{
#        "{PRODUCT_NAME}":{PRODUCT_QTY}
#    }
#}

import json
from datetime import date

 #Supplier Database
g = open("Databases/Supplier_Database.json")
sdb = json.load(g)

#Product List
n = open('Databases/Product_List.json')
pdb = json.load(n)

 #Supplier Database
g = open("Databases/Supplier_Database.json")
sdb = json.load(g)

#Product List
n = open('Databases/Product_List.json')
pdb = json.load(n)

#Sales Log
z = open("Databases/Sales_Log.json")
sl = json.load(z)

#Receipt Maker Def
def Receipt_Maker(kind,day):

    #Purchase Receipt Content
    m = open('Databases/Purchase_Receipt_Content.json')
    prdb = json.load(m)
    #Sales Receipt Content
    p = open('Databases/Sales_Receipt_Content.json')
    srdb = json.load(p)

    #General Functions
    Total = 0
    today = date.today()
    today = today.strftime("%m-%d-%y")
    if kind == "Purchase":
    #Purchase Receipt
        #Header
        f = open(f"Receipts_Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","w")
        f.write("---------------------------------------------\n") #40 Spaces
        f.write(f"Supplier :     {prdb['Supplier']}\n")
        f.write(f"Email    :     {sdb[prdb['Supplier']]['Email']}\n")
        f.write(f"Date     :     {today}\n")
        f.write("---------------------------------------------")
        f.write("\n")
        f.close

        #Body
        with open(f"Receipts_Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","a") as f:
            for i in prdb['Order'].keys():
                Product = i
                Qty = str(prdb["Order"][i])
                Subtotal = str(int(Qty) * sdb[prdb['Supplier']]['Products_CostsPHP'][Product])
                Total += int(Subtotal)
                while len(Product) < (31-len(Qty)):
                    Product += " "
                if len(Qty) == 1:
                    Qty = "0" + Qty
                while len(str(Qty)) < (10-len(Subtotal)):
                    Qty += " "
                f.write(f"{Product}\t{Qty}\t{Subtotal}\n")

        #Footer
        f = open(f"Receipts_Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","a")
        f.write("---------------------------------------------\n")
        Last_Line = "Total    :"
        while len(Last_Line)< (45-len(str(Total))):
            Last_Line += " "
        f.write(f"{Last_Line}{Total}")
        f.close()
    elif kind == "Sales":
#Sales Receipt
        Total=0
        today = day
        today = today.replace("/","-")
        #Header
        g = open(f"Receipts_Folder/Sales Receipts/{today}_Sales_Receipt.txt","w")
        g.write("---------------------------------------------\n") #40 Spaces
        g.write(f"Date     :     {today}\n")
        g.write("---------------------------------------------")
        g.write("\n")
        g.close

        #Body
        with open(f"Receipts_Folder/Sales Receipts/{today}_Sales_Receipt.txt","a") as g:
            for i in srdb[today].keys():
                Product = str(i)
                Qty = str(srdb[today][i]["Quantity"])
                Subtotal = str(srdb[today][i]["Subtotal"])
                Total += int(Subtotal)
                while len(Product) < (31-len(Qty)):
                    Product += " "
                if len(Qty) == 1:
                    Qty = "0" + Qty
                while len(str(Qty)) < (10-len(Subtotal)):
                    Qty += " "
                g.write(f"{Product}\t{Qty}\t{Subtotal}\n")

        #Footer
        g = open(f"Receipts_Folder/Sales Receipts/{today}_Sales_Receipt.txt","a")
        g.write("---------------------------------------------\n")
        Last_Line = "Total    :"
        while len(Last_Line)< (45-len(str(Total))):
            Last_Line += " "
        g.write(f"{Last_Line}{Total}")
        g.close()

def sales_content_writer(date):
    Date = date.replace("/","-")
    srdb = {}
    srdb[Date] = sl[date]
    with open('Databases/Sales_Receipt_Content.json','w') as b:
        json.dump(srdb,b,indent=4)

