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

#Receipt Maker Def
def Receipt_Maker():

    #Supplier Database
    g = open("worksmarter/Databases/Supplier_Database.json")
    sdb = json.load(g)

    #Product List
    n = open('worksmarter/Databases/Product_List.json')
    pdb = json.load(n)

    #Receipt Content
    m = open('worksmarter/Databases/Purchase_Receipt_Content.json')
    prdb = json.load(m)

    p = open('worksmarter/Databases/Sales_Receipt_Content.json')
    srdb = json.load(p)

    #General Functions
    Total = 0
    today = date.today()
    today = today.strftime("%m-%d-%y")

    #Purchase Receipt
        #Header
    f = open(f"worksmarter/Receipts Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","w")
    f.write("---------------------------------------------\n") #40 Spaces
    f.write(f"Supplier :     {prdb['Supplier']}\n")
    f.write(f"Email    :     {sdb[prdb['Supplier']]['Email']}\n")
    f.write(f"Date     :     {today}\n")
    f.write("---------------------------------------------")
    f.write("\n")
    f.close

        #Body
    with open(f"worksmarter/Receipts Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","a") as f:
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
    f = open(f"worksmarter/Receipts Folder/Purchase Receipts/{today}_{prdb['Supplier']}_Purchase_Receipt.txt","a")
    f.write("---------------------------------------------\n")
    Last_Line = "Total    :"
    while len(Last_Line)< (45-len(str(Total))):
        Last_Line += " "
    f.write(f"{Last_Line}{Total}")

    Total=0
        #Header
    g = open(f"worksmarter/Receipts Folder/Sales Receipts/{today}_Sales_Receipt.txt","w")
    g.write("---------------------------------------------\n") #40 Spaces
    g.write(f"Date     :     {today}\n")
    g.write("---------------------------------------------")
    g.write("\n")
    g.close

        #Body
        with open(f"worksmarter/Receipts Folder/Sales Receipts/{today}_Sales_Receipt.txt","a") as g:
            for i in srdb['Order'].keys():
                Product = i
                Qty = str(srdb["Order"][i])
                Subtotal = str(int(Qty) * pdb[i])
                Total += int(Subtotal)
                while len(Product) < (31-len(Qty)):
                    Product += " "
                if len(Qty) == 1:
                    Qty = "0" + Qty
                while len(str(Qty)) < (10-len(Subtotal)):
                    Qty += " "
                g.write(f"{Product}\t{Qty}\t{Subtotal}\n")

        #Footer
        g = open(f"worksmarter/Receipts Folder/Sales Receipts/{today}_Sales_Receipt.txt","a")
        g.write("---------------------------------------------\n")
        Last_Line = "Total    :"
        while len(Last_Line)< (45-len(str(Total))):
            Last_Line += " "
        g.write(f"{Last_Line}{Total}")

Receipt_Maker()
