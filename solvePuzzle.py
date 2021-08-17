import enchant;
dict = enchant.Dict("en_US");


def beatDorrisRecursively(listOfCharsLeft, currentString):

    for char in listOfCharsLeft:
        if(len(listOfCharsLeft) != 0):
            currentString += char;
            listOfCharsLeft.remove(char);
            beatDorrisRecursively(listOfCharsLeft)


def functionProxy():
    inputString = input("Enter a string of letters: ")
    listOfCharacters = list(inputString);
    blankBaseString = "";
    beatDorrisRecursively(listOfCharacters, blankBaseString);

def beatDorrisWithBruteForce(stringOfChars, MAX_LENGTH, setOfWords, currentString):
    for char in stringOfChars:
        if(len(currentString) < MAX_LENGTH):
            newTempString = char + currentString;
            newStringOfChars = stringOfChars.replace(char, "", 1);
            if(len(newTempString) > 2 and dict.check(newTempString)):
                setOfWords.add(newTempString);
            beatDorrisWithBruteForce(newStringOfChars, MAX_LENGTH, setOfWords, newTempString);


def bruteForceProxy():
    charsToUse = input("Type in a string of letters: ");
    MAX_LENGTH = len(charsToUse);
    setOfValidWords = set();
    blankBaseString = "";

    beatDorrisWithBruteForce(charsToUse, MAX_LENGTH, setOfValidWords, blankBaseString);

    spaceCount = 1;
    prettyString = "";
    wordsAsList = list(setOfValidWords);
    wordsAsList.sort(key=len);

    for word in wordsAsList:
        print(word);

bruteForceProxy();


