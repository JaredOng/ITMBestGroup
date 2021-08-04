from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
import ws_database as db
import authentication
import logging

app = Flask(__name__)

app.secret_key = b'secretkey'

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

navbar = """
         <a href='/login'>Login</a> | <a href='/user_interface_page'>User interface</a> | <a href='/saleslog'>Sales Log</a> |
         <a href='/order_input'>Order input</a> | <a href='/receipt'>Receipt</a> | <a href='/deliveryconfirmation'>Delivery confirmation</a>
         <p/>
         """

@app.route('/',methods=["GET","POST"])
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

@app.route('/logout')
def logout():
    session.pop("admin",None)
    return redirect("/")

@app.route('/user_interface_page')
def userinterfacepage():
    return render_template("userinterface.html", page="User interface")

@app.route('/saleslog')
def saleslog():
    sales_log_list = db.get_sales_log()
    return render_template("saleslog.html", page="Sales Log",sales_log_list=sales_log_list)

@app.route('/purchaselog')
def purchaselog():
    purchase_log_list = db.get_purchase_log()
    return render_template("purchaselog.html", page="Purchase Log",purchase_log_list=purchase_log_list)

@app.route('/order_input')
def orderinput():
    return render_template("orderinput.html", page="Order input")

@app.route('/receipt')
def receipt():
    pagecontent = 'Receipt page'
    return render_template("receipt.html", page="Receipt")

@app.route('/deliveryconfirmation')
def deliveryconfirmation():
    pagecontent = 'Delivery confirmation page'
    return render_template("deliveryconfirmation.html", page="Receipt")
