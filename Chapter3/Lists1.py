squares = [1, 4, 9, 16, 25, "asdf", 15.5]
print(squares)

print("array length: " + str(len(squares)))

print(squares[0])
print(squares[1])
print(squares[2])
print(squares[3])
print(squares[4])
print(squares[5])
print(squares[6])
print(squares[-1])
print(squares[-2])
print(squares[-3])
print(squares[-4])
print(squares[-5])
print(squares[-6])
print(squares[-7])

print(squares[0:5])
print(squares[-7:-2])
print(squares[5:])

squares += [36, 49, 64, 81, 100]
print(squares)
squares.remove('asdf')
squares.remove(15.5)
print(squares)
squares.append(121)
print(squares)

#DOES NOT COPY DATA, HAS SAME REFERENCE TO MEMORY AS squares
squaresCopy = squares

squaresCopy.append(144)

print(squares)

newSquaresList = squares[:]

newSquaresList.append(13 ** 2)

print(squares)
print(newSquaresList)

newSquaresList[10:] = ['a', 'bunch', 'of', 'junk', 'asdf', 124]
print(newSquaresList)

newSquaresList[10:] = []
print(newSquaresList)


print(newSquaresList.pop())
print(newSquaresList)

newSquaresList.insert(2, "junkString")
print(newSquaresList)

randomList = [6, 3 ,6 ,8 ,4, 1, 5, 10]
randomList.sort()
print(randomList)

randomList.sort(reverse=True)
print(randomList)

randomCopy = randomList.copy()

randomCopy.append("asdfasdf")
print(randomList)

listOfChars = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print(listOfChars)
print("".join(listOfChars))

