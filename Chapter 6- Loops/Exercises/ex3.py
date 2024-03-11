while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket is 35 Aed") 
    else:
        print("Your ticket is 55 Aed")