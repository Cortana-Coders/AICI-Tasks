"""
 QUIZ - Modules and Packages
"""
# --------------------------------------------------------------------------------------#

# Q 1:
"""
Define a function named 'random_printer'.
It will import the random module and will print a random number between 100 and 200.

Hints:
* randint()
"""

# Q 1:

#---- your solution here ----

# call the function you defined
random_printer()

# --------------------------------------------------------------------------------------#

# Q 2:
"""
Create a module named 'consonants' in the current project.
Define a function named 'get_consonants' in this module.
This function takes a text as parameter and it will return a set of consonants in this text.
Call this function with a text and print the consonants in this text.

Hints:
* your module should implement its own exception handling

Expected Output:
'Pyton Programming Language.... /@*-'

{'r', 'P', 'L', 'y', 'm', 'n', 't', 'g'}
"""

# Q 6:
#-- create the consonants module first --

# import the module you create
import consonants

text = 'Pyton Programming Language A.... /@*-'
cons = consonants.get_consonants(text)
print(cons)


# --------------------------------------------------------------------------------------#



