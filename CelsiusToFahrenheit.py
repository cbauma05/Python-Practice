def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("{:.2f} degrees Celsius is equivalent to {:.2f} degrees Fahrenheit.".format(celsius, fahrenheit))