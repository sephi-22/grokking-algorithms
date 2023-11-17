# This is a greedy algorithm applied to the knapsack problem as given in chapter 9.
# This will not give the optimal solution.

# Volume of the knapsack.
remaining_volume = 4.0

# Dictionary/hashmaps of the items with their value and weights.
items = {}
items["stereo"] = {3000: 4.0}
items["laptop"] = {2000: 3.0}
items["guitar"] = {1500: 1.0}

# Function to retrieve the max loot and the items.
items_carried = set()  # These are the items we will carry in our knapsack
value_of_loot = 0
overburdened = False  # To check if items can still fit.
while not overburdened:
    best_item = None
    best_value = 0
    for item, item_properties in items.items():
        if (
            list(item_properties.keys())[0] > best_value
            and list(item_properties.values())[0] <= remaining_volume
        ):
            best_item = item
            best_value = list(item_properties.keys())[0]
    if best_item is not None:
        items_carried.add(best_item)
        value_of_loot += best_value
        remaining_volume -= list(items[best_item].values())[0]
        print ("Remaining volume:", remaining_volume)
        del items[best_item]
    else:
        overburdened = True

print("Items carried:", items_carried)
print("Total value of loot:", value_of_loot)
