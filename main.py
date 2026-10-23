from parking import Car, ParkingArea, Customer, Parking, Slot, Section, Payment, ParkingCard,Ordinary,VIP
import json

#generating auto ID
def auto_id(label):
    IDS = {
        'PA': "parking_area",
        'CD': "card",
        'CU': "customer",
        'S': "sections",
        'SL': "slots",
        'PK': "parking",
        'PY': "payment"
    }
    
    target_id = IDS.get(label)

    for i in range(1, 1000):
        gen_ID = f"{label}-{i:04d}"

        with open("data.json", 'r') as f:
            data = json.load(f)

        found = False
        
        for item in data.get(target_id, []):
            if item.get("id") == gen_ID:
                found = True
                break
        
        if not found:
            return gen_ID

    return None

#function handling the parking section
def parking_area_details():
    label = 'PA'
    print("\tEntering parking area details.....")

    parking_area_id = auto_id(label)
    number_of_slots = input("Enter number_of_slots: ")
    location = input("Enter location: ")

    parking_area = ParkingArea(parking_area_id, number_of_slots, location)

    #loading the json
    with open("data.json", 'r') as f:
        data = json.load(f)    

    new_parking_area = {
        "id": parking_area_id,
        "number of slots": number_of_slots,
        "location": location
    }
    data["parking_area"].append(new_parking_area)

    #saving to the json
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)
        


#captures car details
def car_details():
    data = []
    plate_number = input("Enter plate number: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")

    vehicle = Car(plate_number, brand, model)

    #loading the json
    with open("data.json", 'r')as f:
        data = json.load(f)    

    new_vehicle = {
        "plate_number":plate_number,
        "brand":brand,
        "model":model,
    }
    data["car"].append(new_vehicle)

    #saving to the json
    with open("data.json", 'w')as f:
        json.dump(data, f, indent = 4)


#handling section details
def section_details():
    print("\tEntering section details.....")
    
    section_id = auto_id('S')
    parking_area_id = input("Enter parking area id: ")

    section = Section(section_id, parking_area_id)

    # Loading the json
    with open("data.json", 'r') as f:
        data = json.load(f)    

    new_section = {
        "id": section_id,
        "parking_area_id": parking_area_id
    }
    data["sections"].append(new_section)

    # Saving to the json
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)
        
#handling slot details
def slot_details():
    label = 'SL'
    print("\tEntering slot details.....")
    data = []
    
    slot_id = auto_id('SL')
    status = input("Enter status: ")
    section_id = input("Enter section id: ")

    slot = Slot(slot_id, status, section_id)

    #loading the json
    with open("data.json", 'r')as f:
        data = json.load(f)    

    new_slot = {
        "id":slot_id,
        "status":status,
        "section_id":section_id
    }
    data["slots"].append(new_slot)

    #saving to the json
    with open("data.json", 'w')as f:
        json.dump(data, f, indent = 4)

#handling customer details
def customer_details():
    print("\tEntering customer details.....")
    data = []
    
    customer_id = auto_id('CU')
    first_name = input("Enter customer first_name: ")
    last_name = input("Enter customer last name: ")

    customer = Customer(customer_id, first_name, last_name)

    #loading the json
    with open("data.json", 'r')as f:
        data = json.load(f)    

    new_customer = {
        "id":customer_id,
        "first_name":first_name,
        "last_name":last_name
    }
    data["customer"].append(new_customer)

    #saving to the json
    with open("data.json", 'w')as f:
        json.dump(data, f, indent = 4)

# handling Parking card details
def card_details():
    print("\tEntering parking card details.....")
    data = []

    card_id = auto_id('CD')
    customer_id = input("Enter customer_id: ")     
    issue_date = input("Enter issue_date: ")
    expiry_date = input("Enter expiry_date: ")
    plate_no = input("Enter plate_no: ")

    parking_card = ParkingCard(card_id, customer_id, issue_date, expiry_date, plate_no)

    #Loading the json
    with open("data.json", 'r') as f:
        data = json.load(f)

    new_parking_card = {
        "id": card_id,
        "customer_id": customer_id,
        "issue_date": issue_date,
        "expiry_date": expiry_date,
        "plate_no":plate_no
    }
    data["card"].append(new_parking_card)

    #saving to json
    with open("data.json", 'w' ) as f:
        json.dump(data, f, indent = 4)

#Handling Parking Details
def parking():
    print("\tEntering Parking Details.....")
    data = []

    parking_id = auto_id('PK')
    entry_time = input("Enter entry_time: ")
    exit_time = input("Enter exit_time: ")
    parking_fee = input("Enter parking_fee: ")
    hours_parked = input("Enter hours_parked: ")
    date = input("Enter date: ")
    slot_id = input("Enter slot_id: ")
    card_id = input("Enter card id: ")


    parking = Parking(parking_id, entry_time, exit_time, parking_fee, hours_parked, date, slot_id, card_id)

    #Loadin json file
    with open("data.json", 'r') as f:
        data = json.load(f)

    new_parking = {
        "id":parking_id,
        "entry_time":entry_time, 
        "exit_time": exit_time,
        "parking_fee": parking_fee,
        "hours_parked": 0,
        "date": date,
        "slot_id": slot_id
    }
    data["parking"].append(new_parking)

    #saving to json
    with open("data.json", 'w') as f:
        json.dump(data, f, indent = 4)

#Handling Payment details
def payment_details():
    print("\tEntering Payment Details")
    data = []

    payment_id = auto_id('PY') 
    status = input("Enter status: ")
    date = input("Enter date: ")
    hours = input("Enter hours: ")
    section = input("Enter section: ")
    parking_id = auto_id('PY')

    payment = Payment(payment_id,status, date, hours, section, parking_id)

    #Loading json file
    with open("data.json", 'r') as f:
        data = json.load(f)

    new_payment = {
        "id": payment_id,
        "status": status,
        "date": date,
        "amount": 0,
        "hours": hours,
        "section": section,
        "parking_id": parking_id
    }
    data["payment"].append(new_payment)

    #saving json file
    with open("data.json", 'w') as f:
        json.dump(data, f, indent = 4)    

#the first to run
def main():
    print("Welcome....\n\t 1. Ordinary ==> 5000 \n\t 2. VIP ==> 10000")
    parking_type = input("enter parking type: ")
    if parking_type == '1':
        car_details()
    elif parking_type == '2':
        car_details()
    else:
        print("INVALID OPTION SELECT 1 / 2")


#testing
main()
parking_area_details()
section_details()
slot_details()
customer_details()
card_details()
parking()
payment_details()
