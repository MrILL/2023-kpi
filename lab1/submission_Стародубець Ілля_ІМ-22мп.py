import collections
import math

############################################################
# Problem 1a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    words = text.split(' ')

    res = words[0]
    for word in words[1:]:
        if word > res:
            res = word

    return res
    # END_YOUR_CODE

############################################################
# Problem 1b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt(math.pow(loc2[0] - loc1[0], 2) + math.pow(loc2[1] - loc1[1], 2))
    # END_YOUR_CODE

############################################################
# Problem 1c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    words = sentence.split(' ')
    map = {}
    for i in range(len(words) - 1):
        if words[i] in map:
            map[words[i]].append(words[i + 1])
        else :
            map[words[i]] = [words[i + 1]]

    res = set()
    def recursive(curWord, curSentence = []): 
        curSentence.append(curWord)

        if len(curSentence) < len(words):
            if curWord in map:
                for nextWord in map[curWord]:
                    recursive(nextWord, curSentence)
        else:
            res.add(' '.join(curSentence))

        curSentence.pop()

    for word in words: recursive(word)

    return list(res)
    # END_YOUR_CODE

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    return sum([v1[v] * v2[v] if v in v2 else 0 for v in v1.keys()])
    # res = 0
    # for v in v1.keys(): 
    #     if v in v2: 
    #         res += v1[v] * v2[v]
    # 
    # return res
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    res = {}
    for v in v2.keys():
        res[v] = v2[v] * scale
        if v in v1:
            res[v] += v1[v]

    return res
    # END_YOUR_CODE

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    wordCounter = {}
    for word in text.split(' '):
        if word in wordCounter:
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
    
    return set([k for (k, v) in wordCounter.items() if v == 1])
    # END_YOUR_CODE

############################################################
# Problem 1g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    def rec(text, startI = 0, endI = len(text)):
        if endI - startI < 2:
            return endI - startI

        maxStringL = 0
        for curStartI in range(startI, endI - 1):
            if maxStringL >= endI - 1 - curStartI:
                break

            curEndI = text.rfind(text[curStartI], curStartI, endI)
            if maxStringL >= curEndI - curStartI + 1:
                continue

            if curEndI == curStartI: #len = 1
                if maxStringL < 1:
                    maxStringL += 1
                continue
            
            newStringL = 2 + rec(text, curStartI + 1, curEndI)
            if maxStringL < newStringL:
                maxStringL += newStringL

        return maxStringL
    
    return rec(text)
    # END_YOUR_CODE
