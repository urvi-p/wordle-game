import random

def main():
  # Source for word list: https://nerdschalk.com/5-letter-harry-potter-words-list-find-a-hint-for-harry-potter-wordle-easily/
  listOfWords = readInWords()
  printInstructions()

  quit = False
  while not quit:
    runGame(listOfWords)
    replay = input("Would you like to play again y/n? ")
    if replay.lower() != 'y':
      quit = True
  
  print("Thanks for playing!")

def readInWords():
  # Read in words from file

  f = open("words.txt", 'r')
  listOfWords = f.readlines()
  f.close()
  return listOfWords

def printInstructions():
  # Print the initial instructions for the game

  instructions = '''
    Welcome to Wordle, Harry Potter Edition!

    Guess the 5-letter word.
    You have 6 guesses.

    Legend:
      - : letter not in word
      * : letter in word but in wrong position
      a : letter in right position

    Ex) word: house
       guess: store
      result: *-*-e

    Let's get started...'''
  print(instructions)

def runGame(listOfWords):
  # This loop runs the game. Gets guesses from the user and prints the results.

  letters = list("abcdefghijklmnopqrstuvwxyz")
  word = listOfWords[random.randint(0, len(listOfWords)-1)].strip()
  charsOfWord = [char.lower() for char in list(word)]

  guessedWord = False
  tries = 6
  guesses = []  # [[guessed word, response],...,]

  while not guessedWord and tries > 0:
    # ask user for input and check validity
    print("\nLetters left to guess: %s" % " ".join(letters))
    guess = input("%d guesses left. Make a guess: " % tries)

    if not guess.isalpha() or len(guess) != 5:
      print("Invalid guess. Try again!\n")
      continue

    response = getResultOfGuess(guess, charsOfWord, letters)

    result = "".join(response)
    guesses.append([guess, result])
    printAllGuesses(guesses)
    
    if result.lower() == word.lower():
      guessedWord = True
    tries -= 1
  
  if guessedWord:
    print("\nCongratulations! You guessed correctly, the word was %s." % word)
  else:
    print("\nUnlucky! You did not guess the word in 6 tries. The word was %s." % word)

def getResultOfGuess(guess, charsOfWord, letters):
  # Compare guess to word and return all guesses

  charsOfGuess = list(guess)
  tempCharsOfWord = charsOfWord[:]
  response = []

  # find letters in correct position
  for i in range(5):
    if charsOfGuess[i] in letters:
      letters.remove(charsOfGuess[i])
    if charsOfGuess[i].lower() == tempCharsOfWord[i]:
      response.append(charsOfGuess[i])
      tempCharsOfWord[i] = "-"
    else:
      response.append("-")

  # find letters in word but in wrong position
  for i in range(5):
    if charsOfGuess[i] in tempCharsOfWord:
      response[i] = "*"
  
  return response

def printAllGuesses(guesses):
  # Print all guesses so far

  for guess in guesses:
    print("%s: %s" % (guess[0], guess[1]))

main()