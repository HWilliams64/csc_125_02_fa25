class Car:
    make: str = "honda"
    model: str = "civic"
    color: str = "red"
    gas_capacity_gallons: int = 100 # total gallons of gas the tank can hold in the gas tank
    current_gas_in_the_tank: float = 0 # how many gallon of gas currently in the tank
    mile_per_gallon: int = 20

    def drive(self, miles_traveled:float|int):
        # How many gallons of gas were used?
        # miles-traveled / MGP. Example: (travel 5 mile w/ 20mpg) 5mile / 20mpg = 1/4 gallon
        total_used_gallons = miles_traveled / self.mile_per_gallon

        # Subtract the gas used for the travel from the gas in the tank
        self.current_gas_in_the_tank -= total_used_gallons




my_honda_civic = Car()
my_honda_civic.color = "orange"

print("Make:", my_honda_civic.make)
print("Model:", my_honda_civic.model)
print("Color:", my_honda_civic.color)

print("-"*40)
your_honda_civic = Car()

print("Make:", your_honda_civic.make)
print("Model:", your_honda_civic.model)
print("Color:", your_honda_civic.color)
