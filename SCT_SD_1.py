# Temperature conversion program
unit = input("Enter the default temperature scale (Kelvin(K)/Celsius(C)/Fahrenheit(F)): ").strip().upper()
temp = float(input("Enter temperature: "))

if unit == 'K':
    nt1 = round((temp - 273.15), 1)  # Kelvin to Celsius
    nt2 = round(((9 * nt1) / 5) + 32, 1)  # Celsius to Fahrenheit
    print(f"{temp} K = {nt1} C")
    print(f"{temp} K = {nt2} F")
    
elif unit == 'C':
    nt3 = round((temp + 273.15), 1)  # Celsius to Kelvin
    nt4 = round(((temp * 9) / 5) + 32, 1)  # Celsius to Fahrenheit
    print(f"{temp} C = {nt3} K")
    print(f"{temp} C = {nt4} F")
    
elif unit == 'F':
    nt5 = round(((temp - 32) * 5 / 9), 1)  # Fahrenheit to Celsius
    nt6 = round((273.15 + nt5), 1)  # Celsius to Kelvin
    print(f"{temp} F = {nt6} K")
    print(f"{temp} F = {nt5} C")

else:
    print("Invalid Choice!")
