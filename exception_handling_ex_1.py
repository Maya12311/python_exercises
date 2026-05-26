class Mechanic:

    def __init__(self, mechanic_id, specialization, vehicle_count):
        self.__mechanic_id = mechanic_id
        self.__specialization = specialization
        self.__vehicle_count = vehicle_count

    def get_mechanic_id(self):
        return self.__mechanic_id
    
    def get_specialization(self):
        return self.__specialization
    
    def get_vehicle_count(self):
        return self.__vehicle_count
    
    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count

class InvalidMechanicIdExcepton(Exception):
    def __init__(self, id ):
        msg = f"the given id {id} is invalid"
        super().__init__(msg)

class InvalidMechanicSpecializationException(Exception):
    def __init__(self, specialization):
        msg = f"the specialization {specialization} is not correct"
        super().__init__(msg)


class VehicleService:
    def __init__(self, mechanic_list):
        self.mechanic_list= mechanic_list

    def assign_vehicle_for_service(self, mechanic_id, vehicle_type):
        
        mechanic_id_is_present = False
        for mech in self.mechanic_list.values():
            if mechanic_id == mech.get_mechanic_id():
                mechanic_id_is_present = True
                if mech.get_spezialization() != vehicle_type:
                    raise InvalidMechanicSpecializationException(mech.get_spezialization())
                mech.set_vehicle_count(mech.get_vehicle_count() + 1)
                break

        
        if not mechanic_id_is_present:
            raise InvalidMechanicIdExcepton(mechanic_id)

       
      
        
        
        

mechanic1 = Mechanic(101, "TW", 1)
mechanic2 = Mechanic(102, "FW", 0)
mechanic3 = Mechanic(103, "TW", 4)
mechanic4 = Mechanic(104, "FW", 2)
mechanic5 = Mechanic(105, "FW", 1)

mechanics = {"mechanic_1" : mechanic1, "mechanic_2": mechanic2,"mechanic_3": mechanic3,"mechanic_4": mechanic4,"mechanic_5" : mechanic5}

vehicle_service_1 = VehicleService(mechanics)

try:
    mechanic_id = 101
    vehicle_service_1.assign_vehicle_for_service(mechanic_id, "TW")
    print(f"the validations have been successfull and the vehicle count has been raised for mechanic with id {id}")
except InvalidMechanicIdExcepton as e:
    print(str(e))

except InvalidMechanicSpecializationException as e:
    print(str(e))

except Exception as e:
    print(str(e))
