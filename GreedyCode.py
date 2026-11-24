import random
# Shahad AlMahri 2202144796 - Batoul Ahmadi 2221189678
# output 1
""" selected fruits:
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2

total Weight: 10 kg
total Cost: 20 KD
total Freshness: 10
Greedy succeeded with an exact match """
#output 2
""" selected fruits:
Lemon | 1kg | 1KD | Freshness: 1
Banana | 5kg | 3KD | Freshness: 2
Papaya | 3kg | 3KD | Freshness: 2
Mango | 6kg | 8KD | Freshness: 3
Apricot | 2kg | 4KD | Freshness: 2

total Weight: 17 kg
total Cost: 19 KD
total Freshness: 10
Greedy failed to reach maximum profit within the maximum weight """
# output 3
""" selected fruits:
Papaya | 3kg | 3KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Lemon | 1kg | 1KD | Freshness: 1

total Weight: 12 kg
total Cost: 20 KD
total Freshness: 11
Greedy succeeded with an exact match """
# output 4
""" selected fruits:
Banana | 5kg | 3KD | Freshness: 2
Lemon | 1kg | 1KD | Freshness: 1
Papaya | 3kg | 3KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2

total Weight: 15 kg
total Cost: 19 KD
total Freshness: 11
Greedy failed to reach maximum profit within the maximum weight
 """
 # gloabl variables
MAX_WEIGHT = 25
MAX_COST = 20
MIN_FRESHNESS = 2
CURRENT_SEASON = "Spring"

# fruits dictionary
fruits = {
    "Mango": {"weight": 6, "cost": 8, "freshness": 3, "even": True, "season": "Spring"},
    "Banana": {"weight": 5, "cost": 3, "freshness": 2, "even": False, "season": "Spring"},
    "Lemon": {"weight": 1, "cost": 1, "freshness": 1, "even": False, "season": "Spring"},
    "Apricot": {"weight": 2, "cost": 4, "freshness": 2, "even": True, "season": "Spring"},
    "Papaya": {"weight": 3, "cost": 3, "freshness": 2, "even": False, "season": "Spring"},
    "Watermelon": {"weight": 8, "cost": 10, "freshness": 5, "even": True, "season": "Summer"},
    "Peach": {"weight": 4, "cost": 5, "freshness": 4, "even": True, "season": "Summer"},
    "Orange": {"weight": 3, "cost": 2, "freshness": 2, "even": False, "season": "Autumn"},
    "Pomegranate": {"weight": 2, "cost": 3, "freshness": 5, "even": True, "season": "Autumn"},
    "Apple": {"weight": 1, "cost": 2, "freshness": 3, "even": False, "season": "Winter"}
}

# step 1: Shuffle the dictionary
fruit_items = list(fruits.items())  # make a list of (name, info)
random.shuffle(fruit_items)         # shuffle the list
fruits = dict(fruit_items)           # recreate the dictionary (random order)

# step 2:filter fruits for current season
spring_fruits = {}
for name, info in fruits.items():
    if info["season"] == CURRENT_SEASON:
        spring_fruits[name] = info

# step 3: make a list for shuffling, make the ratio 
fruit_list = []
for name, info in spring_fruits.items():
    cost_per_weight = info["cost"] / info["weight"]
    fruit_list.append((name, info["freshness"], cost_per_weight, info))


# step 4: Greedy selection 
total_weight = 0
total_cost = 0
total_freshness = 0
selected_fruits = []
used_odd = set() # store if an odd weighted fruit makes entry so we wont select it again

for fruit in fruit_list:
    name = fruit[0]
    info = fruit[3]

    while True:
        if (total_weight + info["weight"] > MAX_WEIGHT) or( total_cost + info["cost"] > MAX_COST):
            break

        if (not info["even"]) and (name in used_odd):
            break

        if not info["even"]:
            used_odd.add(name)

        selected_fruits.append((name, info))
        total_weight += info["weight"]
        total_cost += info["cost"]
        total_freshness += info["freshness"]

        if not info["even"]:
            break

        if total_weight == MAX_WEIGHT and total_cost == MAX_COST:
            break

print("\nselected fruits:")
for name, info in selected_fruits:
    print(f"{name} | {info['weight']}kg | {info['cost']}KD | Freshness: {info['freshness']}")

print(f"\ntotal Weight: {total_weight} kg")
print(f"total Cost: {total_cost} KD")
print(f"total Freshness: {total_freshness}")

if total_weight <= MAX_WEIGHT:
    if total_cost == MAX_COST and total_freshness >= MIN_FRESHNESS:
        print("Greedy succeeded with an exact match")
    elif total_freshness < MIN_FRESHNESS:
        print("Greedy failed to reach minimum freshness threshold of 1")
    elif total_cost <= MAX_COST:
        print("Greedy failed to reach maximum profit within the maximum weight")
