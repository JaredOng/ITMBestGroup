import json
def price_change(product,value):
    f = open("Product_List.json")
    pdb = json.load(f)

    pdb[product] = value

    with open('Product_List.json',"w")as d:
        json.dump(pdb,d,indent=4)