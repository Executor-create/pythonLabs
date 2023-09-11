# Task 1
a = 2
b = 4.5
c = False
d = "Hello"

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Task 2
val = int(input())
val2 = int(input())

print(val + val2)
print(val - val2)
print(val * val2)
print(val / val2)

# Task 3
print("1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exit")
choice = int(input())

index = 0

while index <= 4:
  if choice == 1:
    val = int(input())
    val2 = int(input())
    print(val + val2)
    break
  elif choice == 2:
    val = int(input())
    val2 = int(input())
    print(val - val2)
    break
  elif choice == 3:
    val = int(input())
    val2 = int(input())
    print(val * val2)
    break
  elif choice == 4:
    val = int(input())
    val2 = int(input())
    print(val / val2)
    break
  elif choice == 5:
    print("Exit")
    break