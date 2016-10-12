# Palindrome search
import codecs
import sys
import string

table = str.maketrans('áéíóú', 'aeiou')

def ispalindrome(word):
    string = word.translate(table)
    return string == string[::-1]

def findpalindromes(path):
    file = codecs.open(path, 'r', 'utf-8')
    palindromes = []

    for line in file:
        word = line[:-1]
        wordt = word.translate(table)

        if len(word) > 1 and wordt == wordt[::-1]:
            palindromes.append(word)

    return palindromes

def findreverse(path):
    file = codecs.open(path, 'r', 'utf-8')
    words = []
    wordst = []
    indices = {}
    reverses = []
    i = 0

    for line in file:
        word = line[:-1]

        if len(word) > 1 and not (word[0] == '-' or word[-1] == '-'):
            wordt = word.translate(table)
            words.append(word)
            wordst.append(wordt)

            if wordt[0] not in indices:
                indices[wordt[0]] = [i, i + 1]
            else:
                indices[wordt[0]][1] = i + 1
                        
            i += 1
    
    for i in range(len(words)):
        for j in range(*indices[wordst[i][0]]):
            if j > i and wordst[i] == wordst[j][::-1]:
                reverses.append((words[i], words[j]))

    return reverses

if __name__ == '__main__':
    path = 'words.es.txt'
    
    palindromes = findpalindromes(path)
    
    print('Palíndromos:')

    for i in palindromes:
        print(' - {0}'.format(i))

    reverse = findreverse(path)
    print('Parejas:')

    for i in reverse:
        print(' {0} - {1}'.format(*i))
