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
    def __init__(self,session_id:AnyStr, date:AnyStr, available_capacity:int,min_age_limit:int, vaccine:str, slots:List[Slot]) -> None:
        self.session_id = session_id
        self.available_capacity = available_capacity
        self.min_age_limit  = min_age_limit
        self.vaccine = vaccine
        self.slots = slots
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
        self.sessions = sessions
        try:
            self.from_ = datetime.time(datetime.strptime(from_, "%H:%M:%S"))
            self.to = datetime.time(datetime.strptime(to, "%H:%M:%S"))
        except ValueError as e:
            print(f"Error in center time {e}")

if __name__ == "__main__":
    # d = "09:00AM-11:00AM"
    # slot = Slot(d)
    # print(slot.start, slot.end)

    # d = "13-05 2021"
    # session = Session("293sj", d, 0, 18, "COVIDSHIELD", None )
    # print(session.date)

    f = "09:00:00"
    t = "18:00:00"
    center = Center("kjkj", "Thawe PHC", "RHC Campus Thawe", "Bihar", "Gopalganj", 
    "Thawe", 841440, 26, 84, f, t, "Free", None)
    print(center.from_, center.to)