#lists are dynamic

beers = ['ipa', 'porter', 'stouts', 'sours', 'pale ales', 'lagers']

print beers

#last element in the list
#applies to all negative index, last n item
print beers[-1]

beers.append('strong ales')
# print beers

#insert only handles EXACTLY 2 arguments, index and item
#shifts all other elements on the right
beers.insert(3, 'double ipas')
# print beers

#del to remove items at index, works with negative index
#del is used if you DONT want to work with the deleted element
del beers[0]
# print beers

#can pop from any index of the list, not just the last value
#use pop if you want to use the popped off element
lastBeer = beers.pop(3)
# print lastBeer
# print beers

#len method to check length
print len(beers)

#reverse method changes list permanently
print beers
beers.reverse()
print beers

#IMPORTANT: sorting in python only works consistently in lowercase!

#remove is used for VALUE in a list
#removes only the first occurance in the list
beers.remove('pale ales')
# print beers

#sorted is temp
# print 'sorted temporarily: ' + str(sorted(beers))

#sort mutates the list permanently
#pass in reverse = True to sort in reverse order
beers.sort(reverse = True)
# print beers

