"""
Author: <John Psofimis>
Assignment: #1
"""
gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool 

workout_stats = { 
    "Alex": (30, 45, 50),
    "Jamie": (40, 35, 30),
    "Taylor": (30, 45, 20)
}

totals = {}

for friend in workout_stats:
    total = sum(workout_stats[friend])
    totals[friend + "_Total"] = total

workout_stats.update(totals)


workout_list = [ 
    [30, 45, 50],
    [40, 35, 30],
    [30, 45, 20]
]

print("Yoga and running minutes of all friends:")
for row in workout_list:
    print(row[2])

print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[1:]:
    print(row[2])

for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[friend + "_Total"] >=120:
        print ("Good job staying active,", friend)

name = input("\nEnter a friend's name: ")

if name in workout_stats and isinstance(workout_stats[name], tuple): 
    print("\nWorkout minutes for", name)
    print("Yoga:", workout_stats[name][0])
    print("Running:", workout_stats[name][1])
    print("Weightlifting:", workout_stats[name][2])
    print("Total:", workout_stats[name + "_Total"])
else:
    print("Friend", name, "not found in records.")

highest = max (
    workout_stats["Alex_Total"],
    workout_stats["Jamie_Total"],
    workout_stats["Taylor_Total"]
)

lowest = min (
    workout_stats["Alex_Total"],
    workout_stats["Jamie_Total"],
    workout_stats["Taylor_Total"]
)

if highest == workout_stats ["Alex_Total"]:
    print("\nFriend with highest total workout minutes: Alex")
elif highest == workout_stats ["Jamie_Total"]:
    print("Friend with highest total workout minutes: Jamie")
else:
    print("Friend with highest total workout minutes: Taylor")

if lowest == workout_stats ["Alex_Total"]:
    print("Friend with lowest total workout minutes: Alex")
elif lowest == workout_stats ["Jamie_Total"]:
    print("Friend with lowest total workout minutes: Jamie")
else:
    print("Friend with lowest total workout minutes: Taylor")