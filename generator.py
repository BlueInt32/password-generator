import random
import sys

nb = int(sys.argv[1])
print("Hi ! I was created to generate an easy to type password. You asked for one with %s words :" % (nb) )

wordsList = []
with open('large_wordlist.txt') as f:
  for line in f:
    word = line.split('\t')[1]
    wordsList.append(word.rstrip())
  count = len(wordsList)
  container = []
  seps = [',','.','$','*']
  for i in range(0, nb):
    wordChoice = random.randint(0, count - 1)
    sepChoice = random.randint(0, len(seps) - 1)
    chosenWord = wordsList[wordChoice]
    chosenSep = seps[sepChoice]
    container.append(chosenWord)
    container.append(chosenSep)
  container.pop()
  password = ''.join(container)
  print(password)

  f.close()