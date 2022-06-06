#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on June 2022
# This is a program that finds the average of numbers in an array

import random


def number_average(everyMark):
    # this function find the average
    
    the_average = 0
    for singleMark in everyMark:
        the_average = singleMark + the_average
    the_average = the_average / len(everyMark)

    return the_average


def main():
    # this function gets the marks

    marks = []

    # input
    mark = int(input("What is your Mark? (as %): "))
    marks.append(mark)
    while mark != -1:
        while mark > 100 or mark < -1:
            marks.pop()
            mark = int(input("Invalid Mark! What Is Your Mark? (as %): "))
            marks.append(mark)
        mark = int(input("What is your Mark? (as %): "))
        marks.append(mark)
    marks.pop()
    print("")

    average = number_average(marks)
    print("The average is: {0}%.".format(average))


if __name__ == "__main__":
    main()
