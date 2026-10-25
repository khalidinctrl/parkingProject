from parking import Car, ParkingArea, Customer, Parking, Slot, Section, Payment, ParkingCard,Ordinary,VIP

#function handling the parking section
def parking_area_details():
    print("\tEntering parking area details.....")

    number_of_slots = input("Enter number_of_slots: ")
    location = input("Enter location: ")

    parking_area = ParkingArea(number_of_slots, location)
    parking_area.save()
        
#captures car details
def car_details():
    data = []
    plate_number = input("Enter plate number: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")

    vehicle = Car(plate_number, brand, model)
    vehicle.save()

#handling section details
def section_details():
    print("\tEntering section details.....")
    
    parking_area_id = input("Enter parking area id: ")

    section = Section(parking_area_id)
    section.save()
        
#handling slot details
def slot_details():
    label = 'SL'
    print("\tEntering slot details.....")
    data = []
    
    status = input("Enter status: ")
    section_id = input("Enter section id: ")

    slot = Slot(status, section_id)
    slot.save()

#handling customer details
def customer_details():
    print("\tEntering customer details.....")
    data = []
    
    first_name = input("Enter customer first_name: ")
    last_name = input("Enter customer last name: ")

    customer = Customer(first_name, last_name)
    customer.save()

# handling Parking card details
def card_details():
    print("\tEntering parking card details.....")
    data = []

    customer_id = input("Enter customer_id: ")     
    issue_date = input("Enter issue_date: ")
    expiry_date = input("Enter expiry_date: ")
    plate_no = input("Enter plate_no: ")

    parking_card = ParkingCard(customer_id, issue_date, expiry_date, plate_no)
    parking_card.save()

#Handling Parking Details
def parking():
    print("\tEntering Parking Details.....")
    data = []

    entry_time = int(input("Enter entry_time: "))
    exit_time = int(input("Enter exit_time: "))
    parking_fee = input("Enter parking_fee: ")
    date = int(input("Enter date: "))
    slot_id = input("Enter slot_id: ")
    card_id = input("Enter card id: ")


    parking = Parking(entry_time, exit_time, parking_fee, date, slot_id, card_id)
    parking.save()

#Handling Payment details
def payment_details():
    print("\tEntering Payment Details")
    data = []

    status = input("Enter status: ")
    date = input("Enter date: ")
    hours = input("Enter hours: ")
    section = input("Enter section: ")

    payment = Payment(status, date, hours, section)

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


#calling the functions
main()
parking_area_details()
section_details()
slot_details()
customer_details()
card_details()
parking()
payment_details()
