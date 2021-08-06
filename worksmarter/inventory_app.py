from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
from datetime import date
import ws_database as db
import receipt_writer as rw
import authentication
import logging
import os
import receipt_writer
import datetime

app = Flask(__name__)

app.secret_key = b'secretkey'

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

navbar = """
         <a href='/login'>Login</a> | <a href='/user_interface_page'>User interface</a> | <a href='/saleslog'>Sales Log</a> |
         <a href='/order_input'>Order input</a> | <a href='/receipt'>Receipt</a> | <a href='/deliveryconfirmation'>Delivery confirmation</a>
         <p/>
         """

@app.route('/')
def welcome():
    return render_template("home.html", page="Login")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html", page="Login")

@app.route('/auth',methods=["GET","POST"])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, admin = authentication.login(username,password)
    app.logger.info("%s", is_successful)
    if(is_successful):
        session["admin"] = admin
        return redirect('/user_interface_page')
    else:
        return redirect('/login')

@app.route('/order_input', methods=["GET","POST"])
def orderinput():
    store_pricing_list=db.get_store_pricing()
    if request.method == "POST":
        req = request.form
        d = date.today().strftime("%m/%d/%Y")
        product_name = req.get("product")
        qty = int(req.get("quantity"))
        price = db.get_price(product_name)
        subtotal = qty*price
        qty<= db.get_product_inventory(product_name)
        db.input_sales(d,product_name,qty,price,subtotal)
        db.subtract_current_inventory(product_name,qty)
        db.add_sr_content(d,product_name,qty)
        rw.Receipt_Maker()
    return render_template("orderinput.html", page="Order input",store_pricing_list=store_pricing_list)


@app.route('/logout')
def logout():
    return redirect("/")

@app.route('/user_interface_page')
def userinterfacepage():
    return render_template("userinterface.html", page="User interface")

@app.route('/saleslog',methods=["GET","POST"])
def saleslog():
    sales_log_list = db.get_sales_log()
    return render_template("saleslog.html", page="Sales Log",sales_log_list=sales_log_list)

@app.route('/purchaselog')
def purchaselog():
    purchase_log_list = db.get_purchase_log()
    return render_template("purchaselog.html", page="Purchase Log",purchase_log_list=purchase_log_list)

@app.route('/salesreceipts',methods=["GET","POST"])
def salesreceipt():
    sales_receipts = db.get_sales_receipts()
    return render_template("salesreceipts.html", page="Sales Receipt",sales_receipts=sales_receipts)

@app.route('/purchasereceipts',methods=["GET","POST"])
def purchasereceipt():
    purchase_receipts = db.get_purchase_receipts()
    return render_template("purchasereceipts.html", page="Purchase Receipt",purchase_receipts=purchase_receipts)

@app.route("/receipt_reader",methods=["GET","POST"])
def receipt_reader():
    receipt = request.form.get('receipt')
    text = db.read_receipt(receipt)
    return render_template("receipt_reader.html",page="Receipt_Reader",receipt=receipt,text=text)

@app.route('/currentinventory')
def currentinventory():
    current_inventory_list = db.get_current_inventory()
    return render_template("currentinventory.html", page="Current Inventory",current_inventory_list=current_inventory_list)

@app.route('/deliveryconfirmation')
def deliveryconfirmation():
    return render_template("deliveryconfirmation.html", page="delivery confirmation")

@app.route('/salesreceiptsmaker')
def salesreceiptsmaker():
    return render_template("salesreceiptsmaker.html",page="SalesrReceiptsMaker")

@app.route('/salesrecprg',methods=["GET","POST"])
def salesrecprg():
    if request.method=="POST":
        day = request.form.get('day')
        kind = request.form.get('kind')
        receipt_writer.sales_content_writer(day)
        receipt_writer.Receipt_Maker(kind,day)
        sales_receipts = db.get_sales_receipts()
    return render_template("salesreceipts.html", page="Sales Receipt",sales_receipts=sales_receipts)

if __name__ == '__main__':
    app.run(debug=True)
