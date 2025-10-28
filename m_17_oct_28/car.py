class Car:

    def __init__(self, make: str, model: str, color: str, gas_cap: int = 100, mpg=20) -> None:
        self.__make = make
        self.__model = model
        self._color = color
        # total gallons of gas the tank can hold in the gas tank
        self._gas_capacity_gallons = gas_cap
        self._mile_per_gallon = mpg
        self._current_gas_in_the_tank = 0  # how many gallon of gas currently in the tank

    def __str__(self) -> str:
        return f"{self._color} {self.__make} {self.__model}"

    def __eq__(self, value: object) -> bool:
        print(f"__eq__(value={value})")

        # if value is not the data type Car return false
        if not isinstance(value, Car):
            print(f"The value {value} is not a car")
            return False

        return (self.__make == value.__make
                and self.__model == value.__model
                and self._color == value._color)

    def get_make(self):
        self.secret = "my secret"
        return self.__make

    def change_color(self, new_color: str):
        self._color = new_color

    def fill_tank(self, fill_amount: float):
        if 0 > fill_amount or fill_amount > 1:
            return 0

        how_many_gallons_to_fill = self._gas_capacity_gallons * fill_amount

        if how_many_gallons_to_fill > self._current_gas_in_the_tank:
            self._current_gas_in_the_tank = how_many_gallons_to_fill
        else:
            return 0

        return how_many_gallons_to_fill

    def drive(self, miles_traveled: float | int):
        """
        Simulates the car driving for the specified number of miles.
        The given miles will subtract the amount of gas from the car's 
        gas tank. The tank will never be less then 0 after using this method.
        """

        # How many gallons of gas were used?
        # miles-traveled / MGP. Example: (travel 5 mile w/ 20mpg) 5mile / 20mpg = 1/4 gallon
        total_used_gallons = miles_traveled / self._mile_per_gallon

        # Subtract the gas used for the travel from the gas in the tank
        self._current_gas_in_the_tank -= min(
            total_used_gallons, self._current_gas_in_the_tank)
