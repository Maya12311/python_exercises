class Ticket:
   
    
    counter = 0

    def __init__(self, passenger_name, source, destination):
         self.passenger_name = passenger_name
         self.source = source
         self.destination = destination
         self.ticket_id = None
         self.generate_ticket()

    
    def validate_source_destination(self):
        
        source = self.get_source().lower()
        destination = self.get_destination().lower()

        if source == "delhi" and destination in ["mumbai", "chennai", "pune", "kolkata" ]:
            return True
         
        return False
         
    
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            first_letter_source = self.get_source()[0].upper()
            first_letter_destination = self.get_destination()[0].upper()
            self.ticket_id = first_letter_source + first_letter_destination + str(Ticket.counter)
            return self.ticket_id
        self.ticket_id = None

         
    
    def get_ticket_id(self):
        return self.ticket_id
    
    def get_passenger_name(self):
        return self.passenger_name
    
    def get_source(self):
        return self.source
    
    def get_destination(self):
        return self.destination


ticket1 = Ticket("John", "Delhi", "Mumbai")
print(ticket1.get_ticket_id())   # DM01

ticket2 = Ticket("Amy", "delhi", "pune")
print(ticket2.get_ticket_id())   # DP02

ticket3 = Ticket("Tom", "Mumbai", "Delhi")
print(ticket3.get_ticket_id())   # None