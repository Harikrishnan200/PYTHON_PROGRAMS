import random

def winner(c_winCount,u_winCount,user_score): #This function is used to print the total points and find the winner of the game

    print("POINTS: \n")
    print(user_score[0] +": "+str(u_winCount))
    print("Computer :"+str(c_winCount))

    if c_winCount == u_winCount :
        print("\nThe game is tie !!")

    elif c_winCount > u_winCount:
        print("\nComputer Win....") 

    else:
        print("\n")
        print(user_score[0]+" Wins....")       
    print()

def RockPaperScissor(user,comp,user_score,comp_score): #This function is used to print the winner of each phase
                                                        #user is a variable which contain the user choice
                                                        #comp is a variable which contain the comp choice
    
    
    if user == comp:
        print("Tie!")
        user_score.append("Tie!")             #result of each phase is stored in both list to find the winner
        comp_score.append("Tie")
    elif (user == "Paper" and comp == "Rock") or (user == "Rock" and comp == "Scissor") or (user == "Scissor" and comp == "Paper"):
        print()
        print(user_score[0]+" Wins")
        user_score.append("Win")              #result of each phase is stored in both list to find the winner
        comp_score.append("Fail")
        
    else:
        print("\nComputer Wins")
        user_score.append("Fail") 
        comp_score.append("Win")   

           
    print("\nUser:"+user ,"computer:"+comp)     #print the result of each phase
    print()

def displayScoreBoard(user_score,comp_score,chance):
    u_winCount = 0   # variable used to count the total no. of wins in list user_score
    c_winCount = 0   # variable used to count the total no. of wins in list comp_score
    
    for x in range(1,6):   
        chance.append(x)
    
    print("SCORE BOARD:\n")
    for i in range(6):  # loop used to print the score board
        
        
       
        if i == 0:
            print(f'{chance[i]} | {comp_score[i]} | {user_score[i]}')
            print("__________________")

        else:
            print(f'{chance[i]}    | {comp_score[i]} | {user_score[i]}')
            print()  

    for i in range(1,6):
        if comp_score[i] == "Win":
            c_winCount = c_winCount+1
        if user_score[i] == "Win":
            u_winCount = u_winCount+1
    
    winner(c_winCount,u_winCount,user_score)                

    
def main():
    name = input("\nEnter player name:")
    print("Instruction: There are total 5 chances and whoever gets the highest score will win.")
    n = 0
    rps_list = ["Rock","Paper","Scissor"]
    user_score = [name]     #user_score is a list used to store the user score and the first item of list is assigned with player name for the printing the name on score board
    comp_score = ["Comp"]   #comp_score is a list used to store the computer score the first item of list is assigned with "comp" for printing that name on score board
    chance = ["Numb"]       #chance is a list used to count the no. of chance
    while n !=5 :
        comp_choice = random.choice(rps_list)
        print("1.Rock \n2.Paper \n3.Scissor \n4.Exit")
        user_input = int(input("\nEnter your choice:"))
        user_choice = rps_list[user_input-1]
        RockPaperScissor(user_choice,comp_choice,user_score,comp_score)
        n +=1
    else:
        displayScoreBoard(user_score,comp_score,chance)

if __name__=="__main__":  #call the main function
    main()

    

