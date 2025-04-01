def convert(fahrenheit):
    """Converts Fahrenheit to Celsius using the formula:
       celsius = 5/9 * (fahrenheit - 32)
    """
    return 5/9 * (fahrenheit - 32)

def main():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    celsius = convert(fahrenheit)
    print("Temperature in Celsius:", celsius)

    if celsius > 20:
        print("ITS HOT HERE")
    else:
        print("IT'S COLD HERE")

if __name__ == "__main__":
    main()
