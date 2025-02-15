weight = input("Enter weight of package: ")
weight = float(weight)

#Flat ground shipping rate
cost_ground_premium = 125

#Ground Shipping
if weight <= 2:
  cost = 1.50 * weight + 20
elif weight <= 6:
  cost = 3 * weight + 20
elif weight <= 10:
  cost = 4 * weight + 20
elif weight > 10:
  cost = 4.75 * weight + 20
print("Ground Shipping cost:", cost)
print("Ground Premium cost:", cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = 4.50 * weight
elif weight <= 6:
  cost_drone = 9 * weight
elif weight <= 10:
  cost_drone = 12 * weight
elif weight > 10:
  cost_drone = 14.25 * weight
print("Drone Shipping cost:", cost_drone)