

# Q 1:
"""
Define a function named 'sum_of_list'.
It will take a list as parameter and calculate the sum of numbers in this list.

If it encounters an error during summation, it will raise an Exception.
Otherwise, it will return the summation.

The exception type will be 'TypeError' and the text will be the standard error text.

Hints:
* try-except
* except .... as ....
"""


# Q 1:

# ---- your solution here ---

# call the function you defined
print(sum_of_list([1, 'b', 3]))
# print(sum_of_list([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Q 2:
"""
Below, you see a function named "total_likes".
This function creates a dictionary of reviews.
And it returns total number of likes in this dictionary.

But there is a problem.
If you run the function as it is currently, you will see it raises an exception.

Fix this bug in the function by using try-except-else structure.

Hints:
* examine each review carefully :)


def total_likes():
    reviews = [{'Image': 4, 'Like': 20, 'Comment': 12},
               {'Like': 15, 'Comment': 8, 'Share': 10},
               {'Image': 7, 'Comment': 16, 'Share': 37},
               {'Image': 6, 'Like': 10, 'Comment': 9}]

    total = 0

    for review in reviews:
        total += review['Like']

    return total

total_number_of_likes = total_likes()
print(total_number_of_likes)
"""

# Q 2:

# ---- your solution here ---

# call the function you defined
total_number_of_likes = total_likes()
print(total_number_of_likes)

# --------------------------------------------------------------------------------------#

# Q 3:
"""
Define a function named 'give_me_a_key'.
It will ask for the user to press any key on the keyboard.
If the key that the user pressed is:
1- a number -> return its square
2- a letter -> return its capital form
3- neither a number nor a letter -> return the key itself

Define this function by using try-except-else-finally structure.
"""


# Q 3:

# ---- your solution here ---

# call the function you defined
give_me_a_key()

# --------------------------------------------------------------------------------------#

# Q 4:
"""
Define a function named 'item_at_index'.
It will take a list and an index as parameters.
It will search for the item at this index in the list.
If it doesn't find the item, it will raise a standard exception.
If it finds, it will return the result.

Hints:
* try-except-else
* raise only (no exception type declaration)
"""


# Q 4:

# ---- your solution here ---

# call the function you defined
my_list = ['x', 'y', 'z', 't']
ind = 7
result = item_at_index(my_list, ind)
print(result)

# --------------------------------------------------------------------------------------#
