# Exception Handling 1
'''try:
    
    numb1 = int(input("Enter 1 number: "))
    numb2 = int(input("Enter 2 number: "))
    rez = numb1 / numb2
    print (rez)
    
except ValueError as ex:
    print (" invalid format number")
    print(ex)

except ZeroDivisionError as ex:
    print (" zero not division")
    print(ex)
'''
try:
    
    numb1 = int(input("Enter 1 number: "))
    numb2 = int(input("Enter 2 number: "))
    rez = numb1 / numb2
    print (rez)
    
except (ValueError,ZeroDivisionError) :
    print (" invalid format number")
    

