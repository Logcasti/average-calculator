def Average_Func(Number_List,x):
    Sum_of_List=sum(Number_List)#Add all numbers in the list together
    Average=Sum_of_List/x
    Round_OptsN=['0','1','2','3']
    Round_OptsL=['N','n','No','NO']
    while True:
        print("""Do you want to round?
             Input N for not
             Input 0 for whole number.
             Input 1 for nearest tenth.
             Input 2 for nearest hundredth.
             Input 3 for nearest Thousandth.""")
          

        roundn=input("Put choice in here:").strip()
        if roundn in Round_OptsL:
            Average1=Average
            break
        elif roundn in Round_OptsN:
            Roundn_int=int(roundn)
            Average1=round(Average,Roundn_int)
            break
            
        else:
            print("Sorry, please choice from the following options:")
    print("Your number(s) were: "+ str(Number_List))
    print("You had "+str(x)+" number(s)")
    print("The average of your number:"+ str(Average))
    print("The rounded average of your number is:"+ str(Average1))

            
        
    return Average, Average1



Number_List=[]              #Declare List
y=0


while True:
    x=int(input("How many numbers?"))#How many times to loop               
    if x<=0:
        print("Refrain from typing 0 or negative numbers for amount of numbers")
    else:
        break

while True:
    if y==x:
        break
    #Loop until x(number you need to input) are met.
   
    else:
        Set_Number=float(input("Enter Number:"))      #Numbers are chosen
        y=y+1  #Add to loop counter
        Number_List.append(Set_Number) #Numbers are added to list

Average_Func(Number_List,x)
    

       
    


    
