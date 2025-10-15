#Round Half Up and Bank Rounding
def Half_Up(Average:int,Average1:int,roundn:str)->int:
            Tolerance=0.0000000001
            if roundn=='0':
                Average1=round(Average,int(roundn))
                if Average-.5==Average1:
                    Average1=Average+.5
            elif roundn=='1':
                Average1=round(Average,int(roundn))  #1.15=1.1    round down
                if abs(Average-Average1-0.05)<Tolerance:
                    Average1=round(Average1+.1,int(roundn))

            elif roundn=='2':
                Average1=round(Average,int(roundn))
                if abs(Average-Average1-0.005)<Tolerance:
                    Average1=round(Average1+.01,int(roundn))
            else:
                Average1=round(Average,int(roundn))
                if abs(Average-Average1-0.0005)<Tolerance:
                    Average1=round(Average1+.001,int(roundn))
                    
            return Average1


def Bank_Rounding(Average:int, Average2:int,roundn:str)->int:
            Roundn_int=int(roundn)
            Average2=round(Average,Roundn_int)
            return Average2
    
def Round_Typ():
    Round_Inputs=[1,2,3]
    while True:
        try:
            Type_Round=int(input('''Do you want to do Bank Rounding, Round Half-Up, or both
                      Input 1 for Bank Rounding
                      Input 2 for Round Half-up
                      Input 3 for Both
                Input here: '''))
            if Type_Round in Round_Inputs:
                break
            else:
                print('Please type the Following options:')
                continue
        except ValueError:
            print('Please type the Following options:')
            continue
    return Type_Round
#-------------------------------
def Average_Func(Number_List,Loop):
    Sum_of_List=sum(Number_List)#Add all numbers in the list together
    Average=Sum_of_List/Loop

    Round_OptsN=['0','1','2','3']
    Round_OptsL=['N','n','No','NO','nO']
 

    while True:
        try:

            roundn=input("""What value do you want to round by:
                 Input N for Don't want to round
                 Input 0 for whole number.
                 Input 1 for nearest tenth.
                 Input 2 for nearest hundredth.
                 Input 3 for nearest Thousandth.
            Input Here:""").strip()
            CounterRND=0
            if roundn in Round_OptsL:
                Average1=Average
                Average2=Average

                break
                
            elif roundn in Round_OptsN:
                Average1=Average
                Average2=Average

             
                Type_Round_out=Round_Typ()
                if Type_Round_out==0:
                    CounterRND=CounterRND+1
                    Average2=Bank_Rounding(Average,Average2,roundn)
                    break
                elif Type_Round_out==1:
                    CounterRND=CounterRND+2
                    Average1=Half_Up(Average,Average1,roundn)
                    break
                else:
                    CounterRND=CounterRND+3
                    Average1=Half_Up(Average,Average1,roundn)
                    Average2=Bank_Rounding(Average,Average2,roundn)
                    break
            else:
                print("Sorry, please choice from the following options:")
                continue #Can not accept anything other than what is asked for
        except ValueError:
                print('Please input one of the following choices')
                continue
    return Average,Average1,Average2,CounterRND

     




    
        



while True:
    Number_List=[]              #Declare List

    while True:
        try:
            Loop=int(input("How many numbers?"))#How many times to loop               

            if Loop<=0:
                print("Refrain from typing 0 or negative numbers for amount of numbers")
                continue #Can't run amount of numbers at 0 times or less.
            else:
                break
        except ValueError:
            print("Please type a full number")
            continue #Restart do to not using a integer 
             
                
            
    for i in range(Loop): #Nested Loop; Run the While True Loop x amount of times
        while True:       #Make sure user is using correct numbers to continue Nested Loop
            try:
                Set_Number=float(input("Enter Number:"))      #Numbers are chosen
                  #Add to loop counter
                Number_List.append(Set_Number) #Numbers are added to list
                break
            except ValueError:
                print("Please Type a number only:")
                continue #Exepts any kind of number only ex: 1.5, -1, 1

    Average_out,Average1_out,Average2_out,CounterRND_out=Average_Func(Number_List,Loop)

    if CounterRND_out==0:
        print("Your number(s) were: "+ str(Number_List))
        print("You had "+str(Loop)+" number(s)")
        print("The average of your number:"+ str(Average_out))
    elif CounterRND_out==1:
        print("Your number(s) were: "+ str(Number_List))
        print("You had "+str(Loop)+" number(s)")
        print("The average of your number:"+ str(Average_out))
        print("Bank Rounding: The rounded average of your number is:"+ str(Average2_out))
    elif CounterRND_out==2:
        print("Your number(s) were: "+ str(Number_List))
        print("You had "+str(Loop)+" number(s)")
        print("The average of your number:"+ str(Average_out))
        print("Half-Up Rounding: The rounded average of your number is:"+ str(Average1_out))
    else:
        print("Your number(s) were: "+ str(Number_List))
        print("You had "+str(Loop)+" number(s)")
        print("The average of your number:"+ str(Average_out))
        print("Bank Rounding: The rounded average of your number is:"+ str(Average2_out))
        print("Half-Up Rounding: The rounded average of your number is:"+ str(Average1_out))
    


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
