# Modules

# module_func_library Module

import module_func_library as custom

print(dir(custom))

help(custom)

print("addMultipleNumbers: ",
      custom.addMultipleNumbers(5, 9, 8, 5, 4, 7, 5, 1, 2, 7))

print("multiplyNumbers: ", custom.multiplyNumbers(8, 6, 5, 4))
print("subtraction: ", custom.subtraction(85, 32))
print("subtraction: ", custom.subtraction(5, 32))
print("difference: ", custom.difference(9, 58))
