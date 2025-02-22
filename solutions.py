"""
Question 1
Use a dictionary to count the frequency of the characters a-z A-Z in a given string.

You should write your code to be as general as possible, so that it will work with any string of any given length.

Your resulting dictionary should only contain keys for characters that occured at least once (i.e. no zero count characters should be present.)

Hint: you will probably want to use the ord() function that we studied earlier along with the unicode character codes for a, z, A and Z.

For example, if the given string is:

s = 'Aa, Bb - A a B C'
then your resulting dictionary should be:

{
    'A': 2,
    'a': 2,
    'B': 2,
    'b': 1,
    'C': 1
}
(Note that the order of the keys in the dictionary is not important)

Here are two sample strings you can use:

s1 = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation
of negation) they are a complete set of basic logical operations — all other logical
operations, no matter how complex, can be obtained by suitable combinations of these.”
― John von Neumann, The Computer and the Brain
"""

s2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.
"""
Solution
We only want to consider the characters a-z and A-Z.

We know that the unicode codepoints for each of these character ranges are consecutive:

ord('a'), ord('z')
(97, 122)
ord('A'), ord('Z')
(65, 90)
So when we iterate through each character in our string, we'll ignore any characters that do not fall within those ranges.

We'll use a dictionary to keep track of the count of characters as we iterate through the string.

We'll start with an empty dictionary, and as we encounter a character we'll either update the count (the value associated with the key) if the key is present, or insert it with a count of 1.

counts = {}
for c in s1:
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        counts[c] = counts.get(c, 0) + 1
        
counts
{'A': 1,
 'n': 20,
 'd': 4,
 'a': 23,
 'o': 31,
 'r': 12,
 'e': 27,
 't': 21,
 'h': 11,
 'b': 7,
 's': 9,
 'i': 17,
 'c': 10,
 'p': 7,
 'f': 4,
 'l': 12,
 'g': 6,
 'T': 2,
 'w': 2,
 'y': 2,
 'm': 6,
 'x': 1,
 'u': 3,
 'J': 1,
 'v': 1,
 'N': 1,
 'C': 1,
 'B': 1}
Note how we used counts.get(c, 0) to assign a default count for the key c and then added 1 to it in all cases.

If c was present in the dictionary, counts.get(c, 0) would return the value (the frequency count) and we add 1 to that.

If c was not present in the dictionary, counts.get(c, 0) would return 0 and adding 1 to that we end up inserting a new key (c) into the dictionary with a value of 1.

The same code works for s2 as well:

counts = {}
for c in s2:
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        counts[c] = counts.get(c, 0) + 1
        
counts
{'L': 1,
 'o': 29,
 'r': 22,
 'e': 37,
 'm': 17,
 'i': 42,
 'p': 11,
 's': 18,
 'u': 28,
 'd': 18,
 'l': 21,
 't': 32,
 'a': 29,
 'c': 16,
 'n': 24,
 'g': 3,
 'b': 3,
 'q': 5,
 'U': 1,
 'v': 3,
 'x': 3,
 'D': 1,
 'h': 1,
 'f': 3,
 'E': 1}
Question 2
Given the following dictionaries:

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}
Construct two lists, one containing all the keys of both dictionaries, and one containing all the values of each dictionary. (It is OK for values or keys to be repeated in the lists).

In the example above you should end up with two lists containing the elements:

'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g'
and

10, 20, 30, 100, 200, 300, 30, 40
Note that the order in which the elements appear in each list is not important.

Solution
Here I'll present two approaches (there are probably more!) that I took to get the solution.

In the first approach I will create two empty lists, one for the keys and one for the values:

keys = []
values = []
Next, I'll iterate over all the dictionaries, for each one iterating over the key/value pairs, and simply append the key/value to the appropriate list:

for d in (d1, d2, d3):
    for key, value in d.items():
        keys.append(key)
        values.append(value)
keys
['a', 'b', 'c', 'd', 'e', 'f', 'f', 'g']
values
[10, 20, 30, 100, 200, 300, 30, 40]
So this solution works fine, but in Python we usuallt try not to use loops to iteratively append to lists, as there are often better techniques.

In my second approach, I'll use the fact that we can recover a list of keys and values from a dictionary by using the keys() and values() methods:

list(d1.keys())
['a', 'b', 'c']
list(d1.values())
[10, 20, 30]
So, I'll start with my lists of keys and values set to the keys and values of the first dictionary:

keys = list(d1.keys())
values = list(d1.values())
keys
['a', 'b', 'c']
values
[10, 20, 30]
Next, I'll iterate over the remaining dictionaries, and extend the keys and values lists:

for d in (d2, d3):
    keys.extend(d.keys())
    values.extend(d.values())
keys
['a', 'b', 'c', 'd', 'e', 'f', 'f', 'g']
values
[10, 20, 30, 100, 200, 300, 30, 40]
There is actually a third way we could do this, but the code is a bit repetitive, and could get unwieldy if we were trying to do this for a large number of dictionaries. That may be fine in certain situations though, so let's see how we could do it.

list(d1.keys()) + list(d2.keys()) + list(d3.keys())
['a', 'b', 'c', 'd', 'e', 'f', 'f', 'g']
list(d1.values()) + list(d2.values()) + list(d3.values())
[10, 20, 30, 100, 200, 300, 30, 40]
This approach works fine too, but as you can see our code would become very repetitive if we had many dictionaries to deal with.

Question 3
In this example, suppose you have a grade book designed as follows:

grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}
This grade book is a dictionary that consists of the student's name as the key, and the value is a list representing results for a series of tests, from most recent to oldest.

A new exam has just been graded, and you receive the grades for that specific exam also as a dictionary:

exam = {
    'Eric': 99,
    'John': 100
}
Write code that updates the grades dictionary by adding the latest test result to the beginning of each list corresponding to the student.

If the new exam grade is missing for a student, assign the value None as the latest grade in the grades dictionary.

For the data given above, your grades dictionary should now contain the following information:

{
    'John': [100, 90, 95, 98],
    'Eric': [99, 86, 84, 92],
    'Michael': [None, 90, 89, 85]
}
Solution
We need to mutate the dictionary grades by inserting, as the first element, the latest grade obtained by the student as given in exam.

We can iterate over the keys of the grades dictionary, and retrieve the grade from the exam dictionary - substituting None if no grade was found. Then, we need to insert that grade as the first element of the corresponding grade list.

for student in grades:
    if student in exam:
        grades[student].insert(0, exam[student])
    else:
        grades[student].insert(0, None)
        
grades
{'John': [100, 90, 95, 98],
 'Eric': [99, 86, 84, 92],
 'Michael': [None, 90, 89, 85]}
So this solution works, but we really don't need to use that if...else... statement, since we can use the get() method on dictionaries, which will, by default, return None if the key is not found:

print(exam.get('Michael'))
None
Let's reset the grades dictionary to its original state first:

grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}
And now let's use the get() method:

for student in grades:
    grades[student].insert(0, exam.get(student))
    
grades
{'John': [100, 90, 95, 98],
 'Eric': [99, 86, 84, 92],
 'Michael': [None, 90, 89, 85]}
"""