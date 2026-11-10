from flask import Flask, render_template, request, redirect, url_for
from parking import Car, ParkingArea, Customer, Parking, Slot, Section, Payment, ParkingCard,CashPayment,MobileMoneyPayment
import json

app = Flask(__name__)

def load_data():
    with open("data.json", 'r')as f:
        data = json.load(f)

    return data

def save(data):
    with open("data.json", 'w')as f:
        json.dump(data, f, indent=4)
    


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/customer', methods = ['POST', 'GET'])
def customer():

    if request.method == "POST":
        first_name = request.form["first name"]
        last_name = request.form["last name"]
        contact = request.form["contact"]

        customer = Customer(first_name, last_name, contact)
        id = customer.get_customer_id()

        new_customer = {
            "id":id,
            "first_name":first_name,
            "last_name":last_name,
            "contact": contact
        }

        data = load_data()
        data["customer"].append(new_customer)
        save(data)

        return redirect(url_for('customer'))

    data = load_data()
    return render_template("customer.html", customer_list=data["customer"])


@app.route('/car', methods = ['POST', 'GET'])
def car():

    if request.method == "POST":
        car_plate_no = request.form["car plate number"]
        brand = request.form["car brand"]
        model = request.form["model"]

        car = Car(car_plate_no,brand,model,customer)

        new_car = {
            "car_plate_no":car_plate_no,
            "brand":brand,
            "model":model,
            "customer": customer.get_customer_id()
        }

        data = load_data()
        data["car"].append(new_car)
        save(data)

        return redirect(url_for('car'))

    data = load_data()
    return render_template("car.html", cars=data["car"])

if __name__ == "__main__":
    app.run(debug=True)