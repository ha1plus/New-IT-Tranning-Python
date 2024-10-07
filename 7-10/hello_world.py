#Python Variables

#String
x1 = "John"
x2 = str(3)
print("String")
print("X1: " + x1)
print(type(x1))
print("X2: " + x2)
print(type(x2))
print("X1 + X2: " + x1 + x2)
print(type(x1 + x2))
print("\n")

#Integer
y1 = 3
y2 = int(4)
print("Integer")
result_y1 = f"Result Y1: {y1}"
print(result_y1)
print(type(x1))
result_y2 = "Result Y2: %d" % y2
print(result_y2)
print(type(y2))
result_y1_y2 = "Result Y1 + Y2: {}".format(y1+y2)
print(result_y1_y2)
print(type(y1 + y2))
print("\n")

#Float
z1 = 3.5
z2 = float(4.5)
print("Float")
result_z1 = f"Result Z1: {z1}"
print(result_z1)
print(type(z1))
result_z2_f = f"Result Z2 với f...: {z2}"
result_z2_d = f"Result Z2 với d...: %d" % z2
print(result_z2_f)
print(result_z2_d)
print(type(z2))
result_z1_z2 = f"Result Z1 + Z2: {z1 + z2}"
print(result_z1_z2)
print(type(y1 + y2))
print("\n")

#Boolean
is_active = True
flag = False
print("Boolean")
result_is_active= f"Result Is Active: {is_active}"

print(type(is_active))
result_flag= f"Result Flag: {flag}"
print(result_flag)
print(type(flag))
print("\n")

#Python Operators

#Arithmetic Operators
print("Arithmetic Operators")
x = 10
y = 3
result_x= f"Result X : {x}"
result_y= f"Result Y: {y}"
result_x_addition_y= f"Result X + Y: {x + y}"
result_x_subtraction_y= f"Result X - Y: {x - y}"
result_x_multiplication_y= f"Result X * Y: {x * y}"
result_x_division_y= f"Result X / Y: {x / y}"
result_x_modulus_y= f"Result X % Y: {x % y}"
result_x_exponentiation_y= f"Result X ** Y: {x ** y}"
result_x_floor_division_y= f"Result X // Y: {x // y}"
result_x_y= f"Result X // Y: {x // y}"
print(result_x)
print(result_y)
print(result_x_addition_y)
print(result_x_subtraction_y)
print(result_x_multiplication_y)
print(result_x_division_y)
print(result_x_modulus_y)
print(result_x_exponentiation_y)
print(result_x_floor_division_y)
print("\n")

#Comparison Operators
print("Comparison Operators")
result_x_equal_y= f"Result X equal Y: {x == y}"
result_x_not_equal_y= f"Result X not equal Y: {x != y}"
result_x_greater_than_y= f"Result X greater than Y: {x > y}"
result_x_less_than_y= f"Result X less than Y: {x < y}"
result_x_greater_than_or_equal_to_y= f"Result X greater than or equal to Y: {x >= y}"
result_x_less_than_or_equal_to_y= f"Result X less than or equal to Y: {x <= y}"
print(result_x_equal_y)
print(result_x_not_equal_y)
print(result_x_greater_than_y)
print(result_x_less_than_y)
print(result_x_greater_than_or_equal_to_y)
print(result_x_less_than_or_equal_to_y)
print("\n")

#If .. else
a = 33
b = 200
result_a = f"Result a: {a}"
result_b = f"Result b: {b}"
print("If...else")
print(result_a)
print(result_b)
if a == b:
  print("a and b are equal")
elif b > a:
  print("b is greater than a")
else:
  print("b is less than a")
print("\n")

#For White and Break Continue
print("For White and Break Continue")
fruits = ["apple", "banana", "cherry"]
print("For and Continue")
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("\n")

print("White and Break")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("\n")