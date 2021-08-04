admin = {"nottheavreagejoe":            {"password":"imnotjoeking",
                                        "first_name": "Joe",
                                        "last_name":"Ilagan"},

         "reesepeanutbuttercups":       {"password": "onlyrealpeanutbutter",
                                        "first_name" :"Reese",
                                        "last_name":"Amores"},

         "jablue":                      {"password": "myfavecolorisred",
                                        "first_name": "Jared",
                                        "last_name":"Ong"},

         "uusedtocolynonmycellphone":   {"password": "hotlinebling$$",
                                        "first_name": "Colyn",
                                        "last_name": "Ching"},

         "theoneandshanlyone":          {"password" : "shanisnotasheep",
                                        "first_name" :"Shan",
                                        "last_name" :"Porres"}}

def get_user(username):
    try:
       return admin[username]
    except KeyError:
       return None

sales_log = {"01/02/2021" : {"Dairy King Ice Cream": {"Quantity": 1, "Price": 2500},
                            "Mrs.Chips" : {"Quantity": 1, "Price": 1800},
                            "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500}},

            "01/03/2021" : {"Venus Chocolate Bars" : {"Quantity": 1 , "Price": 4600},
                           "Bullhead Milk" : {"Quantity": 2, "Price": 2500},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650}},

            "01/04/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},

            "01/06/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 1, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 1, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

             "01/07/2021" : {"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                             "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 2, "Price": 2500}},

             "01/08/2021" :{"Mrs. Chips" : {"Quantity": 2, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

             "01/09/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000}},

             "01/10/2021" :{"Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "01/11/2021" :{"Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000}},

             "01/12/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Silver Duck Soy Sauce" : {"Quantity": 2, "Price": 1300},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "01/13/2021" :{"Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500}},

             "01/14/2021" :{"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "01/15/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "01/16/2021" :{"Royal Cola" : {"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500},
                           "Mila's Chocolate Milk" : {"Quantity": 2, "Price": 2500},
                           "Rita Round Biscuits" : {"Quantity": 1, "Price": 270}},

             "01/17/2021" :{"Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Col Git Toothpaste" : {"Quantity": 1, "Price": 1350}},

             "01/18/2021" :{"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Mayon Blue Salt" : {"Quantity": 1, "Price": 2700},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "01/19/2021" :{"Mila's Chocolate Milk" : {"Quantity": 1, "Price": 2500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "01/20/2021" :{"Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500}},

             "01/21/2021" :{"Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Royal Cola" : {"Quantity": 1, "Price": 2270}},

             "01/22/2021" :{"Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},

             "01/23/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "01/24/2021" :{"Mila's Chocolate Milk":{"Quantity": 1, "Price": 2500},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo":{"Quantity": 1, "Price": 650}},

             "01/25/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "01/26/2021" :{"Don Rox Bleach":{"Quantity": 1, "Price": 4500},
                           "Lucky Mo Big Noodles":{"Quantity": 1, "Price": 400},
                           "Magnolia Garlic Bread":{"Quantity": 1, "Price": 4500}},

             "01/27/2021" :{"Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Bullhead Milk":{"Quantity": 1, "Price": 2500}},

             "01/28/2021" :{"NPA Rice" : {"Quantity": 1, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

             "01/29/2021" :{"Royal Cola" : {"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500},
                           "Mila's Chocolate Milk" : {"Quantity": 2, "Price": 2500},
                           "Rita Round Biscuits" : {"Quantity": 1, "Price": 270}},

              "01/30/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},


             "02/01/2021" :{"Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

             "02/02/2021" :{"NPA Rice" : {"Quantity": 1, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

             "02/04/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "02/05/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "02/06/2021" :{"NPA Rice" : {"Quantity": 5, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "02/07/2021" :{"Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Col Git Toothpaste" : {"Quantity": 1, "Price": 1350}},

             "02/08/2021" : {"Dairy King Ice Cream": {"Quantity": 1, "Price": 2500},
                            "Mrs.Chips" : {"Quantity": 1, "Price": 1800},
                            "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500}},

             "02/09/2021" :{"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "02/10/2021" :{"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Mayon Blue Salt" : {"Quantity": 1, "Price": 2700},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "02/11/2021" : {"Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 3, "Price": 2500}},

             "02/12/2021" :{"Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500}},

             "02/13/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "02/14/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "02/15/2021" :{"NPA Rice" : {"Quantity": 3, "Price": 750},
                           "Royal Cola" :{"Quantity": 4, "Price": 2270},
                           "Mrs. Chips":{"Quantity": 2, "Price": 1800}},

             "02/16/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 3, "Price": 2500}},

             "02/17/2021" :{"Magnolia Garlic Bread" : {"Quantity": 4, "Price": 4500},
                           "Datu Itim Vinegar" : {"Quantity": 3, "Price": 2000}},

             "02/18/2021" :{"Mila's Chocolate Milk":{"Quantity": 1, "Price": 2500},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo":{"Quantity": 1, "Price": 650}},

             "02/19/2021" :{"Don Rox Bleach":{"Quantity": 2, "Price": 4500},
                           "Lucky Mo Big Noodles":{"Quantity": 5, "Price": 400},
                           "Magnolia Garlic Bread":{"Quantity": 6, "Price": 4500}},

             "02/20/2021" :{"Mila's Chocolate Milk" : {"Quantity": 5, "Price": 2500}},

             "02/21/2021" :{"Royal Cola" :{"Quantity": 3, "Price": 2270},
                           "NPA Rice" :{"Quantity": 7, "Price": 750}},

             "02/23/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 5, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 2, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

             "02/25/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Silver Duck Soy Sauce" : {"Quantity": 2, "Price": 1300},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "02/26/2021" :{"Dairy King Ice Cream":{"Quantity": 2, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 4, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "02/28/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "03/02/2021" :{"Mila's Chocolate Milk" : {"Quantity": 4, "Price": 2500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "03/03/2021" :{"Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Royal Cola" : {"Quantity": 3, "Price": 2270}},

             "03/04/2021" : {"Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 3, "Price": 2500}},

             "03/06/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 6, "Price": 2500}},

             "03/07/2021" :{"Dairy King Ice Cream" : {"Quantity": 2, "Price": 3700},
                           "Royal Cola" : {"Quantity": 5, "Price": 2270}},

             "03/08/2021" :{"NPA Rice" : {"Quantity": 5, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "03/10/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 2, "Price": 2500}},

            "03/12/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

            "03/14/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

            "03/16/2021" :{"NPA Rice" : {"Quantity": 3, "Price": 750},
                           "Royal Cola" :{"Quantity": 4, "Price": 2270},
                           "Mrs. Chips":{"Quantity": 2, "Price": 1800}},

            "03/19/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 3, "Price": 2500}},

            "03/20/2021" :{"Mila's Chocolate Milk" : {"Quantity": 1, "Price": 2500}},

            "03/23/2021" :{"Royal Cola" :{"Quantity": 3, "Price": 2270},
                           "NPA Rice" :{"Quantity": 7, "Price": 750}},

            "03/24/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 5, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 2, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

            "03/25/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},


            "03/27/2021" :{"Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

            "03/30/2021" :{"NPA Rice" : {"Quantity": 1, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

            "03/31/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 2, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 3, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

             "04/02/2021" : {"Bullhead Milk" : {"Quantity": 5, "Price": 2500},
                             "Datu Itim Vinegar" : {"Quantity": 3, "Price": 2000},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 3, "Price": 2500}},

             "04/03/2021" :{"Mrs. Chips" : {"Quantity": 2, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 2, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 2, "Price": 3700}},

             "04/05/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000}},

             "04/09/2021" :{"Silver Duck Soy Sauce" : {"Quantity": 5, "Price": 1300},
                           "Dairy King Ice Cream" : {"Quantity": 3, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "04/10/2021" :{"Magnolia Garlic Bread" : {"Quantity": 5, "Price": 4500},
                           "Datu Itim Vinegar" : {"Quantity": 3, "Price": 2000}},

             "04/13/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "04/15/2021" :{"Royal Cola" : {"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500},
                           "Mila's Chocolate Milk" : {"Quantity": 2, "Price": 2500},
                           "Rita Round Biscuits" : {"Quantity": 1, "Price": 270}},

             "04/16/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},


             "04/18/2021" :{"Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

            "04/21/2021" :{"NPA Rice" : {"Quantity": 4, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

             "04/22/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "04/25/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "04/28/2021" :{"NPA Rice" : {"Quantity": 5, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "04/29/2021" :{"Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Col Git Toothpaste" : {"Quantity": 1, "Price": 1350}},

             "05/01/2021" : {"Dairy King Ice Cream": {"Quantity": 3, "Price": 2500},
                            "Mrs.Chips" : {"Quantity": 1, "Price": 1800},
                            "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500}},

             "05/03/2021" :{"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "05/04/2021" :{"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Mayon Blue Salt" : {"Quantity": 1, "Price": 2700},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "05/06/2021" : {"Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 3, "Price": 2500}},

             "05/09/2021" :{"Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500}},

             "05/10/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

                         "01/03/2021" : {"Venus Chocolate Bars" : {"Quantity": 1 , "Price": 4600},
                           "Bullhead Milk" : {"Quantity": 2, "Price": 2500},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650}},

            "05/11/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},

            "05/13/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 1, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 1, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

             "05/16/2021" : {"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                             "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 2, "Price": 2500}},

             "05/17/2021" :{"Mrs. Chips" : {"Quantity": 2, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

             "05/18/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000}},

             "05/19/2021" :{"Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "05/20/2021" :{"Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000}},

             "05/21/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Silver Duck Soy Sauce" : {"Quantity": 2, "Price": 1300},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "05/23/2021" :{"Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500}},

             "05/24/2021" :{"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "05/25/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "05/26/2021" :{"Royal Cola" : {"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500},
                           "Mila's Chocolate Milk" : {"Quantity": 2, "Price": 2500},
                           "Rita Round Biscuits" : {"Quantity": 1, "Price": 270}},

             "05/28/2021" :{"Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Col Git Toothpaste" : {"Quantity": 1, "Price": 1350}},

             "05/30/2021" :{"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Mayon Blue Salt" : {"Quantity": 1, "Price": 2700},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "06/01/2021" :{"Mila's Chocolate Milk" : {"Quantity": 1, "Price": 2500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "06/03/2021" :{"Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500}},

             "06/04/2021" :{"Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Royal Cola" : {"Quantity": 1, "Price": 2270}},

             "06/05/2021" :{"Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},

             "06/06/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "06/08/2021" :{"Mila's Chocolate Milk":{"Quantity": 1, "Price": 2500},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo":{"Quantity": 1, "Price": 650}},

             "06/09/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "06/11/2021" :{"Don Rox Bleach":{"Quantity": 1, "Price": 4500},
                           "Lucky Mo Big Noodles":{"Quantity": 1, "Price": 400},
                           "Magnolia Garlic Bread":{"Quantity": 1, "Price": 4500}},

             "06/12/2021" :{"Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Bullhead Milk":{"Quantity": 1, "Price": 2500}},

             "06/13/2021" :{"NPA Rice" : {"Quantity": 1, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

             "06/15/2021" :{"Royal Cola" : {"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500},
                           "Mila's Chocolate Milk" : {"Quantity": 2, "Price": 2500},
                           "Rita Round Biscuits" : {"Quantity": 1, "Price": 270}},

             "06/17/2021" : {"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 1, "Price": 2500}},


             "06/18/2021" :{"Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700}},

             "06/20/2021" :{"NPA Rice" : {"Quantity": 1, "Price": 750},
                           "Royal Cola" :{"Quantity": 1, "Price": 2270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800}},

             "06/21/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "06/22/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "06/23/2021" :{"NPA Rice" : {"Quantity": 5, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "06/25/2021" :{"Panteen Shampoo" : {"Quantity": 1, "Price": 650},
                           "Magnolia Garlic Bread" : {"Quantity": 1, "Price": 4500},
                           "Col Git Toothpaste" : {"Quantity": 1, "Price": 1350}},

             "06/26/2021" : {"Dairy King Ice Cream": {"Quantity": 1, "Price": 2500},
                            "Mrs.Chips" : {"Quantity": 1, "Price": 1800},
                            "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                            "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500}},

             "06/27/2021" :{"Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "06/28/2021" :{"Bullhead Milk" : {"Quantity": 1, "Price": 2500},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Mayon Blue Salt" : {"Quantity": 1, "Price": 2700},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "06/29/2021" : {"Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 3, "Price": 2500}},

             "06/30/2021" :{"Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Don Rox Bleach" : {"Quantity": 1, "Price": 4500}},

             "07/01/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "07/02/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "07/03/2021" :{"NPA Rice" : {"Quantity": 3, "Price": 750},
                           "Royal Cola" :{"Quantity": 4, "Price": 2270},
                           "Mrs. Chips":{"Quantity": 2, "Price": 1800}},

             "07/04/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 3, "Price": 2500}},

             "07/05/2021" :{"Magnolia Garlic Bread" : {"Quantity": 4, "Price": 4500},
                           "Datu Itim Vinegar" : {"Quantity": 3, "Price": 2000}},

             "07/06/2021" :{"Mila's Chocolate Milk":{"Quantity": 1, "Price": 2500},
                           "Mrs. Chips":{"Quantity": 1, "Price": 1800},
                           "Panteen Shampoo":{"Quantity": 1, "Price": 650}},

             "07/08/2021" :{"Don Rox Bleach":{"Quantity": 2, "Price": 4500},
                           "Lucky Mo Big Noodles":{"Quantity": 5, "Price": 400},
                           "Magnolia Garlic Bread":{"Quantity": 6, "Price": 4500}},

             "07/09/2021" :{"Mila's Chocolate Milk" : {"Quantity": 5, "Price": 2500}},

             "07/10/2021" :{"Royal Cola" :{"Quantity": 3, "Price": 2270},
                           "NPA Rice" :{"Quantity": 7, "Price": 750}},

             "07/11/2021" : {"Mila's Chocolate Milk"  : {"Quantity": 5, "Price": 2500},
                           "Venus Chocolate Bars"  : {"Quantity": 2, "Price": 4600},
                           "Beach Fabric Conditioner" : {"Quantity": 2, "Price": 2500}},

             "07/12/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Venus Chocolate Bars" : {"Quantity": 2, "Price": 4600},
                           "Silver Duck Soy Sauce" : {"Quantity": 2, "Price": 1300},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400}},

             "07/13/2021" :{"Dairy King Ice Cream":{"Quantity": 2, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 4, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

             "07/15/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 1, "Price": 2500}},

             "07/16/2021" :{"Mila's Chocolate Milk" : {"Quantity": 4, "Price": 2500},
                           "Mr. Jelly Gulaman Pack" : {"Quantity": 1, "Price": 2500},
                           "Silver Duck Soy Sauce" : {"Quantity": 1, "Price": 1300}},

             "07/18/2021" :{"Dairy King Ice Cream" : {"Quantity": 1, "Price": 3700},
                           "Lucky Mo Big Noodles" : {"Quantity": 1, "Price": 400},
                           "Royal Cola" : {"Quantity": 3, "Price": 2270}},

             "07/19/2021" : {"Datu Itim Vinegar" : {"Quantity": 2, "Price": 2000},
                           "Beach Fabric Conditioner" : {"Quantity": 3, "Price": 2500}},

             "07/20/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 6, "Price": 2500}},

             "07/21/2021" :{"Dairy King Ice Cream" : {"Quantity": 2, "Price": 3700},
                           "Royal Cola" : {"Quantity": 5, "Price": 2270}},

             "07/22/2021" :{"NPA Rice" : {"Quantity": 5, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

             "07/25/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 2, "Price": 2500}},

             "07/26/2021" :{"Dairy King Ice Cream":{"Quantity": 1, "Price": 3700},
                           "Mr. Jelly Gulaman Pack":{"Quantity": 1, "Price": 2500},
                           "Brava Biscuits":{"Quantity": 1, "Price": 570}},

            "07/27/2021" :{"NPA Rice" : {"Quantity": 2, "Price": 750},
                           "Rita Round Biscuits" :{"Quantity": 1, "Price": 270},
                           "Silver Duck Soy Sauce":{"Quantity": 1, "Price": 1300},
                           "Mayon Blue Salt":{"Quantity": 1, "Price": 2700}},

            "07/28/2021" :{"NPA Rice" : {"Quantity": 3, "Price": 750},
                           "Royal Cola" :{"Quantity": 4, "Price": 2270},
                           "Mrs. Chips":{"Quantity": 2, "Price": 1800}},

            "07/29/2021" :{"Brava Biscuits" : {"Quantity": 1, "Price": 570},
                           "Select Vanilla Ice Cream" : {"Quantity": 1, "Price": 2500},
                           "Datu Itim Vinegar" : {"Quantity": 1, "Price": 2000},
                           "Mrs. Chips" : {"Quantity": 1, "Price": 1800},
                           "Bullhead Milk" : {"Quantity": 3, "Price": 2500}},

            "07/30/2021" :{"Mila's Chocolate Milk" : {"Quantity": 1, "Price": 2500}},

            "07/31/2021" :{"Royal Cola" :{"Quantity": 3, "Price": 2270},
                           "NPA Rice" :{"Quantity": 7, "Price": 750}}


        }
def get_sales_log():
    sales_log_list = []

    sales_log_dict={}
    for i,v in sales_log.items():
        for k in v:
            sales_log_dict[i]={"date":i,"product":k,"quantity":v[k]["Quantity"],"price":v[k]["Price"]}
            log = sales_log_dict[i]
            sales_log_list.append(log)


    return sales_log_list


purchase_log ={
            "01/02/2021" : {"Beach Fabric Conditioner":{"Quantity": 5, "Price" : 2356},
                           "Bullhead Milk"            :{"Quantity": 5, "Price" : 2000},
                           "Dairy King Ice Cream"     :{"Quantity": 3, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 4, "Price" : 1750},
                           "Mila's Chocolate Milk"    :{"Quantity": 3, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 5, "Price" : 2100},
                           "Mrs. Chips"               :{"Quantity": 4, "Price" : 1500},
                           "Panteen Shampoo"          :{"Quantity": 5, "Price" : 450},
                           "Select Vanilla Ice Cream" :{"Quantity": 3, "Price" : 2000},
                           "Venus Chocolate Bars"     :{"Quantity": 3, "Price" : 4000}},
            "01/09/2021" : {"Brava Biscuits"          :{"Quantity": 5, "Price" : 500},
                           "Dairy King Ice Cream"     :{"Quantity": 4, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 7, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 3, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 7, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 4, "Price" : 4231},
                           "Mrs. Chips"               :{"Quantity": 4, "Price" : 1500},
                           "Select Vanilla Ice Cream" :{"Quantity": 2, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 6, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 5, "Price" : 4000}},
            "01/16/2021" : {"Beach Fabric Conditioner":{"Quantity": 4, "Price" : 2356},
                           "Bullhead Milk"            :{"Quantity": 3, "Price" : 2000},
                           "Col Git Toothpaste"       :{"Quantity": 3, "Price" : 1240},
                           "Dairy King Ice Cream"     :{"Quantity": 2, "Price" : 3200},
                           "Don Rox Bleach"           :{"Quantity": 3, "Price" : 4200},
                           "Magnolia Garlic Bread"    :{"Quantity": 5, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Mila's Chocolate Milk"    :{"Quantity": 9, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 4, "Price" : 2100},
                           "Mrs. Chips"               :{"Quantity": 5, "Price" : 1500},
                           "Rita Round Biscuits"      :{"Quantity": 4, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 10, "Price" : 2150},
                           "Silver Duck Soy Sauce"    :{"Quantity": 7, "Price" : 1250}},
            "01/23/2021" : {"Brava Biscuits"          :{"Quantity": 5, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 6, "Price" : 2000},
                           "Dairy King Ice Cream"     :{"Quantity": 4, "Price" : 3200},
                           "Mila's Chocolate Milk"    :{"Quantity": 9, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 7, "Price" : 2100},
                           "Mrs. Chips"               :{"Quantity": 5, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 20, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 6, "Price" : 450},
                           "Rita Round Biscuits"      :{"Quantity": 5, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 8, "Price" : 2150},
                           "Silver Duck Soy Sauce"    :{"Quantity": 3, "Price" : 1250}},
            "01/30/2021" : {"Beach Fabric Conditioner":{"Quantity": 5, "Price" : 2356},
                           "Datu Itim Vinegar"        :{"Quantity": 5, "Price" : 1750},
                           "Magnolia Garlic Bread"    :{"Quantity": 7, "Price" : 4231},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 8, "Price" : 2100},
                           "NPA Rice"                 :{"Quantity": 5, "Price" : 567},
                           "Silver Duck Soy Sauce"    :{"Quantity": 2, "Price" : 1250}},

            "02/06/2021" : {"Brava Biscuits"          :{"Quantity": 3, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 4, "Price" : 2000},
                           "Dairy King Ice Cream"     :{"Quantity": 8, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 3, "Price" : 1750},
                           "Lucky Mo Big Noodles"     :{"Quantity": 9, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 10, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 6, "Price" : 2300},
                           "Mila's Chocolate Milk"    :{"Quantity": 8, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 3, "Price" : 2100},
                           "NPA Rice"                 :{"Quantity": 12, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 3, "Price" : 450},
                           "Royal Cola"               :{"Quantity": 9, "Price" : 2150},
                           "Select Vanilla Ice Cream" :{"Quantity": 3, "Price" : 2000},
                           "Venus Chocolate Bars"     :{"Quantity": 9, "Price" : 4000}},
            "02/13/2021" : {"Beach Fabric Conditioner":{"Quantity": 9, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 3, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 6, "Price" : 2000},
                           "Datu Itim Vinegar"        :{"Quantity": 4, "Price" : 1750}},
            "02/20/2021" : {"Bullhead Milk"           :{"Quantity": 10, "Price" : 2000},
                           "Dairy King Ice Cream"     :{"Quantity": 3, "Price" : 3200},
                           "Don Rox Bleach"           :{"Quantity": 4, "Price" : 4200},
                           "Magnolia Garlic Bread"    :{"Quantity": 7, "Price" : 4231},
                           "Mila's Chocolate Milk"    :{"Quantity": 9, "Price" : 2300},
                           "Mrs. Chips"               :{"Quantity": 10, "Price" : 1500},
                           "Rita Round Biscuits"      :{"Quantity": 7, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 9, "Price" : 2150},
                           "Silver Duck Soy Sauce"    :{"Quantity": 5, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 3, "Price" : 4000}},
            "02/27/2021" : {"Bullhead Milk"           :{"Quantity": 7, "Price" : 2000},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Rita Round Biscuits"      :{"Quantity": 5, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 3, "Price" : 2150},
                           "Silver Duck Soy Sauce"    :{"Quantity": 7, "Price" : 1250}},

            "03/06/2021" : {"Beach Fabric Conditioner":{"Quantity": 7, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 4, "Price" : 500},
                           "Dairy King Ice Cream"     :{"Quantity": 7, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 3, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 6, "Price" : 4200},
                           "Mila's Chocolate Milk"    :{"Quantity": 2, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 6, "Price" : 2100},
                           "Mrs. Chips"               :{"Quantity": 2, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 6, "Price" : 567},
                           "Royal Cola"               :{"Quantity": 0, "Price" : 2150},
                           "Select Vanilla Ice Cream" :{"Quantity": 8, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 2, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 9, "Price" : 4000}},
            "03/13/2021" : {"Datu Itim Vinegar"       :{"Quantity": 7, "Price" : 1750},
                           "Lucky Mo Big Noodles"     :{"Quantity": 5, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 6, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 3, "Price" : 2300},
                           "Panteen Shampoo"          :{"Quantity": 9, "Price" : 450}},
            "03/20/2021" : {"Beach Fabric Conditioner":{"Quantity": 10, "Price" : 2356},
                           "Bullhead Milk"            :{"Quantity": 9, "Price" : 2000},
                           "Lucky Mo Big Noodles"     :{"Quantity": 6, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 8, "Price" : 4231},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 6, "Price" : 2100},
                           "Royal Cola"               :{"Quantity": 8, "Price" : 2150},
                           "Select Vanilla Ice Cream" :{"Quantity": 10, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 9, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 12, "Price" : 4000}},
            "03/27/2021" : {"Dairy King Ice Cream"    :{"Quantity": 5, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 8, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 9, "Price" : 4200},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Mila's Chocolate Milk"    :{"Quantity": 5, "Price" : 2300},
                           "Mrs. Chips"               :{"Quantity": 6, "Price" : 1500},
                           "Panteen Shampoo"          :{"Quantity": 7, "Price" : 450},
                           "Select Vanilla Ice Cream" :{"Quantity": 10, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 4, "Price" : 1250}},

            "04/03/2021" : {"Brava Biscuits"          :{"Quantity": 8, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 4, "Price" : 2000},
                           "Dairy King Ice Cream"     :{"Quantity": 7, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 3, "Price" : 1750},
                           "Lucky Mo Big Noodles"     :{"Quantity": 8, "Price" : 500},
                           "NPA Rice"                 :{"Quantity": 9, "Price" : 567},
                           "Royal Cola"               :{"Quantity": 10, "Price" : 2150},
                           "Silver Duck Soy Sauce"    :{"Quantity": 7, "Price" : 1250}},
            "04/10/2021" : {"Beach Fabric Conditioner":{"Quantity": 6, "Price" : 2356},
                           "Col Git Toothpaste"       :{"Quantity": 3, "Price" : 1240},
                           "Don Rox Bleach"           :{"Quantity": 8, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 4, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 6, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 10, "Price" : 2300},
                           "Mila's Chocolate Milk"    :{"Quantity": 5, "Price" : 2300},
                           "Mrs. Chips"               :{"Quantity": 7, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 9, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 3, "Price" : 450},
                           "Rita Round Biscuits"      :{"Quantity": 12, "Price" : 250}},
            "04/17/2021" : {"Beach Fabric Conditioner":{"Quantity": 6, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 9, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 10, "Price" : 2000},
                           "Col Git Toothpaste"       :{"Quantity": 6, "Price" : 1240},
                           "Dairy King Ice Cream"     :{"Quantity": 7, "Price" : 3200},
                           "Don Rox Bleach"           :{"Quantity": 3, "Price" : 4200},
                           "Magnolia Garlic Bread"    :{"Quantity": 6, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Mila's Chocolate Milk"    :{"Quantity": 6, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 1, "Price" : 2100},
                           "Royal Cola"               :{"Quantity": 9, "Price" : 2150},
                           "Venus Chocolate Bars"     :{"Quantity": 10, "Price" : 4000}},
            "04/24/2021" : {"Lucky Mo Big Noodles"    :{"Quantity": 7, "Price" : 500},
                           "NPA Rice"                 :{"Quantity": 13, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 6, "Price" : 450},
                           "Rita Round Biscuits"      :{"Quantity": 4, "Price" : 250},
                           "Select Vanilla Ice Cream" :{"Quantity": 9, "Price" : 2000}},

            "05/01/2021" : {"Beach Fabric Conditioner":{"Quantity": 2, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 7, "Price" : 500},
                           "Col Git Toothpaste"       :{"Quantity": 10, "Price" : 1240},
                           "Don Rox Bleach"           :{"Quantity": 4, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 9, "Price" : 500},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 7, "Price" : 2100},
                           "Rita Round Biscuits"      :{"Quantity": 9, "Price" : 250}},
            "05/08/2021" : {"Beach Fabric Conditioner":{"Quantity": 12, "Price" : 2356},
                           "Datu Itim Vinegar"        :{"Quantity": 5, "Price" : 1750},
                           "Magnolia Garlic Bread"    :{"Quantity": 8, "Price" : 4231},
                           "Mila's Chocolate Milk"    :{"Quantity": 4, "Price" : 2300},
                           "Mrs. Chips"               :{"Quantity": 8, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 5, "Price" : 567},
                           "Royal Cola"               :{"Quantity": 9, "Price" : 2150},
                           "Select Vanilla Ice Cream" :{"Quantity": 3, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 6, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 9, "Price" : 4000}},
            "05/15/2021" : {"Lucky Mo Big Noodles"    :{"Quantity": 3, "Price" : 500},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 9, "Price" : 2100},
                           "NPA Rice"                 :{"Quantity": 15, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 4, "Price" : 450},
                           "Rita Round Biscuits"      :{"Quantity": 8, "Price" : 250},
                           "Silver Duck Soy Sauce"    :{"Quantity": 8, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 4, "Price" : 4000}},
            "05/22/2021" : {"Beach Fabric Conditioner":{"Quantity": 6, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 7, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 4, "Price" : 2000},
                           "Col Git Toothpaste"       :{"Quantity": 4, "Price" : 1240},
                           "Datu Itim Vinegar"        :{"Quantity": 6, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 2, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 9, "Price" : 500},
                           "Mila's Chocolate Milk"    :{"Quantity": 10, "Price" : 2300},
                           "Select Vanilla Ice Cream" :{"Quantity": 4, "Price" : 2000}},
            "05/29/2021" : {"Dairy King Ice Cream"    :{"Quantity": 5, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 3, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 6, "Price" : 4200},
                           "Magnolia Garlic Bread"    :{"Quantity": 9, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 5, "Price" : 2100},
                           "Mrs. Chips"               :{"Quantity": 8, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 4, "Price" : 567},
                           "Rita Round Biscuits"      :{"Quantity": 3, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 13, "Price" : 2150}},

            "06/05/2021" : {"Beach Fabric Conditioner":{"Quantity": 5, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 3, "Price" : 500},
                           "Col Git Toothpaste"       :{"Quantity": 7, "Price" : 1240},
                           "Lucky Mo Big Noodles"     :{"Quantity": 9, "Price" : 500},
                           "Rita Round Biscuits"      :{"Quantity": 3, "Price" : 250},
                           "Venus Chocolate Bars"     :{"Quantity": 7, "Price" : 4000}},
            "06/12/2021" : {"Col Git Toothpaste"      :{"Quantity": 5, "Price" : 1240},
                           "Datu Itim Vinegar"        :{"Quantity": 3, "Price" : 1750},
                           "Mayon Blue Salt"          :{"Quantity": 3, "Price" : 2300},
                           "NPA Rice"                 :{"Quantity": 7, "Price" : 567},
                           "Select Vanilla Ice Cream" :{"Quantity": 2, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 6, "Price" : 1250}},
            "06/19/2021" : {"Brava Biscuits"          :{"Quantity": 1, "Price" : 500},
                           "Dairy King Ice Cream"     :{"Quantity": 5, "Price" : 3200},
                           "Datu Itim Vinegar"        :{"Quantity": 8, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 4, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 9, "Price" : 500},
                           "Mila's Chocolate Milk"    :{"Quantity": 6, "Price" : 2300},
                           "NPA Rice"                 :{"Quantity": 8, "Price" : 567},
                           "Rita Round Biscuits"      :{"Quantity": 3, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 9, "Price" : 2150}},
            "06/26/2021" : {"Lucky Mo Big Noodles"    :{"Quantity": 5, "Price" : 500},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 6, "Price" : 2100},
                           "NPA Rice"                 :{"Quantity": 9, "Price" : 567},
                           "Panteen Shampoo"          :{"Quantity": 2, "Price" : 450},
                           "Silver Duck Soy Sauce"    :{"Quantity": 5, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 6, "Price" : 4000}},

            "07/03/2021" : {"Beach Fabric Conditioner":{"Quantity": 9, "Price" : 2356},
                           "Bullhead Milk"            :{"Quantity": 2, "Price" : 2000},
                           "Brava Biscuits"           :{"Quantity": 6, "Price" : 500},
                           "Col Git Toothpaste"       :{"Quantity": 7, "Price" : 1240},
                           "Datu Itim Vinegar"        :{"Quantity": 4, "Price" : 1750},
                           "Don Rox Bleach"           :{"Quantity": 7, "Price" : 4200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 4, "Price" : 500},
                           "Mayon Blue Salt"          :{"Quantity": 2, "Price" : 2300},
                           "Mrs. Chips"               :{"Quantity": 7, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 11, "Price" : 567},
                           "Rita Round Biscuits"      :{"Quantity": 5, "Price" : 250}},
            "07/10/2021" : {"Dairy King Ice Cream"    :{"Quantity": 7, "Price" : 3200},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 4, "Price" : 2100},
                           "Panteen Shampoo"          :{"Quantity": 6, "Price" : 450},
                           "Select Vanilla Ice Cream" :{"Quantity": 9, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 4, "Price" : 1250},
                           "Venus Chocolate Bars"     :{"Quantity": 8, "Price" : 4000}},
            "07/17/2021" : {"Beach Fabric Conditioner":{"Quantity": 3, "Price" : 2356},
                           "Brava Biscuits"           :{"Quantity": 6, "Price" : 500},
                           "Col Git Toothpaste"       :{"Quantity": 9, "Price" : 1240},
                           "Dairy King Ice Cream"     :{"Quantity": 2, "Price" : 3200},
                           "Don Rox Bleach"           :{"Quantity": 6, "Price" : 4200},
                           "Mrs. Chips"               :{"Quantity": 7, "Price" : 1500},
                           "Venus Chocolate Bars"     :{"Quantity": 9, "Price" : 4000},
                           "Rita Round Biscuits"      :{"Quantity": 3, "Price" : 250}},
            "07/24/2021" : {"Dairy King Ice Cream"    :{"Quantity": 6, "Price" : 3200},
                           "Lucky Mo Big Noodles"     :{"Quantity": 3, "Price" : 500},
                           "Magnolia Garlic Bread"    :{"Quantity": 8, "Price" : 4231},
                           "Mayon Blue Salt"          :{"Quantity": 9, "Price" : 2300},
                           "Mr. Jelly Gulaman Pack"   :{"Quantity": 3, "Price" : 2100},
                           "NPA Rice"                 :{"Quantity": 5, "Price" : 567},
                           "Select Vanilla Ice Cream" :{"Quantity": 3, "Price" : 2000}},
            "07/31/2021" : {"Brava Biscuits"          :{"Quantity": 6, "Price" : 500},
                           "Bullhead Milk"            :{"Quantity": 2, "Price" : 2000},
                           "Col Git Toothpaste"       :{"Quantity": 5, "Price" : 1240},
                           "Dairy King Ice Cream"     :{"Quantity": 6, "Price" : 3200},
                           "Don Rox Bleach"           :{"Quantity": 4, "Price" : 4200},
                           "Mrs. Chips"               :{"Quantity": 6, "Price" : 1500},
                           "NPA Rice"                 :{"Quantity": 9, "Price" : 567},
                           "Rita Round Biscuits"      :{"Quantity": 3, "Price" : 250},
                           "Royal Cola"               :{"Quantity": 6, "Price" : 2150},
                           "Select Vanilla Ice Cream" :{"Quantity": 6, "Price" : 2000},
                           "Silver Duck Soy Sauce"    :{"Quantity": 3, "Price" : 1250}}}

def get_purchase_log():
    purchase_log_list = []

    purchase_log_dict={}
    for i,v in purchase_log.items():
        for k in v:
            purchase_log_dict[i]={"date":i,"product":k,"quantity":v[k]["Quantity"],"price":v[k]["Price"]}
            log = purchase_log_dict[i]
            purchase_log_list.append(log)


    return purchase_log_list
