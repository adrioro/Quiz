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


# The 3 level choices:
level_list= ["easy", "medium", "difficult"]

level=raw_input ("Pick a level by typing easy, medium, or difficult.\n")


# Defining the corresponding quiz list of correct answers.

def quiz_answer_list ():
    if level == "easy":
        return quiz1_answers
    if level == "medium":
        return quiz2_answers
    else:
        if level == "difficult":
          return quiz3_answers


# User enters the answer, determines the result and plays again when possible.

def user_enter_answer():
    count = 0
    while count <4:
        users_input = raw_input ("Enter you answer for #1.\n")
        list= quiz_answer_list ()
        correct_answer = list[0] 
        total_trials = 3 
        while users_input != correct_answer: # To address mispeling errors.
           count = count + 1 # To add trial attempts to the count.
           trials_left = total_trials - count   
           if count <=2:              
              print "Wrong spelling. Please try again. You have " + str(trials_left) + " remaining."
              break
           else:
              print "Game over.Thank you for playing!"
              break
                    
        while users_input == correct_answer: 
            print "Correct answer"
            count = 5 # To avoid going back to the beginning of the function. 
            return "Return next function here" # here I'll enter new function" # Change when new action is ready.
                   

    
# _________________________________________________
           
def print_quiz():
   if level == "easy": 
      print quiz1
      user_enter_answer()
      
   if level == "medium": 
      print quiz2
      user_enter_answer()
      
   if level=="difficult": 
      print quiz3
      user_enter_answer()

   else:
        return "\n"
        
      

def if_wrong_level(): 
   level=raw_input ("Try again. Pick a level by typing easy, medium, or difficult.\n")   
   while level in level_list:   
      if level == "easy":            
         print "You chose the EASY level.\n" + quiz1
         break 
      else:                
         if level == "medium":
            print "You chose the MEDIUM level\n."+ quiz2
            break   
         else:
            if level == "difficult":
               print "You chose the DIFFICULT level."+ quiz3
               break
               print_quiz()  
   else:
               print "Your choice is. " + level+ " Wrong Answer! Game Over"
               return

def start_quiz():
   print "Your choice is, LEVEL: " + level
   if level not in level_list:
      print "Wrong spelling. You have one trial remaining."
      if_wrong_level()
      return "\n"
   else:
      print "Please, fill in the blanks in the order presented."
      print_quiz()
      return "\n"
      
      
      

print start_quiz()

    
    
    
    
        
    