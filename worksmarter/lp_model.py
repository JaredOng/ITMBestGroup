import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from sklearn.linear_model import LinearRegression

f = open("Databases/Capacity_Inventory_List.json")
Capacity_Inventory_List = json.load(f)
f = open("Databases/Sales_Log.json")
sales_log = json.load(f)
f = open("Databases/Product_List.json")
Product_List = json.load(f)
f = open("Databases/Supplier_Database.json")
Supplier_Database = json.load(f)
f = open("Databases/IdealProductList.json")
next_days = json.load(f)
f = open("Databases/Current_Inventory.json")
Current_Inventory = json.load(f)

#LP MODEL
def LP_Model():
    next_day = {}
    for items in Capacity_Inventory_List:
        graph_items = []
        temp = 0
        for i, dates in enumerate(sales_log):
            if i % 7 != 0:
                try:
                    temp += sales_log[dates][items]["Quantity"]
                except:
                    temp += 0
            else:
                graph_items.append(temp)
                temp = 0
        x = np.array(graph_items).reshape((-1, 1))
        y = np.array(range(len(graph_items)))
        model = LinearRegression().fit(x, y)
        if int(model.intercept_ + model.coef_ * len(graph_items)+1) >= 0:
            next_day[items] = int(model.intercept_ + model.coef_ * len(graph_items)+1) #NEXT WEEK
        else:
            next_day[items] = 0
    with open("Databases/IdealProductList.json", "w") as filez: #write
        json.dump(next_day, filez)
    return next_day

def Report_Generator():
    for items in Capacity_Inventory_List:
        graph_items = []
        temp = 0
        for i, dates in enumerate(sales_log):
            if i % 7 != 0:
                try:
                    temp += sales_log[dates][items]["Quantity"]
                except:
                    temp += 0
            else:
                graph_items.append(temp)
                temp = 0
        fig, ax = plt.subplots()
        ax.plot(range(len(graph_items)), graph_items )
        ax.set_xlabel("Week #")
        ax.set_ylabel("Quantity of Product")
        ax.set_title(items+ " Sales History")
        fig.savefig("Product_Graphs/LP_"+ items + ".png")
        plt.close(fig)


def Profit_list_func():
    Profit_list = {}
    for items in Product_List:
        for supplier in Supplier_Database:
            try:
                Profit_list[items] = Product_List[items] - Supplier_Database[supplier]["Products_CostsPHP"][items]
            except:
                pass
    return Profit_list

def To_Purchase_func():
    import json
    To_Purchase = {}
    for item in next_days:
        if next_days[item] - Current_Inventory[item] >= 0:
            To_Purchase[item] = next_days[item] - Current_Inventory[item]
        else:
            To_Purchase[item] = 0
    return To_Purchase
