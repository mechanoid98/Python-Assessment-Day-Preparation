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
  cost = (price_per_pound*weight) + 0
  return cost

def cheapest_method(weight):
  if (drone_shipping_cost(weight)) < (ground_shipping_cost(weight)) and premium_shipping:
    return print("The cheapest shipping method is by drone. The price would be "+str(drone_shipping_cost(weight)))
  elif (ground_shipping_cost(weight)) < (drone_shipping_cost(weight)) and premium_shipping:
    return print("The cheapest shipping method is by ground. The price would be "+str(ground_shipping_cost(weight)))
  elif premium_shipping < ground_shipping_cost(weight) and drone_shipping_cost(weight):
    return print("The cheapest shipping method is the premium shipping method. The price would be "+str(premium_shipping))

cheapest_method(41.5)

