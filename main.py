from parking import Car, ParkingArea, Customer, Parking, Slot, Section, Payment, ParkingCard,CashPayment,MobileMoneyPayment
from datetime import datetime, date

def parking_system():
    print(f"{'='*4} PARKING MANAGEMENT SYSTEM {'='*5}")
    
    #Parking Area Details
    location = input("Enter parking area location: ")
    parking_area = ParkingArea(location)
    parking_area.save()

    #Section Details
    status = input("Enter section status (e.g., free/occupied): ")
    section_type = input("Enter section type (vip/ordinary): ")
    section = Section(parking_area, status, section_type)
    section.save()

    #Customer Details
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    contact = input("Enter customer contact (e.g., 0700111222): ")
    customer = Customer(first_name, last_name, contact)
    customer.save()

    #Car Details (Composes Customer)
    plate = input("Enter car plate number: ")
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    car = Car(plate, brand, model, customer)
    car.save()

    # 5. Slot Details (Composed with Area, Section, and Car)
    slot_status = input("Enter slot status: ")
    slot = Slot(slot_status, section)
    slot.save()
    print(f"Slot created with ID: {slot.get_slot_id()}")

    #Parking Card Details (Composes Car and Customer)
    issue_date = input("Enter card issue date (YYYY-MM-DD): ")
    expiry_date = input("Enter card expiry date (YYYY-MM-DD): ")
    card = ParkingCard(issue_date, expiry_date, car, customer)
    card.save()

    #Parking Ticket Details (Composes all previous objects)
    entry_time = int(input("Enter entry time (hour as integer): "))
    exit_time = int(input("Enter exit time (hour as integer): "))
    today  = date.today()
    ticket = Parking(entry_time, exit_time, today, car, slot, card, section, parking_area)
    ticket.save()
    
    #Display the ticket
    print("\n" + str(ticket))

    #Payment Details (Cash or Mobile Money)
    pay_choice = input("Select payment method (1. Cash / 2. Mobile Money): ")
    pay_date = date.today()

    if pay_choice == '1':
        amount_tendered = int(input("Enter amount tendered: "))
        payment = CashPayment(pay_date, section, parking_area, ticket, amount_tendered)
        payment.validate_payment()
        payment.save()
        payment.display_payment()

    elif pay_choice == '2':
        network = input("Enter mobile network (e.g., airtel / mtn): ")
        phone_number = input("Enter phone number: ")
        transaction_id = input("Enter transaction id")
        payment = MobileMoneyPayment(pay_date, pay_choice, ticket, network, phone_number, transaction_id)

        if payment.validate_payment():
            print("Phone number validated successfully!")
        else:
            print("Invalid phone format")
        payment.save()
        payment.display_payment()
    else:
        print("Invalid payment option selected.")


parking_system()