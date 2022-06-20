import random
comp = print("Computer's Turn : Stone(st), Paper(pa) or Scissor(sc) : Computer Has Chosen")
you = input("Your Turn : Stone(st), Paper(pa), Scissor(sc) : ")
a = random.randint(1,3)
if (a==1):
    comp = 'st'
    print("Computer chose stone.")
elif (a==2):
    comp = 'pa'
    print("Computer chose paper.")
elif (a==3):
    comp = 'sc'
    print("Computer chose scissor.")

if(you=='st'):
    print("You chose stone.")
elif(you=='pa'):
    print("You chose paper.")
elif(you=='sc'):
    print("You chose Scissor.")
def game(comp, you):
    if(comp==you):
        return None
    if(comp=='st' and you=='pa'):
        return True
    elif(comp=='st' and you=='sc'):
        return False
    elif(comp=='pa' and you=='sc'):
        return True
    elif(comp=='pa' and you=='st'):
        return False
    if(comp=='sc' and you=='pa'):
        return False
    elif(comp=='sc' and you=='st'):
        return True
x = game(comp, you)
if (x==None):
    print("It's a Tie.")
elif(x==True):
    print("Congrats! You Win.")
elif(x==False):
    print("Alas! You Lose.")