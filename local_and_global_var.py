gun = 10

def checkpoint(soldiers):
    global gun # Use the global variable 'gun'
    gun -= soldiers # local variable 'gun' referenced before assignment
    print("[Inside Function] Remaining guns : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun -= soldiers # local variable(parameter 'gun')
    print("[Inside Function with Return] Remaining guns : {0}".format(gun))
    return gun

print("Total guns before function call : {0}".format(gun))
checkpoint(2)
print("Total guns after function call : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("Total guns after function call with return : {0}".format(gun))