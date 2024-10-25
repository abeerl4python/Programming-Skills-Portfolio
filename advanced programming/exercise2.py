import random # Importing randon to select a random joke

# Updated joke dataset
jokes = [
    "Why did the chicken cross the road?To get to the other side.",
    "What happens if you boil a clown?You get a laughing stock.",
    "Why did the car get a flat tire?Because there was a fork in the road!",
    "How did the hipster burn his mouth?He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet?SUPPLIES!!!!",
    "Why does the golfer wear two pants?Because he's afraid he might get a 'Hole-in-one.'",
    "What did the buffalo say when his kid went to college?Bison.",
    "Why shouldn't you tell secrets in a cornfield?Too many ears.",
    "Why did the donut go to the dentist?To get a filling.",
    "Why don't scientists trust Atoms?They make up everything."
]

def joke():
    while True:
        # Select a random joke
        joke = random.choice(jokes)
        # Split setup and punchline
        setup, punchline = joke.split('?') # using '?' as a variable to split the joke and punchline
        
        # Displays jokeline 
        print(f"Setup: {setup}?") # Displays the setupline ny using the f-string
        input("Press Enter to see the punchline...") 
        # Display punchline
        print(f"Punchline: {punchline}") 
        
        # Ask if the user wants another joke
        another = input("\nWould you like to hear another joke? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

# Main program loop
if __name__ == "__main__":
    print("Welcome! Ask 'Alexa tell me a joke' to get started.")
    while True:
        command = input("Enter your command: ").strip().lower()
        if command == "alexa tell me a joke":
            joke()
        else:
            print("Unknown command. Please try again.")