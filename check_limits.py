def is_in_range(value,min_value,max_value=None):
  if max_value != None:
    return value > min_value and value < max_value
  else:
    return value > min_value

def battery_is_ok(temperature, soc, charge_rate):
  if is_in_range(temperature,0,45):
  #if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  elif is_in_range(soc,20,80):
  #elif soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  elif is_in_range(charge_rate,0.8):
  #elif charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
