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
    g = open("Supplier_Database.json")
    sdb = json.load(g)

    #Product List 
    n = open('Product_List.json')
    pdb = json.load(n)

    #Receipt Content 
    m = open('Receipt_Content.json')
    rdb = json.load(m)

    #General Functions
    Total = 0
    today = date.today()
    today = today.strftime("%m/%d/%y")
    #Purchase Receipt
    if rdb['kind'] == "Purchase":
        #Header
        f = open(f"Receipts Folder/{today} {rdb['Supplier']} Purchase_Receipt.txt","w")
        f.write("---------------------------------------------\n") #40 Spaces
        f.write(f"Supplier :     {rdb['Supplier']}\n")
        f.write(f"Email    :     {sdb[rdb['Supplier']]['Email']}\n")
        f.write(f"Date     :     {today}\n")
        f.write("---------------------------------------------")
        f.write("\n")
        f.close
        
        #Body
        with open("Receipts Folder/Purchase_Receipt.txt","a") as f:
            for i in rdb['Order'].keys():
                Product = i
                Qty = str(rdb["Order"][i])
                Subtotal = str(int(Qty) * sdb[rdb['Supplier']]['Products_CostsPHP'][Product])
                Total += int(Subtotal)
                while len(Product) < (31-len(Qty)):
                    Product += " "
                if len(Qty) == 1:
                    Qty = "0" + Qty
                while len(str(Qty)) < (10-len(Subtotal)):
                    Qty += " "
                f.write(f"{Product}\t{Qty}\t{Subtotal}\n")
    
        #Footer
        f = open("Receipts Folder/Purchase_Receipt.txt","a")
        f.write("---------------------------------------------\n")
        Last_Line = "Total    :"
        while len(Last_Line)< (45-len(str(Total))):
            Last_Line += " "
        f.write(f"{Last_Line}{Total}")

    elif rdb['kind'] == "Sales":
        #Header
        f = open("Receipts Folder/Sales_Receipt.txt","w")
        f.write("---------------------------------------------\n") #40 Spaces
        f.write(f"Date     :     {today}\n")
        f.write("---------------------------------------------")
        f.write("\n")
        f.close
        
        #Body
        with open("Receipts Folder/Sales_Receipt.txt","a") as f:
            for i in rdb['Order'].keys():
                Product = i
                Qty = str(rdb["Order"][i])
                Subtotal = str(int(Qty) * pdb[i])
                Total += int(Subtotal)
                while len(Product) < (31-len(Qty)):
                    Product += " "
                if len(Qty) == 1:
                    Qty = "0" + Qty
                while len(str(Qty)) < (10-len(Subtotal)):
                    Qty += " "
                f.write(f"{Product}\t{Qty}\t{Subtotal}\n")
    
        #Footer
        f = open("Receipts Folder/Sales_Receipt.txt","a")
        f.write("---------------------------------------------\n")
        Last_Line = "Total    :"
        while len(Last_Line)< (45-len(str(Total))):
            Last_Line += " "
        f.write(f"{Last_Line}{Total}")   
  
Receipt_Maker()