name = input("Enter your name :")

brith_year = int(input("enter your brith year :"))
age = 2026-brith_year

weight_kg = float(input("Enter the weight in kg :"))
weight = weight_kg*1000

char = input("Enter any one character: ")
ascii_value = ord(char)

name_list = list(name)
name_tuple = tuple(name)
name_set = set(name)

binary_age = bin(age)
octal_age = oct(age)
hex_age = hex(age)

if age>20:
    status = "adult"
else :
    status = "minor"

print("\n----- PROFILE SUMMARY -----")
print("Name:", name)
print("Age:", age, "| Status:", status)
print("Weight (grams):", weight)

print("\nASCII of character:", char, "=", ascii_value)

print("\nName as list:", name_list)
print("Name as tuple:", name_tuple)
print("Name as set:", name_set)

print("\nAge in binary:", binary_age)
print("Age in octal:", octal_age)
print("Age in hexadecimal:", hex_age)