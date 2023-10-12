import time

events = [
  (476, "Fall of the Western Roman Empire"),
  (1066, "Norman Conquest of England"),
  (1492, "Christopher Columbus's first voyage to the Americas"),
  (1776, "United States Declaration of Independence"),
  (1789, "Start of the French Revolution"),
  (1865, "End of the American Civil War"),
  (1969, "Apollo 11 Moon landing"),
  (1989, "Fall of the Berlin Wall")
]

dictionaryOfYears = {
  476: "Fall of the Western Roman Empire",
  1066: "Norman Conquest of England",
  1492: "Christopher Columbus's first voyage to the Americas",
  1776: "United States Declaration of Independence",
  1789: "Start of the French Revolution",
  1865: "End of the American Civil War",
  1969: "Apollo 11 Moon landing",
  1989: "Fall of the Berlin Wall"
}

yearsToVisit = [1492, 1776, 1969, 1989]

def timePortal():
  print("Now you will go on a trip at the times you specified")
  try:
    for year in yearsToVisit:
      event = dictionaryOfYears.get(year)
      if event is not None:
        time.sleep(1)
        print(f"You are traveling in {year} with event {event}")
      else:
        print(f"Event for year {year} not found")
  except:
    print("Such year not found")

def addEvent(year, description):
  dictionaryOfYears[year] = description

def deleteEvent(year):
  dictionaryOfYears.pop(year)

def showEvents():
  for year, desc in dictionaryOfYears.items():
    print(f"{year} - {desc}")

while True:
  print("1. Add event\n2. Show events\n3. Delete event\n4. Portal\n5. Exit")
  choice = int(input("Enter your choice: "))

  if choice == 1:
    year = int(input("Enter year: "))
    desc = input("Enter description of event: ")
    addEvent(year, desc)
  elif choice == 2:
    showEvents()
  elif choice == 3:
    try:
      year = int(input("Enter deleted year of event: "))
      deleteEvent(year)
    except ValueError:
      print("No such year")
  elif choice == 4:
    timePortal()
  elif choice == 5:
    break