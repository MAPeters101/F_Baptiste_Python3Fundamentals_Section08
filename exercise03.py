'''
Question 3
In this example, suppose you have a grade book designed as follows:

grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}
This grade book is a dictionary that consists of the student's name as the key,
and the value is a list representing results for a series of tests, from most
recent to oldest.

A new exam has just been graded, and you receive the grades for that specific

exam also as a dictionary:

exam = {
    'Eric': 99,
    'John': 100
}
Write code that updates the grades dictionary by adding the latest test result
to the beginning of each list corresponding to the student.

If the new exam grade is missing for a student, assign the value None as the
latest grade in the grades dictionary.

For the data given above, your grades dictionary should now contain the
following information:

{
    'John': [100, 90, 95, 98],
    'Eric': [99, 86, 84, 92],
    'Michael': [None, 90, 89, 85]
}
'''