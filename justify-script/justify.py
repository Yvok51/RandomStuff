#!/usr/bin/env python3

"""
Simple script which justifies text
Takes a command line argument as the width of the text
and justifies the stdin and puts it on stdout
"""

EMPTY_LINE = ''

def tokenize(input):
    for line in input:
        tokens = line.strip().split()
        if not tokens:
            yield EMPTY_LINE
        for token in tokens:
            yield token

def listElementSize(arr : list) -> int:
    return sum(map(len, arr))

def numberOfSpaces(line : list) -> int:
    return len(line) - 1

def minLineSize(line : list) -> int:
    wordSize = listElementSize(line)
    whitespaceSize = numberOfSpaces(line)
    return wordSize + whitespaceSize

def minLineSizeWToken(line : list, word : str):
    return minLineSize(line) + len(word) + 1

def printLeftJustified(line : list, output) -> None:
    for i, word in enumerate(line):
        if i != len(line) - 1:
            print(word, end=' ', file=output)
        else:
            print(word, file=output)

def printJustified(line : list, justifyLength : int, output) -> None:
    extraWhitespace = max(justifyLength - minLineSize(line), 0)
    extraWhitespacePerWord = extraWhitespace // numberOfSpaces(line) if numberOfSpaces(line) > 0 else 0
    leftoverWhitespace = extraWhitespace - extraWhitespacePerWord * numberOfSpaces(line)

    whitespaceBase = ' ' * (extraWhitespacePerWord + 1)
    whitespaceExtended = whitespaceBase + ' '

    for i, word in enumerate(line):
        afterWord = whitespaceExtended if i < leftoverWhitespace else whitespaceBase
        if (i < len(line) - 1):
            print(word, end=afterWord, file=output)
        else:
            print(word, file=output)

def printParagraphBreak(output):
    print(file=output)

def justify(inputStream, outputStream, justifyLength):
    lastLine = []
    currentLine = []
    
    for token in tokenize(inputStream):
        if token == EMPTY_LINE and lastLine:
            printLeftJustified(currentLine, outputStream)
            printParagraphBreak(outputStream)
            currentLine = []
            lastLine = []

        elif minLineSizeWToken(currentLine, token) > justifyLength:
            if currentLine:
                printJustified(currentLine, justifyLength, outputStream)
                lastLine = currentLine
                currentLine = [token]
            else: # single word larger than justifyLength
                printLeftJustified([token], outputStream)
                lastLine = [token]
                currentLine = []

        elif token != EMPTY_LINE:
            currentLine.append(token)

    if currentLine:
        printLeftJustified(currentLine, outputStream)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print('ERROR: Incorrect number of arguments provided\nProvide only the width of the text', file=sys.stderr)
        sys.exit(1)

    justifyLength = args[0]
    if not justifyLength.isdecimal():
        print('ERROR: The argument is not a natural number', file=sys.stderr)
        sys.exit(1)

    justifyLength = int(justifyLength)
    if justifyLength < 1:
        print('ERROR: The text width is less than 1', file=sys.stderr)
        sys.exit(1)

    justify(sys.stdin, sys.stdout, justifyLength)


if __name__ == '__main__':
    import sys
    main()