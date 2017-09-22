'''
multi line comments
comments
comment again
'''

from itertools import izip

games = ['starcraft', 'counter-strike', 'dota', 'pubg',]

# print games

#INDENTATIONS MATTER!!!
for game in games:
  print 'I love ' + str(game.title()) + '!'

grid = [[1,2,3], [4,5,6], [7,8,9]]

#nested for loop
for row in grid:
  for item in row:
    print item

#range to make a list of numbers => NOT inclusive
for num in range(1, 5):
  print num

#range(start, end, skip)
nums = list(range(1, 10, 3))
print nums

squares = []
for num in range(1, 11):
  squares.append(num ** 2)
print squares

#LIST COMPHREHENSION
#expression, passed into the for loop
shorterSquares = [val ** 2 for val in range(1, 11)]
print shorterSquares

#min, max, sum
print min(squares)  #1
print max(squares)  #100
print sum(squares)  #385

#slice([start], end), NOT inclusive, does not mutate original list
#if no start argument, start at the beginning
#if no end argument, slice until the end
print squares[0 : 3]

#COPY A LIST using slice
copySquares = squares[:]
print copySquares

#python equality checks values!
print squares == copySquares


#TUPLES (simple data structure)
#uses parens, isntead of square brackets
#CANNOT REASSIGN VALUES OF A TUPLE, but can overwrite the tuple variable with a new tuple
#can iterate thru the tuple, just like a list
myTuple = (5, 10)
print myTuple

#myTuple[0] = 2   # returns error!

for num in squares:
    if num % 2 == 0:
        print num
    else:
        print str(num) + ' is not even'
