import matplotlib.pyplot as plt

# Monthly billing value of the distributor, broken down by state
billing_values = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Others': 19849.53
}

# Calculate the total monthly billing value
total_billing_value = sum(billing_values.values())

# Calculate the percentage of representation of each state within the total monthly value
percentages = {state: (value / total_billing_value) * 100 for state, value in billing_values.items()}

# Print the percentages
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")

# Option to display the percentages in a graph
show_graph = input("Do you want to display the percentages in a graph? (y/n) ").lower() == 'y'
if show_graph:
    # Create a pie chart
    plt.pie(percentages.values(), labels=percentages.keys(), autopct='%1.1f%%')
    plt.title("Percentage of Representation by State")
    plt.show()
