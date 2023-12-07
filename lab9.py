import threading
import random
import time

class Polling:
  def poll(self):
    pass

  def runPolling(self):
    while True:
      self.poll()

  def runPollingInThread(self):
    threading.Thread(target=self.runPolling).start()

class Entrance(Polling):
  def __init__(self):
    super().__init__()
    self.visitors = []
    self.type = "entrance"
    self.money_earned = 0

  def poll(self):
    for visitor in list(self.visitors):
      self.visitors.remove(visitor)
      self.money_earned += visitor.order.price

  def enter(self, visitor):
    self.visitors.append(visitor)

  def __str__(self):
    order_info = ", ".join([f"{visitor.order.title}" for visitor in self.visitors if visitor.order])
    return f"Number of visitors: {len(self.visitors)}, money earned: ${self.money_earned:.2f}, Orders: {order_info}"

class Waiter(Polling):
  def __init__(self, position, salary, tip_rate):
    super().__init__()
    self.position = position
    self.salary = salary
    self.tip_rate = tip_rate

  def poll(self):
    if self.position.type == "table":
      visitor = self.position.enter()
      self.take_order(visitor)
    elif self.position.type == "kitchen":
      order = self.position.take_order()
      if order:
        order.status = Order.Status.READY
        self.position.move(self.position.next)

  def move(self):
    if self.position.type == "table":
      self.position = self.position.next
    elif self.position.type == "kitchen":
      self.position = self.position.prev

  def take_order(self, visitor):
    order = Order(Order.Status.RAW, "coffee", visitor, 5.0)
    self.position.order = order
    self.position = self.position.prev

  def calculate_tip(self):
    return self.position.money_earned * self.tip_rate

class Kitchen(Entrance):
  def __init__(self):
    super().__init__()
    self.order = None

  def poll(self):
    if self.order and self.order.status == Order.Status.RAW:
      print(f"Kitchen received an order for {self.order.title}")
      self.order.status = Order.Status.READY
    elif self.order and self.order.status == Order.Status.READY:
      self.move(self.next)

  def take_order(self):
    order = self.order
    self.order = None
    return order

class Table(Entrance):
  def __init__(self, waiter):
    super().__init__()
    self.waiter = waiter

  def poll(self):
    for visitor in list(self.visitors):
      self.waiter.enter(visitor)

class Order:
  class Status:
    RAW = "raw"
    READY = "ready"

  def __init__(self, status, title, owner, price):
    self.status = status
    self.title = title
    self.owner = owner
    self.price = price

class Visitor:
  def __init__(self, name, order):
    self.name = name
    self.order = order

entrance = Entrance()
waiter = Waiter(entrance, 1.0, 0.1)
kitchen = Kitchen()
table = Table(waiter)

entrance.runPollingInThread()
waiter.runPollingInThread()
kitchen.runPollingInThread()
table.runPollingInThread()

while True:
  time.sleep(1)
    
  visitors = [Visitor(f"John", Order(Order.Status.RAW, "coffee", None, 5.0)) for _ in range(random.randint(1, 5))]
    
  for visitor in visitors:
    entrance.enter(visitor)

  print(entrance)
  print("============================================")
