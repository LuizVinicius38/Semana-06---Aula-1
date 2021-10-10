try:
    numero = int(input(""))
    if numero <= 9:
        print(True)
    else:
        print(False)
except ValueError:
    print(False)
    
    
