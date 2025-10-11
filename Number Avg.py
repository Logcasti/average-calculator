def Average_Func(Number_List,x):
    Sum_of_List=sum(Number_List)#Add all numbers in the list together
    Average=Sum_of_List/x

    Round_OptsN=['0','1','2','3']
    Round_OptsL=['N','n','No','NO','nO']
    while True:
        print("""Do you want to round?
             Input N for not
             Input 0 for whole number.
             Input 1 for nearest tenth.
             Input 2 for nearest hundredth.
             Input 3 for nearest Thousandth.""")
          

        roundn=input("Put choice in here:").strip()
        if roundn in Round_OptsL:  #Compares to words and letters allowed
            Average1=Average
            break
        elif roundn in Round_OptsN:
            Roundn_int=int(roundn)
            Average1=round(Average,Roundn_int) #Compares to Numbers allowed
            break
            
        else:
            print("Sorry, please choice from the following options:")
            continue #Can not accept anything other than what is asked for

        
    return Average, Average1


while True:
        
    Number_List=[]              #Declare List
    y=0


    while True:
        try:
            x=int(input("How many numbers?"))#How many times to loop               

            if x<=0:
                print("Refrain from typing 0 or negative numbers for amount of numbers")
                continue #Can't run amount of numbers at 0 times or less.
            else:
                break
        except ValueError:
            print("Please type a full number")
            continue #Restart do to not using a integer 
             
                
            

    while True:
        if y==x:
            break
        #Loop until x(number you need to input) are met.
       
        else:
            try:
                Set_Number=float(input("Enter Number:"))      #Numbers are chosen
                y=y+1  #Add to loop counter
                Number_List.append(Set_Number) #Numbers are added to list
            except ValueError:
                print("Please Type a number only:")
                continue #Exepts any kind of number only ex: 1.5, -1, 1

    Average_out,Average1_out=Average_Func(Number_List,x)

            
    print("Your number(s) were: "+ str(Number_List))
    print("You had "+str(x)+" number(s)")
    print("The average of your number:"+ str(Average_out))
    print("The rounded average of your number is:"+ str(Average1_out))
             


    while True:
        Stop_Start=input(
            '''
            Do you want to run again or stop?
            Type E to leave application
            Type S to start application again
            Enter E/S here:''').lower()
        if Stop_Start=='e':
            exit()
        elif Stop_Start=='s':
            break
        else:
            print("Please Type E or S")
            continue #Numbers, Words, and letters not equal to E/e or S/s do not state restart or leave  
            
    
    


    
