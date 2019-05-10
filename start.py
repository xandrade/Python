def testing_var_1():
    return 1

def testing_var_2():
    return 2

def testing_failed():
    return None

def testing(var):
    if var == 1: return testing_var_1()
    if var == 2: return testing_var_2()
    else:  return testing_failed()

print(testing(1))
print(testing(3))
print(testing(22))
