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


    data = load_data()
    return render_template("customer.html", customer_list=data["customer"])


@app.route('/car', methods=['POST', 'GET'])
def car():
    if request.method == "POST":
        plate_no = request.form["plate_no"]
        brand = request.form["brand"]
        model = request.form["model"]
        customer_id = request.form["customer_id"]

        new_car = {
            "plate_number": plate_no,
            "brand": brand,
            "model": model,
            "customer id": customer_id
        }
        
        data = load_data()
        data["car"].append(new_car)
        save(data)

    data = load_data()
    return render_template("car.html", car_list=data["car"])

@app.route('/parking_area', methods=['POST', 'GET'])
def parking_area():
    if request.method == "POST":
        location = request.form["location"]
        parking_area = ParkingArea(location)

        new_parking_area = {
            "id": parking_area.parking_area_id,
            "number of slots": parking_area.number_of_slots,
            "location": parking_area.location
        }
        data = load_data()
        data["parking_area"].append(new_parking_area)
        save(data)

    data = load_data()
    return render_template("parkingArea.html", parking_area_list=data["parking_area"])

@app.route('/section', methods = ['POST', 'GET'])
def section():

    if request.method == "POST":
        area_id = request.form["parking area id"]
        status = request.form["status"]
        type = request.form["type"]

        part = Section(area_id, status, type)

        new_section = {
            "id":part.get_section_id(),
            "parking_area":part.parking_area,
            "status":part.status,
            "type":part.type,
            "capacity":part.capacity
        }

        data = load_data()
        data["sections"].append(new_section)
        save(data)

    data = load_data()
    return render_template("section.html", section_list=data["sections"])

@app.route('/slot', methods = ['POST', 'GET'])
def slot():

    if request.method == "POST":
        status = request.form["status"]
        section_id = request.form["section id"]

        bay = Slot(status, section_id)

        new_slot = {
            "id":bay.get_slot_id(),
            "status":bay.status,
            "section id":bay.section
        }

        data = load_data()
        data["slots"].append(new_slot)
        save(data)

        return redirect(url_for('slot'))

    data = load_data()
    return render_template("slot.html", slot_list=data["slots"])

@app.route('/parkingCard', methods = ['POST', 'GET'])
def parking_card():

    if request.method == "POST":
        issue_date = request.form["issue date"]
        expiry_date = request.form["expiry date"]
        car_plate = request.form["car plate number"]
        customer_id = request.form["customer id"]

        pass_card = ParkingCard(issue_date, expiry_date, car_plate, customer_id)

        new_card = {
            "id":pass_card.get_card_id(),
            "car":pass_card.car,
            "customer_id":pass_card.customer,
            "issue_date":pass_card.issue_date,
            "expiry_date":pass_card.expiry_date
        }

        data = load_data()
        data["card"].append(new_card)
        save(data)

    data = load_data()
    return render_template("parkingCard.html", card_list=data["card"])

@app.route('/parking', methods = ['POST', 'GET'])
def parking():

    if request.method == "POST":
        entry_time = int(request.form["entry time"])
        exit_time = int(request.form["exit time"])
        date = request.form["date"]
        car_plate = request.form["car plate number"]
        slot_id = request.form["slot id"]
        card_id = request.form["card id"]
        section_id = request.form["section id"]
        area_id = request.form["parking area id"]

        ticket = Parking(entry_time, exit_time, date, car_plate, slot_id, card_id, section_id, area_id)

        new_parking = {
            "id":ticket.get_parking_id(),
            "entry_time":ticket.entry_time,
            "exit_time":ticket.exit_time,
            "car":ticket.car,
            "slot_id":ticket.slot,
            "card":ticket.card,
            "section":ticket.section,
            "hours_parked":ticket.get_hours_parked(),
            "date":ticket.date,
            "parking_area":ticket.parking_area
        }

        data = load_data()
        data["parking"].append(new_parking)
        save(data)

    data = load_data()
    return render_template("parking.html", parking_list=data["parking"])

@app.route('/payment', methods = ['POST', 'GET'])
def payment():

    if request.method == "POST":
        date = request.form["date"]
        method = request.form["method"]
        parking_id = request.form["parking id"]

        if method.lower() == "cash":
            amount_tendered = int(request.form["amount tendered"] or 0)
            
            pay = CashPayment(date, method, parking_id, amount_tendered)

            new_payment = {
                "id":pay.payment_id,
                "date":pay.date,
                "method":pay.method,
                "parking":pay.parking,
                "status":pay.status,
                "amount_tendered":pay.amount_tendered
            }
        else:
            network = request.form["network"]
            phone_number = request.form["phone number"]
            transaction_id = request.form["transaction id"]

            pay = MobileMoneyPayment(date, method, parking_id, network, phone_number, transaction_id)

            new_payment = {
                "id":pay.payment_id,
                "date":pay.date,
                "method":pay.method,
                "parking":pay.parking,
                "status":pay.status,
                "network":pay.network,
                "phone_number":pay.phone_number,
                "transaction_id":pay.transaction_id
            }

        data = load_data()
        data["payment"].append(new_payment)
        save(data)

    data = load_data()
    return render_template("payment.html", payment_list=data["payment"])


if __name__ == "__main__":
    app.run(debug=True)