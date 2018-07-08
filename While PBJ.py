# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

##bread = input("How many slices of bread do you have?")
##pbutter = input("How many servings of peanut butter do you have?")
##jelly = input("How many servings of jelly to you have?")
##sandwich = min(bread/2, pbutter, jelly)
##sandwich_number = 1
##
##while bread >= 2 and pbutter >= 1 and jelly >= 1:
##    print "I am making sandwich #{0}.".format(sandwich_number)
##    bread = bread - 2
##    pbutter = pbutter - 1
##    jelly = jelly - 1
##    sandwich_number = sandwich_number + 1

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = input("How many slices of bread do you have?")
pbutter = input("How many servings of peanut butter do you have?")
jelly = input("How many servings of jelly to you have?")
sandwich = min(bread/2, pbutter, jelly)
sandwich_number = 1

while bread >= 4 and pbutter >= 2 and jelly >= 2:
    print "Making sandwich #{0}.".format(sandwich_number)
    print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format((bread/2)-1, pbutter-1, jelly-1)
    bread = bread - 2
    pbutter = pbutter - 1
    jelly = jelly - 1
    sandwich_number = sandwich_number + 1

    if bread <= 3 or pbutter <= 1 or jelly <= 1:
        print "Making sandwich #{0}.".format(sandwich_number)
        bread = bread - 2
        pbutter = pbutter - 1
        jelly = jelly - 1
        sandwich_number = sandwich_number + 1

    if bread <= 1:
        print "All done; I ran out of bread."

    if pbutter <= 1:
        print "All done; I ran out of peanut butter."

    if jelly <= 1:
        print "All done; I ran out of jelly."

