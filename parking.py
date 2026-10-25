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
        return self.parking_area_id

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
            #loading the json
        with open("data.json", 'r') as f:
            data = json.load(f)    

        new_parking_area = {
            "id": self.__parking_area_id,
            "number of slots": self.number_of_slots,
            "location": self.location
        }
        data["parking_area"].append(new_parking_area)

        #saving to the json
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)

    def available_slots(self):
        pass

    def occupied_slots(self):
        pass
    
class Section:
    def __init__(self, parking_area_id):
        self.__section_id = self.auto_id()
        self.parking_area_id = parking_area_id
        self.capacity = 50

    def get_section_id(self):
        return self.__section_id

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
            # Loading the json
        with open("data.json", 'r') as f:
            data = json.load(f)    

        new_section = {
            "id": self.auto_id(),
            "parking_area_id": self.parking_area_id
        }
        data["sections"].append(new_section)

        # Saving to the json
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)

    def get_available_slots(self):
        return self.__available_slots

    def get_occupied_slots(self):
        return self.__occupied_slots    

class Ordinary(Section):
    def __init__(self, section_id, parking_area_id, available_slots, occupied_slots, name = "Ordinary", capacity = 25, rate_per_hour = 5000):
        super().__init__(section_id, parking_area_id)

        self.__available_slots = available_slots
        self.__occupied_slots = occupied_slots
        self.name = name
        self.capacity = capacity
        self.rate_per_hour = rate_per_hour

        def get_available_slots(self):
            return self.__available_slots
        
        def get_occupied_slots(self):
            return self.__occupied_slots

class VIP(Section):
    def __init__(self, section_id, parking_area_id, available_slots, occupied_slots, name = "VIP", capacity = 25, rate_per_hour = 10000):
        super().__init__(section_id, parking_area_id)

        self.__available_slots = available_slots
        self.__occupied_slots = occupied_slots
        self.name = name
        self.capacity = capacity
        self.rate_per_hour = rate_per_hour

    def get_available_slots(self):
            return self.__available_slots
    
    def get_occupied_slots(self):
        return self.__occupied_slots


class Slot:
    def __init__(self, status, section_id):
        self.__slot_id = self.auto_id()
        self.status = status
        self.section_id = section_id

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
            "section_id":self.section_id
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
    def __init__(self, plate_no, brand, model):
        self.__plate_no = plate_no
        self.brand = brand
        self.model = model
    
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
            "plate_number":self.plate_number,
            "brand":self.brand,
            "model":self.model,
        }
        data["car"].append(new_vehicle)
    
        #saving to the json
        with open("data.json", 'w')as f:
            json.dump(data, f, indent = 4)
    

class Customer:
    def __init__(self, first_name, last_name):
        self.__customer_id = self.auto_id()
        self.first_name = first_name
        self.last_name = last_name

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
            "last_name":self.last_name
        }
        data["customer"].append(new_customer)

        #saving to the json
        with open("data.json", 'w')as f:
            json.dump(data, f, indent = 4)

        
class Parking:
    def __init__(self, entry_time, exit_time, parking_fee, date, slot_id, card_id):
        self.__parking_id = self.auto_id()
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.parking_fee = parking_fee
        self.__hours_parked = 0
        self.date = date
        self.slot_id = slot_id
        self.card_id = card_id

    def get_parking_id(self):
        return self.__parking_id

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

    def display_parking(self):
        pass

class ParkingCard:
    def __init__(self, customer_id, issue_date, expiry_date, plate_no):
        self.__card_id = self.auto_id()
        self.customer_id = customer_id
        self.__card_validity = False 
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.plate_no = plate_no

    def get_card_id(self):
        return self.__card_id 

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
            "customer_id": self.customer_id,
            "issue_date": self.issue_date,
            "expiry_date": self.expiry_date,
            "plate_no":self.plate_no
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
    def __init__(self, status, date, hours, section, parking_id):
        self.payment_id = self.auto_id()
        self.status = status
        self.date = date
        self.__amount = 0
        self.hours = hours
        self.section = section
        self.parking_id = parking_id

    @property
    def amount(self):
        return self.__amount

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
            "parking_id": self.parking_id
        }
        data["payment"].append(new_payment)

        #saving json file
        with open("data.json", 'w') as f:
            json.dump(data, f, indent = 4)       
    
    def calculate_amount(self):
        pass
 
t1 = ParkingArea(30, "center")
print(t1)