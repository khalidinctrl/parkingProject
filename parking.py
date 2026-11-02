import json

class ParkingArea:
    def __init__ (self, number_of_slots, location):
        self.__parking_area_id = self.auto_id()
        self.number_of_slots = number_of_slots
        self.location = location

    def __str__(self):
        return f"number_of_slots ==> {self.number_of_slots}\n location ==> {self.location}\n id ==> {self.__parking_area_id}"
    
    @property
    def parking_area_id(self):
        return self.__parking_area_id

    def auto_id(self):
        label = "PA"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("parking_area", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
        with open("data.json", 'r') as f:
            data = json.load(f)    

        new_parking_area = {
            "id": self.__parking_area_id,
            "number of slots": self.number_of_slots,
            "location": self.location
        }
        data["parking_area"].append(new_parking_area)

        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)    

class Section:
    def __init__(self, parking_area, status, type):
        self.__section_id = self.auto_id()
        self.parking_area = parking_area
        self.status = status
        self.type = type
        self.capacity = 50

    def check_available_slots(self):
        pass

    def get_section_id(self):
        return self.__section_id

    def check_rate(self):
        vip = 10000
        ordinary = 5000
        if self.type == "vip":
            return vip
        elif self.type == "ordinary":
            return ordinary
        else:
            return "section is vip / ordinary"
    
    def auto_id(self):
        label = "S"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("sections", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
        with open("data.json", 'r') as f:
            data = json.load(f)    

        new_section = {
            "id": self.__section_id,
            "parking_area": self.parking_area_id,
            "status": self.status,
            "type": self.type,
            "capacity": self.capacity
        }
        data["sections"].append(new_section)

        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)
            

class Slot:
    def __init__(self, status, section, parking_area, car):
        self.__slot_id = self.auto_id()
        self.status = status
        self.section = section
        self.parking_area = parking_area
        self.car = car

    def auto_id(self):
        label = "SL"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("slots", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
        #loading the json
        with open("data.json", 'r')as f:
            data = json.load(f)    
    
        new_slot = {
            "id":self.__slot_id,
            "status":self.status,
            "section_id":self.section
        }
        data["slots"].append(new_slot)
    
        #saving to the json
        with open("data.json", 'w')as f:
            json.dump(data, f, indent = 4)

    def get_slot_id(self):
        return self.__slot_id

    def search_slot(self):
        pass

    def update_status(self):
        pass

class Car:
    def __init__(self, plate_no, brand, model, customer):
        self.__plate_no = plate_no
        self.brand = brand
        self.model = model
        self.customer = customer
    
#getter for plate number
    def get_plate_no(self):
        return self.__plate_no

    def __str__ (self):
        return f"plate_no ==> {self.get_plate_no()} brand ==>{self.brand} model ==>{self.model}"

    def save(self):
        #loading the json
        with open("data.json", 'r')as f:
            data = json.load(f)    
    
        new_vehicle = {
            "plate_number":self.__plate_no,
            "brand":self.brand,
            "model":self.model,
        }
        data["car"].append(new_vehicle)
    
        #saving to the json
        with open("data.json", 'w')as f:
            json.dump(data, f, indent = 4)
    

class Customer:
    def __init__(self, first_name, last_name, contact):
        self.__customer_id = self.auto_id()
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact

    def auto_id(self):
        label = "CU"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("customer", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None
    
    def get_customer_id(self):
        return self.__customer_id

    def save(self):
        #loading the json
        with open("data.json", 'r')as f:
            data = json.load(f)    

        new_customer = {
            "id":self.__customer_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "contact": self.contact
        }
        data["customer"].append(new_customer)

        #saving to the json
        with open("data.json", 'w')as f:
            json.dump(data, f, indent = 4)

        
class Parking:
    def __init__(self, entry_time, exit_time, date, car, slot, card, section, parking_area):
        self.__parking_id = self.auto_id()
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.date = date
        self.car = car
        self.slot = slot
        self.card = card
        self.section = section
        self.parking_area = parking_area
        self.__hours_parked = 0


    def get_parking_id(self):
        return self.__parking_id

    def __str__(self):
        return f"{'*'*20}\n\t TICKET \n parking area ==> {self.parking_area.location} \n section ==> \n entry time ==> {self.entry_time} \n exit time ==> {self.exit_time} \n car ==> {self.car.plate_no, self.car.brand, self.car.model} \n slot ==> {self.slot.slot_id} hours parked ==> {self.__hours}"

    def auto_id(self):
        label = "PK"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("parking", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
            #Loadin json file
        with open("data.json", 'r') as f:
            data = json.load(f)

        new_parking = {
            "id":self.__parking_id,
            "entry_time":self.entry_time, 
            "exit_time": self.exit_time,
            "parking_fee": self.parking_fee,
            "hours_parked": self.calculate_hours(),
            "date": self.date,
            "slot_id": self.slot_id
        }
        data["parking"].append(new_parking)

        #saving to json
        with open("data.json", 'w') as f:
            json.dump(data, f, indent = 4)
       
    def calculate_hours(self):
        self.__hours = self.exit_time - self.entry_time
        return self.__hours

class ParkingCard:
    def __init__(self, issue_date, expiry_date, car, customer):
        self.__card_id = self.auto_id()
        self.customer = customer
        self.__card_validity = False 
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.car = car

    def get_card_id(self):
        return self.__card_id 
    
#REMEMBER TO MASK THE CARD NUMBER IN A LONG AND CARDY WAY LIKE 5376-37478-3892
    def auto_id(self):
        label = "CD"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("card", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
            #Loading the json
        with open("data.json", 'r') as f:
            data = json.load(f)

        new_parking_card = {
            "id": self.__card_id,
            "customer_id": self.customer,
            "issue_date": self.issue_date,
            "expiry_date": self.expiry_date,
            "plate_no":self.car
        }
        data["card"].append(new_parking_card)

        #saving to json
        with open("data.json", 'w' ) as f:
            json.dump(data, f, indent = 4)

    def get_card_validity(self):
        return self.__card_validity       

    def renew_card(self):
        pass

class Payment:
    def __init__(self, date, section, parking_area, parking):
        self.payment_id = self.auto_id()
        self.date = date
        self.parking = parking
        self.section = section
        self.parking_area = parking_area
        self.status = "pending"
        self._amount = 0

    @property
    def amount(self):
        return self._amount

    def auto_id(self):
        label = "PY"

        with open("data.json", 'r') as f:
            data = json.load(f)

        for i in range(1, 1000):
            gen_ID = f"{label}-{i:04d}"
            
            found = False
            for item in data.get("payment", []):
                if item.get("id") == gen_ID:
                    found = True
                    break
            
            if not found:
                return gen_ID
                
        return None

    def save(self):
    #Loading json file
        with open("data.json", 'r') as f:
            data = json.load(f)

        new_payment = {
            "id": self.payment_id,
            "status": self.status,
            "date": self.date,
            "amount": 0,
            "hours": self.hours,
            "section": self.section,
            "parking_id": self.parking_area.parking_area_id
        }
        data["payment"].append(new_payment)

        #saving json file
        with open("data.json", 'w') as f:
            json.dump(data, f, indent = 4)       
    
    def calculate_amount(self,):
        self._amount = self.section.rate * self.__hours

class CashPayment(Payment):
    def __init__(self, date, hours, section, parking_area, parking, amount_tendered):
        super().__init__(date, hours, section, parking_area, parking)
        self.amount_tendered = amount_tendered
        self.__balance = 0
        self.section = section

    def calculate_balance(self):
        self.__balance = self.amount_tendered - self._amount
        return self.__balance

    def validate_payment(self):
        valid  = False

        self.calculate_amount()
        if self.amount_tendered >= self._amount:
            self.__balance = self.amount_tendered - self._amount
            self.status = "paid"
            valid = True
        else:
            self.status = "Insufficient cash"
            return valid

    def display_payment(self):
        print(f"Cash payment of {self.amount}\n Change: {self.__balance}")


class MobileMoneyPayment(Payment):
    def __init__(self, date, section, parking_area, parking, phone_number, network):
        super().__init__(date, section, parking_area, parking)
        self.phone_number = phone_number
        self.network = network

    def receipt_link(self):
        return f"https{self.network}{self.payment_id}"

    def display_payment(self):
        print(f"payment ==> {self.payment_id}\n network ==> {self.network}\n phone number ==> {self.phone_number}")


    def validate_payment(self):
        valid  = False
        
        if self.phone_number.startswith('0') and len(self.phone_number) == 10:
            body = self.phone_number[1:]
            self.phone_number = f"+256 {body[0:3]} {body[3:6]} {body[6:]}"
            valid = True
            return valid
            
        return valid
        

m1 = MobileMoneyPayment("2000-1-1",6,"sec","p1","0700111222","airtel")
m1.display_payment()
print(m1.validate_payment())

