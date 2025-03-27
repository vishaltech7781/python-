import random

def game():
    print ("print u r playing a game :")
    score = random.randint(1,100)

    #now fetch thw highscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!= ""):
            highscore= int(highscore)
        else:
            highscore= 0 

    print(f"your score is :{score}")
    if(score>highscore):
        #write the highscore to the file 
        with open("highscore.txt","w")as f:
            f.write(str(score))


game()