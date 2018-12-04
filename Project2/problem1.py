import random

print("Choose a number in your head between 1 and 10\n")

guess_num=1
nums=list(range(1,11))

index=(len(nums)-1)//2

com_guess=nums[index]

print("The computer guesses: ",com_guess,"\n")

print("If the guess is too large, enter(1)")
print("if the guess is too small, enter (2)")
print("If the guess is correct, enter (3)\n")

compare=int(input("Please enter 1, 2, or 3: \n"))

if (compare==3):
    print("The computer guesses your number!")
else:
    guess_num+=1
    while((compare==1 or compare==2) and guess_num<=3):
        if(guess_num==2):            
            if (compare==1):
                index=(index)//2
                com_guess = nums[index-1]
                print("The computer guesses: ",com_guess,"\n")
                compare=int(input("Please enter 1, 2, or 3: \n"))
            else:
                index=(index//2)
                com_guess= nums[index+1]
                print("The computer guesses: ",com_guess,"\n")
                compare=int(input("Please enter 1, 2, or 3: \n"))
        if(guess_num==3):            
            if (compare==1):
                index=(index//2)
                com_guess = nums[random.randint(0,index-1)]
                print("The computer guesses: ",com_guess,"\n")
                compare=int(input("Please enter 1, 2, or 3: \n"))
            else:
                index=(index//2)
                com_guess= nums[random.randint(index+1,len(nums))]
                print("The computer guesses: ",com_guess,"\n")
                compare=int(input("Please enter 1, 2, or 3: \n"))
        guess_num+=1
    if (compare==3):
        print("The computer guessed your number!")
    else:
        print("The computer could not guess your number!")

