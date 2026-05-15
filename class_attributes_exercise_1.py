class Classroom:
    classroom_list = ["Schweiz", "Australien", "Pakistan"]

    


    @classmethod
    def search_classroom(cls, class_room):
        for room in cls.classroom_list:
            if room.lower() == class_room.lower():
                return "Found"
        
        return -1
        
    
#c1 = Classroom()
is_room_in_west = Classroom.search_classroom("Pakistan")
print("Search room in west ", is_room_in_west)