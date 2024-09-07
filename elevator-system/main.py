class Elevator:
    """Elevator class"""

    def __init__(self, id, direction):
        self.id = id
        self.current_floor = 1
        self.direction = direction
        self.destinations = set()
    


    def add_destination(self, destination):
        self.destinations.add(destination)
        return self.destinations
    
    def remove_destination(self, destination):
        self.destinations.remove(destination)
        return self.destinations
    
    def move(self):
        if self.is_idle():
            return
        if self.direction == "up":
            self.current_floor = min(self.destinations)
        else:
            self.current_floor = max(self.destinations)
        
        self.destinations.remove(self.current_floor)
        self.update_direction()
    

    def is_idle(self):
        return len(self.destinations) == 0


    def can_accept_request(self, requested_floor, requested_direction):
        if self.is_idle():
            return True
        
        if self.direction == "up" and requested_direction == "up":
            return requested_floor >= self.current_floor
        
        if self.direction == "down" and requested_direction == "down":
            return requested_floor <= self.current_floor
        
        return False
    
    def update_direction(self):
        if self.destinations:
            if min(self.destinations) < self.current_floor:
                self.direction = "down"
            elif max(self.destinations) > self.current_floor:
                self.direction = "up"
        else:
            self.direction = ""
    
    def get_current_floor(self):
        return self.current_floor
    
    def get_direction(self):
        return self.direction
    
    def get_destinations(self):
        return self.destinations
    
    def get_next_destination(self):
        if self.direction == "up":
            return min(self.destinations)
        else:
            return max(self.destinations)
    
    def get_highest_destination(self):
        if not self.destinations:
            return self.current_floor
        return max(self.destinations)
    
    def get_lowest_destination(self):
        if not self.destinations:
            return self.current_floor
        return min(self.destinations)



class ElevatorSystem:
    """ElevatorSystem class"""

    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators
        self.elevators = [Elevator(i, "") for i in range(num_elevators)]
    
    def request_elevator(self, requested_floor, requested_direction):
        best_elevator = self.find_best_elevator(requested_floor, requested_direction)
        best_elevator.add_destination(requested_floor)
        best_elevator.direction = requested_direction
        return best_elevator
    
    def find_best_elevator(self, requested_floor, requested_direction):

        suitable_elevators = []
        best_elevator = None
        best_score = float("inf")
        best_distance = float("inf")

        for elevator in self.elevators:
            if elevator.can_accept_request(requested_floor, requested_direction):
                suitable_elevators.append(elevator)
            

        if not suitable_elevators:
            return min(self.elevators, key=lambda x: abs(x.get_current_floor() - requested_floor))


        for elevator in suitable_elevators:

            direction_score = 0 if elevator.get_direction() == requested_direction else 1
            distance_score = abs(elevator.get_current_floor() - requested_floor)

            if (best_score, best_distance) > (direction_score, distance_score):
                best_score = direction_score
                best_distance = distance_score
                best_elevator = elevator

        return best_elevator

    def step(self):
        for elevator in self.elevators:
            if not elevator.is_idle():
                elevator.move()
    
    def get_elevators(self):
        return self.elevators


    def print_status(self):
        for elevator in self.elevators:
            print(f"Elevator {elevator.id}: Floor {elevator.current_floor}, "
                  f"Direction: {elevator.direction}, "
                  f"Highest: {elevator.get_highest_destination()}, "
                  f"Lowest: {elevator.get_lowest_destination()}")
        print("---")


if __name__ == "__main__":
    elevator_system = ElevatorSystem(10, 2)
    elevator_system.print_status()

    elevator_system.request_elevator(5, "up")
    elevator_system.print_status()
    elevator_system.request_elevator(3, "down")
    elevator_system.print_status()
    elevator_system.request_elevator(7, "up")
    elevator_system.print_status()