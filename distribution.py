"""
distribution.py
Author: Patrick Daley   
Credit: Classmate and https://developers.google.com/edu/python/sorting

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

text = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "' + text + '" is: ')

#Makes text lowercase
text = text.lower()


list1 = []

for c in string.ascii_lowercase:
    if text.count(c) != 0:
        list1.append(c * text.count(c))


sort = (sorted(list1, key=len, reverse=True))
for a in sort:
    print(a)



"""

a = text.count('a')
b = text.count('b')
c = text.count('c')
d = text.count('d')
e = text.count('e')
f = text.count('f')
g = text.count('g')
h = text.count('h')
i = text.count('i')
j = text.count('j')
k = text.count('k')
l = text.count('l')
m = text.count('m')
n = text.count('n')
o = text.count('o')
p = text.count('p')
q = text.count('q')
r = text.count('r')
s = text.count('s')
t = text.count('t')
u = text.count('u')
v = text.count('v')
w = text.count('w')
x = text.count('x')
y = text.count('y')
z = text.count('z')


if a >= 1:
    print(a*'a')
if b >= 1:
    print(b*'b')
if c >= 1:
    print(c*'c')
if d >= 1:
    print(d*'d')
if e >= 1:
    print(e*'e')
if f >= 1:
    print(f*'f')
if g >= 1:
    print(g*'g')
if h >= 1:
    print(h*'h')
if i >= 1:
    print(i*'i')
if j >= 1:
    print(j*'j')
if k >= 1:
    print(k*'k')
if l >= 1:
    print(l*'l')
if m >= 1:
    print(m*'m')
if n >= 1:
    print(n*'n')
if o >= 1:
    print(o*'o')
if p >= 1:
    print(p*'p')
if q >= 1:
    print(q*'q')
if r >= 1:
    print(r*'r')
if s >= 1:
    print(s*'s')
if t >= 1:
    print(t*'t')
if u >= 1:
    print(u*'u')
if v >= 1:
    print(v*'v')
if w >= 1:
    print(w*'w')
if x >= 1:
    print(x*'x')
if y >= 1:
    print(y*'y')
if z >= 1:
    print(z*'z')
else:
    print('')

"""









