def makeChange(amount):
    # Initialize an empty Set to store unique representations
    result_set = set()

    # Loop through each possible number of quarters
    for quarters in range(amount // 25 + 1):
        # Loop through each possible number of dimes
        for dimes in range((amount - quarters * 25) // 10 + 1):
            # Loop through each possible number of nickels
            for nickels in range((amount - quarters * 25 - dimes * 10) // 5 + 1):
                # Calculate the remaining number of pennies
                pennies = amount - quarters * 25 - dimes * 10 - nickels * 5
                # Add the representation to the Set
                result_set.add((quarters, dimes, nickels, pennies))

    return result_set

# Example usage:
amount = 20
result = makeChange(amount)
print("Unique representations of", amount, "cents:")
for representation in result:
    print(representation)
