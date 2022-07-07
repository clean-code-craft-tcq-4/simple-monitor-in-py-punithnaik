def check_range(value,min_value,max_value=None):
  if max_value == None:
    return value > min_value
  else:
    return value < min_value or value > max_value

def print_result(element):
  print(element + " is out of range!")

def battery_is_ok(temperature, soc, charge_rate):
  result = []
  parameters = {"Temperature":[temperature,0,45],"State of Charge":[soc,20,80],"Charge rate":[charge_rate,0.8,None]}
  for element in parameters:
    result_value = check_range(parameters[element][0],parameters[element][1],parameters[element][2])
    result.append(result_value)
    if result_value == True:
      print_result(element)
      return False
  return True
  

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
