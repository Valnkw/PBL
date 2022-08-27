##Simple 2 input calculator 8/26/22

save = 0.0


while True:

     #this will be ans
    
    first=(input("Enter your first number: "))   #takes in first input
    if first=="ans":
      first = save 
    oper=input("Enter your op: ")
    second=(input("Enter your second number: ")) #takes in second input
    if second=="ans":
      second = save 
    

    if oper == "*":
        answer=float(first)*float(second) # multiplies the 2 inputs
        print(answer)
        save = answer
    if oper == "-":
        answer=float(first)-float(second) # subtracts the 2 inputs
        save = answer
    if oper == "+":
        answer=(float(first)) + (float(second)) # adds the 2 inputs 
        print(answer)
        save = answer
    if oper == "**":
        answer=float(first)**float(second) # takes the first input raises it to the power of the second input
        print(answer)
        save = answer
    if oper == "/":
        answer=float(first)/float(second) # divides the 2 inputs
        print(answer)
        save = answer
    mac=input("Continue y or n: ") # user can continue to use calculator
    if mac != "y":
        exit()


  





