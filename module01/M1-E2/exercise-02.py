### M1-E2
print("Temp Converter")
print("Choose a temp")
tempType = input("F (Farenheit) or C (Celcius): ")
num = float(input("Type in the number: "))
if tempType == "c" or tempType == "C":
    print(f"{num * 9 / 5 + 32}°F")
elif tempType == "f" or tempType == "F":
    print(f"{(num - 32) * 5 / 9}°C")