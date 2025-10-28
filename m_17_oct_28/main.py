from time import sleep
from csc_125_02_fa25.m_17_oct_28.car import Car
from csc_125_02_fa25.m_17_oct_28.garage import Garage


my_garage = Garage(4, 10,600)

my_honda_civic = Car(make="honda", model="civic", color="orange")
your_porsche = Car(make="Porsche", model="911", color="yellow")
your_ferrari = Car(make="Ferrari", model="Roma", color="red")

my_honda_civic_ticket = my_garage.park(my_honda_civic)
sleep(10)

fee, car = my_garage.retrieve(my_honda_civic_ticket)

print(f"${fee}, Is correct car {car is my_honda_civic}")

your_porsche_ticket = my_garage.park(your_porsche)
sleep(1)
fee, car = my_garage.retrieve(your_porsche_ticket)
print(f"${fee}, Is correct car {car is your_porsche}")
