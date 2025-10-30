import time
import uuid
from csc_125_02_fa25.m_17_oct_28.car import Car

# LIFO => Last in first out
# FIFO => First in first out
class Garage:

    def __init__(self, parking_spaces:int, parking_fee_sec:int, max_parking_time_sec:int) -> None:
        self.__parking_spaces = parking_spaces
        self.__parking_fee_sec = parking_fee_sec
        self.__max_parking_time_sec = max_parking_time_sec
        self.__garage_dict:dict[str, dict] = {}
        self.__towed_cars_set: set[str] = set()

    def get_parking_fee(self):
        """
        Returns the parking rate dollars per second to park in the garage.
        """
        return self.__parking_fee_sec

    def get_max_parking_time(self):
        """
        Returns the maximum amount of time a car can be parked in the garage
        consecutively.
        """
        return self.__max_parking_time_sec

    def __clean_garage(self):
        current_time: float = time.time()

        # Extra memory
        # temp_garage_dict = {}

        for ticket, car_dict in self.__garage_dict.items():
            parked_at = car_dict["parked_at"]
            total_time_sec = current_time - parked_at
            if total_time_sec > self.get_max_parking_time():
                print(f"Towed: {car_dict['car']}")
                self.__towed_cars_set.add(ticket)
            # else:
            #     temp_garage_dict[ticket] = car_dict

        #self.__garage_dict = temp_garage_dict

        for towed_ticket in self.__towed_cars_set:
            self.__garage_dict.pop(towed_ticket)
        

    def park(self, car:Car) -> str | None:

        if len(self.__garage_dict) >= self.__parking_spaces:
            self.__clean_garage()

        if len(self.__garage_dict) < self.__parking_spaces:
            uid = uuid.uuid4()
            ticket: str = uid.hex[:8]
            # Total number of seconds since Dec 31 1970
            parked_at = time.time()

            # The valet ticket is the key to the car in the dictionary
            self.__garage_dict[ticket] = {
                "parked_at": parked_at,
                "car":car
            }

            return ticket
        else:
            # No room left in the garage we return nothing because nothing
            # was parked
            return None

    def retrieve(self, ticket:str) -> tuple[float |None, Car | None, str | None]:

        # Use the get method in the dict to get the car dict safely b/c the
        # ticket might not match to any car.
        car_dict = self.__garage_dict.get(ticket, None)

        # If the ticket matches car
        if car_dict:
            # Calculate the fee
            retrieve_at = time.time()
            parked_at = car_dict["parked_at"]
            total_time_sec = retrieve_at - parked_at

            # Mulitply the total time parked time the rate per second
            fee = total_time_sec * self.__parking_fee_sec
            
            # Get the car from the car dict
            car = car_dict["car"]
            return fee, car, "Have a nice day"
        elif ticket in self.__towed_cars_set:
            return 1000, None, "Your car was towed..."

        return None, None, "no car found"

    def __str__(self) -> str:

        utilization = round(len(self.__garage_dict)/self.__parking_spaces, 2)

        return f"Garage: {len(self.__garage_dict)} of {self.__parking_spaces} | {utilization*100}% full"
