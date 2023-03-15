#
#
# -----------------------------------Exercise 1a - Getting started with Python
Beskrivning
In most programming languages you are able to write comments in the code which will be ignored by the computer but are useful for us humans. To write a comment you use the hashtag-character #. See the following example:


# This is a comment and will not be executed

Exercise 1a

Go to this web site where you have the online Python interpreter https://repl.it/languages/python3 (might only work on Chrome)
Create your first python application by printing out "Hello world!"
Add a comment to the code explaining that this is your very first Python program.
#
#
# -----------------------------------Exercise 1b - If- and else-statements
Beskrivning
During the lesson we went through how if-else-statements work. Let us write our first Python program which makes use of them.

The if-statement needs a condition to validate (something to check whether it is true or not) but the else-statement should not have anything other than the colon sign. The action that each statement should perform (printing out something) should be indented with either four spaces or a tab.


number_of_volvos = 5
number_of_teslas = 6
if number_of_volvos < number_of_teslas:
    print("You should buy more Volvos!")
else:
    print("You have enough Volvos for now.")

If you run the code above, the if-statement will be true since 5 is less than 6.
However, if you would increase the number of Volvos to 6 or greater, then the if-statement will be false and the it will print out whatever is in the else-statement instead.


Exercise 1b

Write the code above and change the values of number_of_volvos and number_of_teslas so that you on the first run get to print (“You should buy more volvos”) and on the second run print(“You have enough volvos for now”)
#
#
# -----------------------------------Exercise 1c - If- and else-statements
Beskrivning
There is also a third option to the if-else-statements which is called the elif-statement. Please see the following example:


number_of_volvos = 6
number_of_teslas = 6

if number_of_volvos < number_of_teslas:
    print("You should buy more Volvos!")
elif number_of_volvos == number_of_teslas:
    print("You have the same number of Teslas as Volvos")
else:
    print("You have enough Volvos for now.")

The program will first check whether the if-statement is true or not.
If it is false (like it is in this case) it will then check the elif-statement instead.
If the elif-statement is true, we will print whatever is in that section and then finish the program.
However if the elif-statement also is false, we then enter the else-statement.
You can have as many elif-statements as you want and it is optional whether you want to have an else-statement at the end or not.

 

Exercise 1c

Write the code above and change the number_of_volvos and number_of_teslas so it will print out all the three different printouts
#
#
# -----------------------------------Exercise 1d - If- and else-statements
Beskrivning
Exercise 1d (optional)

Go to this page https://www.w3schools.com/python/python_conditions.asp and perform the exercises there
#
#
# -----------------------------------Exercise 1e - Comparison operators
Beskrivning
Exercise 1e - odd number finder (optional)

This exercise is optional and for those who want to learn more comparison operators than what was covered in the lecture.

Create a variable called number in the beginning of your program which is assigned to any number of your choice
Write an if-else-statement which will determine whether the number is odd or even
If it is odd, it should print out "The number is odd!", otherwise it should print out "The number is even!"
You should search the web for finding out how to make Python determine if the number is odd or even (using a search engine is part of the exercise)#
#
# -----------------------------------Exercise 1a - Getting started with Python

#
#
# -----------------------------------Exercise 1a - Getting started with Python