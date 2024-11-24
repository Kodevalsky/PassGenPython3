from itertools import product
from lists import subDict, dummyCharacters, numbersOnly

# Returns the cartesian product of all replaceable characters 
def fullSub(password):
	letters = []
	# Place substitution sets into the letters array
	for val in password:
		if val in subDict:
			letters.append(subDict[val])
		else:
			letters.append(val)
	return [''.join(item) for item in product(*letters)]

# Returns a list of possible passwords by replacing the first letter with common substitutions and appending numbers and letters to the end. If numbers flag is set then append numbers to end
def basicSub(password, numbers=False):
	numCombos = [''.join(p) for n in range(1, 5) for p in product(numbersOnly, repeat=n)]
	characterList = numCombos if numbers else dummyCharacters
	passwords = []
	middle = password[1:]
	replacements = product(subDict[password[0]], characterList)
	for val in replacements:
		passwords.append(val[0] + middle + val[1])
	return passwords

# Same as basic substitution, but appends 0-9999 to the end 
def appendNumbers(password):
	return basicSub(password, True)
