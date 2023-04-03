while True:
    while True:
        temp = input("Enter the temperature: ")
        try:
            temp = float(temp)
            break
        except ValueError:
            print("Stop clowning around! Enter a number!")

    conversion_type = input("Convert to Celsius (C) or Fahrenheit (F): ").capitalize()

    if conversion_type == "C":
        celsius = (temp - 32) * 5 / 9
        print("The temperature converted to Celsius is: ", celsius)
    elif conversion_type == "F":
        fahrenheit = (temp * 9 / 5) + 32
        print("The temperature converted to Fahrenheit is: ", fahrenheit)
    else:
        print("Ma\'am we only do Celsius or Fahrenheit conversions here!")

    another_conversion = input("Do you wanna convert another temperature (y/n): ").lower()
    if another_conversion == "n":
        print("Ok, bye!")
        break


