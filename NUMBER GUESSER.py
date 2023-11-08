import random
flag=0
game=1
i=0
while(game==1):
    numr=random.randint(1,100)
    while(i<5 and flag!=1):
        print("***********************************************************************")
        print("Guess the number!\nBetween range 1 to 100\n")
        numu=int(input(">"))
        if(numu<numr and numu>0 and i!=4):
            print("\nYour Number is LOWER than the expected number!")
            print("\n")
            print("HINT NO ",(i+1))
            if(numr%2==0):
                print("It is a divisible of 2")
            elif(numr%3==0):
                print("It is divisible by 3")
                print("\n")
            elif(numr%5==0):
                print("It is divisible by 5")
                print("\n")
        elif(numu>numr and numu<100 and i!=4):
            print("Your Number is HIGHER than the expected number!")
            print("HINT NO ",(i+1))
            if(numr%2==0):
                print("It is a divisible of 2")
            elif(numr%3==0):
                print("It is divisible by 3")
            print("\n")
        elif(numu==numr):
            print("*********YOU WON !!!***********")
            flag=1
            pass
        elif(i!=4):
            print("Watch Out for your ans!... You lost your 1 chance")
        if(i!=4 and flag!=1):
            print("YOU HAVE",(4-i),"CHANCE LEFT !")
            print("\n")
        i+=1
    if(flag!=1):
        print("YOU LOST ! TRY AGAIN NEXT TIME :) ")
        print("The Number was ",numr)
        print("\n")
    
    print("To PLAY AGAIN type 1\nIf you want to QUIT then type 0")
    flag=0
    game=1
    i=0
    game=int(input())