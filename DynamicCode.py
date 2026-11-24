import random
# Shahad AlMahri 2202144796 - Batoul Ahmadi 2221189678

# gloabl variables
MAX_WEIGHT = 25
MAX_COST = 20
MIN_FRESHNESS = 2
CURRENT_SEASON = "Spring"

""" overlapping subproblems: different selections can reach the same total weight and cost
optimal substructure: The best solution for weight w and cost c depends on smaller subproblems (w-weight[i], c-cost[i])
dp[w][c] = maximum total freshness we can get with total weight = w and cost = c 
***** OPTIMAL SOLUTION ******
after filling dp we trace back from (MAX_WEIGHT, MAX_COST) find out which fruits were included by checking if taking a fruit improved freshness compared to not taking it
kg 25, kd20
"""
#output1
"""Papaya | 3kg | 3KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Lemon | 1kg | 1KD | Freshness: 1
Banana | 5kg | 3KD | Freshness: 2

Dynamic Programming Result:
Total combinations that match the optimal solotion is 116"""
#output 2
"""selected fruits:
Banana | 5kg | 3KD | Freshness: 2
Lemon | 1kg | 1KD | Freshness: 1
Apricot | 2kg | 4KD | Freshness: 2
Papaya | 3kg | 3KD | Freshness: 2
Mango | 6kg | 8KD | Freshness: 3

Dynamic Programming Result:
Total combinations that match the optimal solotion is 0"""
#output 3
"""selected fruits:
Banana | 5kg | 3KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2
Papaya | 3kg | 3KD | Freshness: 2
Mango | 6kg | 8KD | Freshness: 3
Lemon | 1kg | 1KD | Freshness: 1

Dynamic Programming Result:
Total combinations that match the optimal solotion is 351"""
#output 4
"""
selected fruits:
Mango | 6kg | 8KD | Freshness: 3
Lemon | 1kg | 1KD | Freshness: 1
Banana | 5kg | 3KD | Freshness: 2
Papaya | 3kg | 3KD | Freshness: 2
Apricot | 2kg | 4KD | Freshness: 2

Dynamic Programming Result:
Total combinations that match the optimal solotion is 437"""

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

# step 3: make a list for shuffling
fruit_list = []
for name, info in spring_fruits.items():
    fruit_list.append((name, info))


# step 4: initialize DP table
# dp[w][c] = maximum freshness achievable with weight w and cost c
dp = [[0 for i in range(MAX_COST + 1)] for j in range(MAX_WEIGHT + 1)]
# firatly starting points  1 weight 1 cost= 0 freshness
dp[1][1] = 0  

# step5: fill the DP table
for name, info in fruit_list:
    weight = info["weight"]
    cost = info["cost"]
    freshness = info["freshness"]
    is_even = info["even"]

    # How many times we can use this fruit:
    times = 25 if is_even else 1  # if even weight, unlimited use; if odd, only once
    counter =0
    for i in range(times):
        new_dp = [row[:] for row in dp]  # Copy current dp table
        for w in range(MAX_WEIGHT + 1):
            for c in range(MAX_COST + 1):
                if dp[w][c] != -1:
                    new_w = w + weight
                    new_c = c + cost
                    if new_w <= MAX_WEIGHT and new_c <= MAX_COST:
                        new_freshness = dp[w][c] + freshness
                        if new_freshness > new_dp[new_w][new_c]:
                            new_dp[new_w][new_c] = new_freshness
                            counter+=1

        dp = new_dp  # update dp
        

# step 6: find the best possible solution
best_weight = -1
best_cost = -1
best_freshness = -1

for w in range(MAX_WEIGHT + 1):
    for c in range(MAX_COST + 1):
        if dp[w][c] >= MIN_FRESHNESS:
            if w == MAX_WEIGHT and c == MAX_COST:
                if dp[w][c] > best_freshness:
                    best_weight = w
                    best_cost = c
                    best_freshness = dp[w][c]
# Step 6: Print results
print("\nselected fruits:")
for name, info in fruit_list:
    print(f"{name} | {info['weight']}kg | {info['cost']}KD | Freshness: {info['freshness']}")
if best_freshness != -1:
    print("\nDynamic Programming Result:")
    print(f"Total combinations that match the optimal solution is {counter}")
else:
    print("\nDynamic Programming Result:")
    print(f"No exact match found for 25kg and 20KD with minimum freshness {MIN_FRESHNESS}")