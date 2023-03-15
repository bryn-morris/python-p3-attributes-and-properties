# class Human:
#     species = "Homo sapiens"

#     def get_age(self):
#         print("Retrieving age.")
#         return self._age

#     def set_age(self, age):
#         print(f"Setting age to { age }")
#         self._age = age

#     age = property(get_age, set_age,)

# mara = Human()

# mara.set_age(55)

# print(mara.age)

# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

human.temperature = -300