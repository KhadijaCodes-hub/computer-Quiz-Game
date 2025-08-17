print("Welcome to Computer Quiz!")

# Ask user if he/she wants to play the game
playing = input("Do you want to play? (yes / no) ").lower().strip()
if playing != "yes":
    quit()    # Quit the game if user does not want to play
print("Okay! Let's Play :)")

score=0

# Question = 1
answer = input('What does CPU stands for? ').lower().strip()
if answer=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")  

# Question = 2
answer = input('What does GPU stands for? ').lower().strip()
if answer=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 

# Question = 3
answer = input('What does RAM stands for? ').lower().strip()
if answer=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 

# Question = 4
answer = input('What does ROM stands for? ').lower().strip()
if answer=="read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")   

# Display the score and percentage of the user 
print(f"You got {score} questions correct!")   
print(f"You got {(score/4)*100}%") 