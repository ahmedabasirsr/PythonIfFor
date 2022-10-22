# Exception Handling 2

try:
    
    numb1 = int(input("Enter 1 number: "))
    numb2 = int(input("Enter 2 number: "))
    rez = numb1 / numb2
    print (rez)
    
except (ValueError,ZeroDivisionError) :
    print (" invalid format number")
    
else:
    print (" continue befor except")
    print(rez * 3)

finally:
    print (" print this message however try and except ")
