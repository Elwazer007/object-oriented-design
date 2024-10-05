
class Key:
    def __init__(self, key_id):
        self.key_id = key_id

class Room:

    def __init__(self, room_number: str, room_type: str , location , price , availability, key):
        self._room_number = room_number
        self._room_type =room_type
        self._location = location
        self._price = price
        self._availability = availability
        self._key = key
        self._bookings = []

    
    def get_room_number(self):
        return self._room_number
    
    def get_room_type(self):
        return self._room_type
    

    def get_location(self):
        return self._location
    
    def get_price(self):
        return self._price
    
    def get_availability(self):
        return self._availability
    
    def get_key(self):
        return self._key
    
    def set_room_key(self, key):
        self._key = key
    
    def set_availability(self, availability):
        self._availability = availability
    
    def add_booking(self, booking):
        self._bookings.append(booking)
    
    def remove_booking(self, booking):
        self._bookings.remove(booking)
    
    def get_bookings(self):
        return self._bookings
    

class Account:
    def __init__(self, username , password):
        self._username = username
        self._password = password


class Booking:

    def __init__(self, booking_id, rooms, check_in_date, check_out_date, payment_method):
        self._booking_id = booking_id
        self._rooms = rooms
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._payment_method = payment_method
        self._status = "Pending"
        
    

    def _update_rooms_booking(self):
        for room in self._rooms:
            room.add_booking(self)
    
    def _remove_rooms_booking(self):
        for room in self._rooms:
            room.remove_booking(self)

    def get_booking_id(self):
        return self._booking_id
    
    def get_rooms(self):
        return self._rooms
    
    def get_check_in_date(self):
        return self._check_in_date
    
    def get_check_out_date(self):
        return self._check_out_date
    
    def get_payment_method(self):
        return self._payment_method
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method
    
    def set_check_in_date(self, check_in_date):
        self._check_in_date = check_in_date
    
    def set_check_out_date(self, check_out_date):
        self._check_out_date = check_out_date
    
    def set_room(self, rooms):
        self._rooms = rooms
    
    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def get_total_cost(self):
        total_cost = 0
        for room in self._rooms:
            total_cost += room.get_price()
        return total_cost
    
    def get_room_numbers(self):
        room_numbers = []
        for room in self._rooms:
            room_numbers.append(room.get_room_number())
        return room_numbers
    
    def get_room_types(self):
        room_types = []
        for room in self._rooms:
            room_types.append(room.get_room_type())
        return room_types
    
    def cancel_booking(self):
        self._status = "Cancelled"
        self._remove_rooms_booking()
    
    def complete_booking(self):
        self._status = "Completed"
        

class BookingManager:

    def __init__(self):
        self._bookings = []
    
    def _validate_booking_availability(self, rooms, check_in_date, check_out_date):
        for room in rooms:
            if room.get_availability() == False:
                return False
            
            for booking in room._get_bookings():
                if booking.get_check_in_date() < check_out_date and booking.get_check_out_date() > check_in_date:
                    return False
        return True
    
    def create_booking(self, rooms, check_in_date, check_out_date, payment_method):
        booking_id = len(self._bookings) + 1
        
        if self._validate_booking_availability(rooms, check_in_date, check_out_date):
            booking = Booking(booking_id, rooms, check_in_date, check_out_date, payment_method)
            self._bookings.append(booking)
            booking._update_rooms_booking()
            return booking
        else:
            return None

    def add_booking(self, booking):
        self._bookings.append(booking)
    
    def remove_booking(self, booking):
        self._bookings.remove(booking)
    
    def get_bookings(self):
        return self._bookings
    
    def get_booking_by_id(self, booking_id):
        for booking in self._bookings:
            if booking.get_booking_id() == booking_id:
                return booking
        return None
    
    def get_bookings_by_room_number(self, room_number):
        bookings = []
        for booking in self._bookings:
            for room in booking.get_rooms():
                if room.get_room_number() == room_number:
                    bookings.append(booking)
        return bookings
    
    def get_bookings_by_room_type(self, room_type):
        bookings = []
        for booking in self._bookings:
            for room in booking.get_rooms():
                if room.get_room_type() == room_type:
                    bookings.append(booking)
        return bookings
    
    def get_bookings_by_check_in_date(self, check_in_date):
        bookings = []
        for booking in self._bookings:
            if booking.get_check_in_date() == check_in_date:
                bookings.append(booking)
        return bookings
    
    def get_bookings_by_check_out_date(self, check_out_date):
        bookings = []
        for booking in self._bookings:
            if booking.get_check_out_date() == check_out_date:
                bookings.append(booking)
        return bookings
    
    def get_bookings_by_payment_method(self, payment_method):
        bookings = []
        for booking in self._bookings:
            if booking.get_payment_method() == payment_method:
                bookings.append(booking)
        return bookings
    
    def get_bookings_by_status(self, status):
        bookings = []
        for booking in self._bookings:
            if booking.get_status() == status:
                bookings.append(booking)
        return bookings
    
    def get_total_earnings(self):
        total_earnings = 0
        for booking in self._bookings:
            total_earnings += booking.get_total_cost()
        return total_earnings



class Guest:
    
    def __init__(self, name, phone_number, email, address):
        self._name = name
        self._phone_number = phone_number
        self._email = email
        self._address = address
        self.booking = None

    def create_booking(self , rooms , check_in_date , check_out_date, payment_method):
        booking = BookingManager.create_booking(rooms, check_in_date, check_out_date, payment_method)
        self.booking = booking
        return booking

    def check_in(self):
        for room in self.booking.get_rooms():
            room.set_availability(False)

    def check_out(self):
        for room in self.booking.get_rooms():
            room.set_availability(True)
        self.booking.complete_booking()
    
    def cancel_booking(self):
        self.booking.cancel_booking()
        self.booking = None