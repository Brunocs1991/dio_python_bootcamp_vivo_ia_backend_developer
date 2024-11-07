class Bike:
  def __init__(self, color, model, year, value, gear=1):
    self.color = color
    self.model = model
    self.year = year
    self.value = value
    self.gear = gear

  def honk(self):
    print(f"{self.model} Honk Honk")

  def stop(self):
    print(f"{self.model}Stopping bike")
    print(f"{self.model}Bike is stopped!")

  def run(self):
    print(f"{self.model}Bike is running")

  def get_color(self):
    return self.color

  def change_gear(self, gear):
    print(f"Changing gear")

  # def __str__(self):
  #     return f"Bike: color={self.color} model={self.model} year={self.year} value={self.value}"

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join(f'{key}={value}' for key, value in self.__dict__.items())}"


b1 = Bike("red", "Trek", 2017, 500)
b1.honk()
b1.stop()
b1.run()
print(b1.color, b1.model, b1.year, b1.value)

b2 = Bike("blue", "Giant", 2018, 600)
b2.honk()  # Bike.honk(b2)
b2.change_gear(10)

b2.get_color()
print(b2)
