def main():
    temperatures = []

    print("Enter the temperatures for each day of the week:")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in days:
        temp = float(input(f"Enter temperature for {day}: "))
        temperatures.append(temp)

    lowest = min(temperatures)
    highest = max(temperatures)
    total = sum(temperatures)
    average = total / len(temperatures)

    print("\nWeekly Temperature Report")
    print(f"Lowest Temperature: {lowest}°")
    print(f"Highest Temperature: {highest}°")
    print(f"Sum of Temperatures: {total}°")
    print(f"Average Temperature: {average:.2f}°")

main()
