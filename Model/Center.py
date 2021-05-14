from datetime import datetime
from typing import List, AnyStr

class Slot:
    def __init__(self, slot: AnyStr) -> None:
        try:
            start, end = slot.split('-')
            self.start = datetime.time(datetime.strptime(start, f"%H:%M%p"))
            self.end = datetime.time(datetime.strptime(end , f"%H:%M%p"))
        except ValueError as e:
            self.start = None
            self.end = None
            print(f"Error In Slot : {e}")


class Session:
    def __init__(self,session_id:AnyStr, date:AnyStr, available_capacity:int,min_age_limit:int, vaccine:str, slots) -> None:
        self.session_id = session_id
        self.available_capacity = available_capacity
        self.min_age_limit  = min_age_limit
        self.vaccine = vaccine
        self.slots = [Slot(s) for s in slots]
        try:
            self.date = datetime.date(datetime.strptime(date, f"%d-%m-%Y"))
        except ValueError as e:
            print(f"Error while getting session Date {e}")
        
    

    
class Center:
    
    def __init__(self, center_id:AnyStr, name:AnyStr, address:AnyStr, state_name:AnyStr, district_name:AnyStr, block_name:AnyStr, pincode:int, lat:int, long:int, from_:AnyStr, to:AnyStr , fee_type:AnyStr, sessions:List[Session] ) -> None:
        self.center_id = center_id
        self.name = name
        self.address = address
        self.state_name = state_name
        self.district_name = district_name
        self.block_name = block_name
        self.pincode = pincode
        self.lat = lat
        self.long = long
        self.fee_type = fee_type
        self.sessions = [Session(**s) for s in sessions]
        try:
            self.from_ = datetime.time(datetime.strptime(from_, "%H:%M:%S"))
            self.to = datetime.time(datetime.strptime(to, "%H:%M:%S"))
        except ValueError as e:
            print(f"Error in center time {e}")
    
    def get_availablity(self, age):
        for session in self.sessions:
            if session.min_age_limit <= age and session.available_capacity > 0:
                return True
        else:
            return False


    def from_json(j_data):
        j_data['from_'] = j_data['from']
        del j_data['from']
        return Center(**j_data)

    



if __name__ == "__main__":
    # d = "09:00AM-11:00AM"
    # slot = Slot(d)
    # print(slot.start, slot.end)

    # d = "13-05 2021"
    # session = Session("293sj", d, 0, 18, "COVIDSHIELD", None )
    # print(session.date)

    # f = "09:00:00"
    # t = "18:00:00"
    # center = Center("kjkj", "Thawe PHC", "RHC Campus Thawe", "Bihar", "Gopalganj", 
    # "Thawe", 841440, 26, 84, f, t, "Free", None)
    # print(center.from_, center.to)
    j_data = {'centers': [{'center_id': 520128, 'name': 'THAWE PHC', 'address': 'RCH Campus Thawe PHC Thawe PHC', 'state_name': 'Bihar', 'district_name': 'Gopalganj', 'block_name': 'Thawe', 'pincode': 841440, 'lat': 26, 'long': 84, 'from': '09:00:00', 'to': '18:00:00', 'fee_type': 'Free', 'sessions': [{'session_id': 'e622514c-d4f9-4ad3-82fb-54b5d099e157', 'date': '13-05-2021', 'available_capacity': 0, 'min_age_limit': 18, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'session_id': '5fc79035-5837-4e92-a9e6-1907437d0421', 'date': '13-05-2021', 'available_capacity': 11, 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}, {'session_id': '4258b4ca-9858-437c-8156-b8c52043971d', 'date': '14-05-2021', 'available_capacity': 0, 'min_age_limit': 18, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}]}]}
    center  = Center.from_json(j_data['centers'][0])
    print(center.get_availablity(44))