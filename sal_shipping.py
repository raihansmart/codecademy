def ground_shipping(weight):

  if weight < 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  Flat_Charge = 20.00
  return (weight * price_per_pound) + Flat_Charge
  
print(ground_shipping(8.4))

premium_shipping = 125.00

def drone_shipping(weight):
    if weight < 2:
      price_per_pound = 4.50
    elif weight <= 6:
      price_per_pound = 9.00
    elif weight <= 10:
      price_per_pound = 12.00
    else:
      price_per_pound = 14.25

    return weight * price_per_pound 

print(drone_shipping(1.5))

def cheapest_method(weight):

  ground = ground_shipping(weight) 
  drone = drone_shipping(weight)
  premium = premium_shipping 

  if ground < premium and ground < drone:
    method = "Ground Shipping"
    cost = ground

  elif drone < ground and drone < premium:
    method = "Drone Shipping"
    cost = drone

  else:
    method = "Premium Shipping"
    cost = premium

  print(
    "The cheapest way to ship " + str(weight) + " lb is $%.2f with %s Method." 
  % (cost, method)
  )

print(cheapest_method(4.8))
print(cheapest_method(41.5))

