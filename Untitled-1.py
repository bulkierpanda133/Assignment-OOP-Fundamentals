#Task 1: Vehicle Registration System

# Vehicle class definition
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    # Method to update the vehicle owner
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")

# Create instances of the Vehicle class
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")

# Display the initial state of the vehicles
print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, {vehicle2.owner}")

# Update the owner of vehicle1
vehicle1.update_owner("Charlie")

# Update the owner of vehicle2
vehicle2.update_owner("Diana")

# Display the updated state of the vehicles
print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, {vehicle2.owner}")



#Task 2: Event Management System Enhancement

# Event class definition with participant tracking
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to zero

    # Method to add a participant
    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current participant count: {self.participant_count}")

    # Method to get the current participant count
    def get_participant_count(self):
        return self.participant_count

# Demonstration of the Event class with participant tracking
event = Event("Python Workshop", "2024-10-20")

# Display initial participant count
print(f"Initial participant count: {event.get_participant_count()}")

# Add participants
event.add_participant()
event.add_participant()
event.add_participant()

# Display final participant count
print(f"Final participant count: {event.get_participant_count()}")
