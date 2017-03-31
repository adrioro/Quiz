# Defining quizes by game level from easy to difficult.

#Easy:
quiz1 = '''Python is a high-level, interpreted, interactive and object-oriented scripting ___1___. Python is ___2___ to be highly readable. It uses English ___3___ frequently where other languages use ___4___.'''

#Medium:
quiz2 = '''A group of individual ___1___, which make a single code block are called ___2___ in Python. 
Compound or complex statements, such as if, while, def, and class require a ___3___ line and a ___4___.'''

#Difficult:
quiz3 = ''' A ___1___ is a sequence of ___2___ Python objects. They are ___3___, just like lists. 
They cannot be changed unlike lists, and they use parentheses. Lists use square ___4___. '''


# Answers to the quizes
quiz1_answers = ["language", "designed", "keywords", "punctuation"] # List of correct answers.
quiz2_answers = ["statements", "suites", "header", "suite"] # List of correct answers.
quiz3_answers = ["tuple", "inmutable", "sequences", "brackets"] # List of correct answers.

#___________________________________________________________________Part1

# This is the starting function and one at which the user will be returned to if she/he wanted to play again.

def start():
  global level #It'll be used throughout the game.
  print "\nHELLO!!!Welcome to my Quiz!\n\nInstructions:\nThis game consist of three difficulty levels (easy, medium and difficult). Each level requires you to fill-in four blanks. To start the game, you will have to choose the level you would like to complete first. As you complete each level, you will be automatically moved to the next level in the list of hierarchy until you complete all of them satisfactorily.\nGood Luck\n!"
  level = raw_input ("\nPlease select an easy, medium or difficult level.\nEnter your choice here: ") # For the user to enter the level.
  
  return difficulty_level()



# Promping the user to the desired level of dificulty after validating it.

def difficulty_level():

         level_list = ["easy", "medium", "difficult"] # Category options for the user.
         if level not in level_list: # To address mispeling errors.
                print "\nWrong spelling. Sorry." # It communicates the user that the entry was not valid.
                return start() # It gives the user the chance to enter it again if the answer is wrong.             
                
         elif level in level_list:
            print "\nCongratulations! You chose the " + level +" level. You are ready to play!\n" # Once the entry was validated the user is notified.
            return validate_answer() # Goes to next function.     

#___________________________________________________________________Part2


# This function creates a list to use in validate_answer() to print the corresponding quiz with the blanks filled, as it's being completed.
def filled_quizzes ():
    
    str =quiz1.split() # splits the quiz.
    quiz1_a = quiz1.replace ("___1___", "language") # Replaces the word.
    
    str =quiz2.split() 
    quiz1_b = quiz1_a.replace ("___2___", "designed")
    
    str =quiz3.split() 
    quiz1_c = quiz1_b.replace ("___3___", "keyword")
    
    str =quiz3.split() 
    quiz1_d = quiz1_c.replace ("___4___", "punctuation")
        
    list = (quiz1_a, quiz1_b, quiz1_c, quiz1_d ) # I created a list I needed for a future function: validate_answer().
    quiz_list = list
    return quiz_list


# The following function defines right list of answers.

def quiz_answer_list ():
    if level == "easy": # Condition based on the active level.
        print "\nFill in the blanks.\n\n" + quiz1 +"\n" # prompts the user to fill the blank and prints the corresponding quiz.
        return quiz1_answers # Makes accessible the corrresponding answers for the active quiz.
        
        
    if level == "medium":
        print "\nFill in the blanks.\n\n" + quiz2 +"\n"
        return quiz2_answers
        
    else:
        if level == "difficult":
            print "\nFill in the blanks.\n\n" + quiz3 +"\n"
            return quiz3_answers


# This function validates the answers entered.

def validate_answer():
    validate_list = quiz_answer_list()
    print_filled_quiz = filled_quizzes ()
    position_in_list = 0 # this is my base count. Zero corresponds to the first position/item in the list.  
    final_position_list = 3 # This is the position of the last items in the list, the 4th item.
    while True:
        user_input = raw_input ("Enter Answer here: ") # For the user to enter the input.
        while user_input != validate_list[position_in_list]: # Negative conditioning for cases in which the answer is not correct.
         if position_in_list < final_position_list: # Sets top limit of count.
            print "\nWrong spelling. Please try again."  # Communicates the user that the answer entered was wrong.
            break # To stops the loop.
         else:
            return "\nYou exceeded the number of trials. \nGame over.Thank you for playing!\n"  # For when trials have been used.                        
        while user_input == validate_list[position_in_list]: # Conditioning for when the answer is correct.
         if position_in_list < final_position_list: # IF still within the allowed count.
             print "\nCongratulations! Your answer is correct.\n\n" + print_filled_quiz[position_in_list] +"\n\nPlease continue. " #Communicated the user that the answer was right and placed it in the quiz, filling the blanck.
             position_in_list = position_in_list + 1 # To stops the loop.
         else:     
             print "\nCongratulations! Your answer is correct.\n\nYou completed the level!!!PLease continue.\n\n________________________________\n\n"
             return "Todo bien" # Moving to next level.
               
#___________________________________________________________________Part3

# This function moves from one level to another as required, depending on what the active level is.

def next_level():
    level_list = ["easy", "medium", "difficult"] # Category options for the user.
    global level
    if level == level_list[0]: #It uses the place in the list, from 0:easy, to 2:difficult.
        level = level_list[1]
        return validate_answer()
    elif level == level_list[1]:
        level = level_list[2]
        return validate_answer()
    else:
        if level == level_list[2]: #If last level, the game is over.
            print "Congratulations!!! You completed the highest level.\nThe game is over.\n\n" #It communicates to the user that the game is over.
            return play_again()
            
 # This function is to give the user the option of playing again by entering a code.
            
def play_again():
    user_input = raw_input ("To play again enter code 333 here: ")
    if user_input == "333": #If the code entered is right.
        return start() #The game starts over.
    else: # Otherwise.
        print "A wrong code was entered. Try again." # It communicates the user that the entered code was wrong and invites her/him to try again.
        return play_again()
                    
print start() # The game starts here.   



    
    
         
    
