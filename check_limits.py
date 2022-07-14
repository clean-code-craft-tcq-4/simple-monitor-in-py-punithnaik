language = "English" #For German language, input "German"

#Prints warning in english
def print_warning_english(element,limit):
  if limit == "min":
    print("Warning: " + element + " approaching minimum value")
  elif limit == "max":
    print("Warning: " + element + " approaching maximum value")

#Prints alert in english
def print_alert_english(element):
  print(element + " is out of range!")

#Checks the text type (Warning or alert) and calls the corresponding print function      
def print_english(text_type,element,limit):
  if text_type == "Warning":
    print_warning_english(element,limit)
  else:
    print_alert_english(element)

#Prints warning in german
def print_warning_german(element,limit):
  if limit == "min":
    print("Warnung: " + element + " nähert sich dem Mindestwert")
  else:
    print("Warnung: " + element + " nähert sich dem Maximalwert")

#Prints alert in german
def print_alert_german(element):
  print(element + " liegt außerhalb des Bereichs!")
      
#Checks the text type (Warning or alert) and calls the corresponding print function
def print_german(text_type,element,limit):
  if text_type == "Warning":
    print_warning_german(element,limit)
  else:
    print_alert_german(element)

#Checks the language and calls corresponding print function
def print_text(text_type,element,limit=None):
  global language
  if language == "English":
    print_english(text_type,element,limit)
  elif language == "German":
    print_german(text_type,element,limit)    

def check_range(value,min_value,max_value=None):
  if max_value == None:
    return value < min_value
  else:
    return value < min_value or value > max_value

def check_warning(element,value,min_value,max_value=None):
  tolerance_percent = 5
  if max_value == None and value > min_value and value < (min_value + (min_value*tolerance_percent/100)):
    print_text("Warning", element, "min")
  elif max_value != None and value > min_value and value < min_value + (max_value*tolerance_percent/100):
    print_text("Warning", element, "min")
  elif max_value != None and value < max_value and value > max_value - (max_value*tolerance_percent/100):
    print_text("Warning", element, "max")

def battery_is_ok(temperature, soc, charge_rate):
  result = []
  parameters = {"Temperature":[temperature,0,45],"State of Charge":[soc,20,80],"Charge rate":[charge_rate,0.8,None]}
  for element in parameters:
    check_warning(element,parameters[element][0],parameters[element][1],parameters[element][2])
    result_value = check_range(parameters[element][0],parameters[element][1],parameters[element][2])
    result.append(result_value)
    if result_value == True:
      print_text("alert", element)
      return False
  return True
  

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is False)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(0, 20, 0.8) is True)
  assert(battery_is_ok(46, 81, 0.9) is False)
  assert(battery_is_ok(44, 79, 0.83) is True)
  assert(battery_is_ok(1, 21, 0.83) is True)
