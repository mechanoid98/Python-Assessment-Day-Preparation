premium_shipping = 125

def ground_shipping_cost(weight):
  if weight > 10:
    price_per_pound = 4.75
  elif 6 < weight <= 10:
    price_per_pound = 4.00
  elif 2 < weight <= 6:
    price_per_pound = 3.00
  elif weight < 2:
    price_per_pound = 1.50
  cost = (price_per_pound*weight) + 20
  return cost

def drone_shipping_cost(weight):
  if weight > 10:
    price_per_pound = 14.25
  elif 6 < weight <= 10:
    price_per_pound = 12.00
  elif 2 < weight <= 6:
    price_per_pound = 9.00
  elif weight < 2:
    price_per_pound = 4.50
  cost = (price_per_pound*weight)
  return cost


def print_cheapest_shipping_method(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_shipping
  drone = drone_shipping_cost(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  
  print(
    "The cheapest option available is $%.2f with %s shipping." 
       % (cost, weight))
  
print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)

