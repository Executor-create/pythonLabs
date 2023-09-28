class Hotel: 
  def __init__(self, cost):
    self.cost = cost
    self.services = []
  
  def addService(self, service):
    self.services.append(service)

  def removeService(self, service):
    self.services.remove(service)

class Service:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def bar(self, client):
    if client.reserve == True:
      if client.age >= 18 and client.money >= self.price:
        if client.stress < 1:
          client.stress -= 0.25
          client.money -= self.price
          if client.stress < 0:
            client.stress = 0
        else:
          print("Your stress value is full")
          exit()
      else:
        print("You're too young")
        exit()
    else:
      print("You don't have reservation")
      exit()
    print(vars(client))

  def eat(self, client):
    if client.reserve == True:
      if client.money > self.price:
        if client.hunger < 1:
          client.hunger += 0.45
          client.money -= self.price
          if client.hunger > 1:
            client.hunger = 1
        else:
          print("Your hunger value is full")
          exit()
      else:
        print("You don't have enough money")
        exit()
    else:
      print("You don't have reservation")
      exit()
    print(vars(client))

  def childrenRoom(self, client):
    if client.reserve == True:
      if client.age < 18:
        if client.stress > 0:
          client.stress -= 0.25
          if client.stress < 0:
            client.stress = 0
        else:
          print("You don't have stress")
          exit()
      else:
        print("You are too old for this")
        exit()
    else:
      print("You don't have reservation")
      exit()
    print(vars(client))
  
  def massage(self, client):
    if client.reserver == True:
      if client.comfort < 1 and client.money >= self.price:
        client.comfort += 0.45
        client.money -= self.price
      else:
        print("Your comfort value is full or you don't have money")
        exit()
    else:
      print("You don't have reservation")
      exit()
    print(vars(client))

class BusinessService(Service):
  def __init__(self, name, price):
    super().__init__(name, price)

  def businessRoom(self, client):
    if client.reserve == True:
      if client.role == "Businessman":
        if client.money > self.price:
          if client.business < 1 and client.show_off < 1:
            client.business += 0.25
            client.show_off += 0.10
            client.money -= self.price
            print(vars(client))
          else:
            print("Your business value is full.")
            exit()
        else:
          print("You don't have enough money")
      else:
        print("You are not a businessman.")
    else:
      print("You don't have reservation")
      exit()

class ResortService(Service):
  def __init__(self, name, price):
    super().__init__(name, price)

  def doSport(self, client):
    if client.reserve == True:
      if client.role == "Sportsman":
        if client.money > self.price:
          if client.sport < 1.0:
            client.sport += 0.25
            client.money -= self.price
            print(vars(client))
          else:
            print("Your sport value is full.")
        else:
          print("You don't have enough money")
      else:
        print("You are not a sportsman.")
    else:
      print("You don't have reservation")
      exit()

class BusinessHotel(Hotel):
  def __init__(self, cost):
    super().__init__(cost)
  
class ResortHotel(Hotel):
  def __init__(self, cost):
    super().__init__(cost)

class Client:
  def __init__(self, age, hunger, comfort, stress, money):
    self.age = age
    self.hunger = hunger
    self.comfort = comfort
    self.stress = stress
    self.money = money
    self.reserve = False

  def reservation(self, hotel):
    if self.money >= hotel.cost:
      self.money -= hotel.cost
      self.reserve = True
      print("You reserved an hotel")
    else:
      print("You don't have enough money to reserve hotel")

class Businessman(Client):
  def __init__(self, age, hunger, comfort, stress, money, business, show_off):
    super().__init__(age, hunger, comfort, stress, money)
    self.business = business
    self.show_off = show_off
    self.role = "Businessman"

class Sportsman(Client):
  def __init__(self, age, hunger, comfort, stress, money, sport):
    super().__init__(age, hunger, comfort, stress, money)
    self.sport = sport
    self.role = "Sportsman"

  def competition(self, *sportsmen):
    max_value = float('-inf')
    min_value = float('inf')

    for sportsman in sportsmen:
      sportsman_sport = sportsman.sport

      if sportsman_sport > max_value:
        max_value = sportsman_sport
      if sportsman_sport < min_value:
        min_value = sportsman_sport

    print(f"Highest sports value with {max_value} points")
    print(f"Lowest sports value with {min_value} points")

hotel = Hotel(200)
busHotel = BusinessHotel(500)
resHotel = ResortHotel(200)

busService = BusinessService("Business Room", 500)
resService = ResortService("Do Sport", 200)
childService = Service("Child", 500)
eatService = Service("Eat", 100)
barService = Service("Bar", 200)

busHotel.addService(busService)
hotel.addService(barService)
hotel.addService(barService)
hotel.addService(childService)

businessman = Businessman(50, 0.25, 0.50, 0.45, 1000, 0.25, 0.5)
sportsman = Sportsman(50, 0.25, 0.50, 0, 1000, 0.25)
client = Client(15, 0.50, 0.25, 0.43, 40)

businessman.reservation(hotel)

barService.bar(businessman)