# Initialize an empty list to store sales data
sales_data = []
grand_total = 0

# Number of salesmen
num_salesmen = int(input("Enter the number of salesmen: "))

for _ in range(num_salesmen):
    name = input("\nEnter salesperson's name: ")
    
    # Collect sales data for 5 items
    sales = []
    for i in range(1, 6):
        sale = int(input(f"Enter sales for Item{i}: "))
        sales.append(sale)

    # Calculate total sales for the salesperson
    total_sales = sum(sales)
    grand_total += total_sales

    # Store data
    sales_data.append([name] + sales + [total_sales])

# Display sales data in tabular format
print("\nSales Data")
print(f"{'Name':<10} {'Item1':<6} {'Item2':<6} {'Item3':<6} {'Item4':<6} {'Item5':<6} {'TotalSales':<10}")
for data in sales_data:
    print(f"{data[0]:<10} {data[1]:<6} {data[2]:<6} {data[3]:<6} {data[4]:<6} {data[5]:<6} {data[6]:<10}")

# Display grand total
print(f"\nGrandTotal: {grand_total}")
