# import module
import os
import random
import time
os.system('cls||clear')

# print welcome
print(" Welcome to Find Missing Word!!\n")
print("-> Your goal is to find missing the word in each sentence. ")
print("   Choose the correct word in the list.")
print("   When playing the game you will be able to have a streak and you will recevie hints.")
print("   Have fun practicing!!! \n")

# ask the user name
user_name = input(" What is your name? \n Enter your name:").strip().lower()


ready = input(f"Hey {user_name}, are you ready for pratice? (y/n): ").strip().lower()

if ready != "y":
    print("Okay! see you next time!")
    time.sleep(1.5)
    os.system('cls||clear')

print(" Let's try to do some sentences for practing!")


#Easy part
# make lists the words for each level: Easy, Medium, Hard
E_words = ["chopsticks", "sat", "eating","lost","everyday","tricks","come","programmer","fishing","crescent"]

# make a list for easy sentences.
E_sentences = ["He eats rice with __________.",
               "The cat ___ in the chair.",
               "She was ______ and talking.",
               "I ____ my watch yesterday.",
               "He does not go to the gym ________.",
               "You don't teach your cat ______.",
               "No one will ____ after me.",
               "I want to be a computer __________.",
               "We went _______ after school.",
               "The moon looks like a ________."]

# make a dictionary for the answer
E_answers = {
    E_sentences[0]:"chopsticks",
    E_sentences[1]:"sat",
    E_sentences[2]:"eating",
    E_sentences[3]:"lost",
    E_sentences[4]:"everyday",
    E_sentences[5]:"tricks",
    E_sentences[6]:"come",
    E_sentences[7]:"programmer",
    E_sentences[8]:"fishing",
    E_sentences[9]:"crescent"
    }

# Medium part
M_words = ["docked","managed","passionate","barn","discuss","should","fascinating","afraid","mentioning","umbrella"] 

M_sentences = ["If he was late again, he would be ______ a day's pay.",
               "Even though she was late, she still _______ to finish her work.",
               "While I am a __________ basketball fan, but I prefer soccer.",
               "The horse raced past the ____.",
               "Let's schedule a meeting to _______ the project details.",
               "It was nice to talking to you; we ______ do this again.",
               "The teacher, who is known for being strict, gave a ___________ lecture.",
               "I'm ______ I cannot attend the meeting on Friday.",
               "Speak of the devil, we were just __________ your recent promotion.",
               "It's going to rain this afternoon, so we should bring an ________."]

M_answers = {
    M_sentences[0]:"docked",
    M_sentences[1]:"managed",
    M_sentences[2]:"passionate",
    M_sentences[3]:"barn",
    M_sentences[4]:"discuss",
    M_sentences[5]:"should",
    M_sentences[6]:"fascinating",
    M_sentences[7]:"afraid",
    M_sentences[8]:"mentioning",
    M_sentences[9]:"umbrella"
}


# hard part
H_words = ["untangling","ambiguous","meticulous","reluctant","comprehensive","resilient","groundbreaking","arrogant","intricate","profound"]

H_sentences = ["The electrical wires require a lot of __________.",
               "The politician's speech was full of _________ statements that confused the audience.",
               "Her __________ attention to detail made the project nearly perfect.",
               "His _________ agreement showed that he wasn't fully convinced.",
               "The teacher gave a _____________ explanation of the complex topic.",
               "She was known for her _________ attitude, never giving up despite challenges.",
               "The scientist made a ______________ discovery that changed modern medicine.",
               "His ________ behavior made it difficult for others to work with him.",
               "The instructions were so _________ that many people struggled to follow them.",
               "The novel presents a ________ message about life and human nature."]

H_answers = {
    H_sentences[0]:"untangling",
    H_sentences[1]:"ambiguous",
    H_sentences[2]:"meticulous",
    H_sentences[3]:"reluctant",
    H_sentences[4]:"comprehensive",
    H_sentences[5]:"resilient",
    H_sentences[6]:"groundbreaking",
    H_sentences[7]:"arrogant",
    H_sentences[8]:"intricate",
    H_sentences[9]:"profound",
}

# Use function to run the game
def play_game(level):
# loop to run the whole game 
    score = 0
    streak = 0
    max_attempts = 2
    attempts = 0

    while True: 
        # loop for select level
        while True:
            if level == "easy":
                words = E_words
                sentences = E_sentences
                answers = E_answers
                break

            elif level == "medium":
                words = M_words
                sentences = M_sentences
                answers = M_answers
                break

            elif level == "hard":
                words = H_words
                sentences = H_sentences
                answers = H_answers
                break 
            else:
                print(" Invalid level!")

        sentence = random.choice(sentences)
        correct = answers[sentence]

        print("Word list:",words)
        print("\nHere is the sentence: ")
        print(sentence)

        user = input("Fill the blank of the answer: ").strip().lower()

        if user == correct:
            score += 1
            streak += 1
            attempts = 0
            print(f"Yes, you got it {user_name}!!!")
            print(" Your score is:",score)
            print(" Your streak is:", streak)

            # # time.sleep(1.5)
            # os.system('cls||clear')
        else:
            score -= 1 
            attempts += 1
            streak = 0
            
            print(" You're wrong, but it's okay!")
            # print("Correct answer was", correct)
            # time.sleep(1.5)
            # os.system('cls||clear')


        # ask the user for hints. 
            use_hint = input("Do you want to use a hint? (yes/ no ): ").strip().lower()
        
            if use_hint == "yes":
                print("Hint: The words starts with",correct[0] )

                user = input(" Let's try again: ").strip().lower()



        #second chance if they get right
                if user == correct:
                    score +=1
                    streak +=1
                    attempts =0
                    print(" Yes, you got it right this time!!!")
                else:
                    attempts +=1
                print(" Oh no, still wrong.")
            
        # show the answer if final answer is wrong
        if user != correct:
            print("\n The correct answer was", correct)


        if attempts >= max_attempts:
            streak = 0
            attempts = 0
            print(" You got it wrong! Your streak has been reset.")
                    
        # print all the current score and streak when they use max attempts. 
        print("\n>> Your current score is:", score)
        print(" >> Your current streak is:", streak)


# ask the user want to play again
        more = input("Do you want another sentence?(yes/no): ").strip().lower()
        if more != "yes":
            print("Thanks you for play Find Missing Words.")
            break 
level = input("(easy, medium, hard) Let's choose level you want to select: ").strip().lower()
play_game(level)