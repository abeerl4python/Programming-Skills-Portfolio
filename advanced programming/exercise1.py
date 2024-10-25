import random

def Menu(): # To display the difficulty level 
    print("DIFFICULTY LEVEL")
    print(" 1. EASY")
    print(" 2. MODERATE")
    print(" 3. ADVANCED")

def randomNumber(difficultylevel): # Creating randomnumber function with variable(difficultylevel)
    # Generating random number based on difficulty level 
    if difficultylevel == 1:    
        return random.randint(1, 9)  # Easy: single digit numbers
    elif difficultylevel == 2:
        return random.randint(10, 99)  # Moderate: double digit numbers
    elif difficultylevel == 3:
        return random.randint(1000, 9999)  # Advanced: 4-digit numbers

def decideOperation(): # For deciding random operation
    return random.choice(['+', '-']) # Using choice() function exclusive in randomlibrary for deciding the operation

def displayProblem(num1, num2, operation): # Creating a function with variables num1 num2 and operation
    return int(input(f"{num1} {operation} {num2} = ")) #Displays and returns the answer of the user

def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer: #Using if and else statement for telling the user about their answer
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False

def displayResults(score): # To display the final score and rank based on the performance
    print(f"\nYour final score: {score}/100") # displays the final score to the user
    
    if score >= 90:
        print("Rank: A+")
    elif score >= 80:
        print("Rank: A")
    elif score >= 70:
        print("Rank: B")
    elif score >= 60:
        print("Rank: C")
    else:
        print("Rank: D")

def quiz(): #for conducting the quiz 
    Menu()  #calling the menu() function
    
    # Get difficulty level from user
    difficultylevel = int(input("Select difficulty level (1-3): "))
    while difficultylevel not in [1, 2, 3]:
        print("Invalid choice. Please select 1, 2, or 3.")
        difficultylevel = int(input("Select difficulty level (1-3): "))

    score = 0
    
    for _ in range(10):
        num1 = randomNumber(difficultylevel) # Calls the randomNumber() function to generate the 1st number
        num2 = randomNumber(difficultylevel) # Calls the randomNumber() function to generate the 2nd number
        operation = decideOperation() # Calls the operation() function to generate rsndom operation

        # Calculate correct answer based on operation
        correct_answer = num1 + num2 if operation == '+' else num1 - num2
        
        #Using if and else statement to calculate the score
        # First attempt
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(user_answer, correct_answer):
            score += 10
        else:
            # Second attempt
            print("Try again!")
            user_answer = displayProblem(num1, num2, operation)
            if isCorrect(user_answer, correct_answer):
                score += 5

    displayResults(score) # displays the score

def main(): # loop and play the quiz if the user wants to play again
    play_again = 'yes'
    while play_again.lower() == 'yes':
        quiz()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()