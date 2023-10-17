def fractional_knapsack(items: list[tuple], capacity: int) -> tuple[list, float]:
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        weight, value = item
        if capacity >= weight:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((capacity, fraction * value))
            total_value += fraction * value
            break

    return knapsack, total_value

items = [(10, 60), (20, 100), (30, 120)]
capacity = 50

knapsack, total_value = fractional_knapsack(items, capacity)

print("Items in the knapsack:")
for item in knapsack:
    weight, value = item
    print(f"Weight: {weight}, Value: {value}")

print("Total Value:", total_value)