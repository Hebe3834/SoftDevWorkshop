# Hebe Huang
# SoftDev
# Program To Print A Random SoftDev Student's Name
# 2021-09-27                                           

# SUMMARY OF DISCUSSION:
# We discussed about Hebe's code with importing Github into Python with PyGithub.
# We soon found out that there were many issues involving the API and installing
# it properly, so we gave up on that route and decided to refactor Andrew and Justin's
# code. Given two txt files of the names of students separated by period, we can create
# a dictionary and print out a random student.

# DISCOVERIES:
# random has a choice method which randomly selects an element from a sequence.
# dict.values() returns a list of the values from each key in the given dictionary

# QUESTIONS:
# How do we create lists of names separated by period without having to do it
# manually?

# COMMENTS:
# To improve maintainability, we can create a function that handles the file input,
# so we don't have open, read, and splitline every single time.
#
# The dictionary does not seem to be the best datastructure given the the amount of
# data we have, but for larger amounts of data the dictionary would be effective at
# accessing the list you want.
#
# We can do research into how to fetch the Github API, so we don't have to create
# lists of students by hand.

import random

# Open/Read Files
f1 = open("period1.txt", "r")
f2 = open("period2.txt", "r")
period1 = f1.read();
period2 = f2.read();

def main():
    # Split each file into a list separated by "\n"
    pd1_students = period1.splitlines()
    pd2_students = period2.splitlines()

    # Declaration of the dictionary
    STUDENTS = {
                "Period 1": pd1_students,
                "Period 2": pd2_students,
    }

    #print(STUDENTS)

    # Randomly select a key from the dictionary
    period = random.choice(list(STUDENTS.values()))

    # Randomly select a person from that random period
    rand_person = random.choice(period)

    print(rand_person)

main()
