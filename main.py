# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower().strip().split()
    word = ''.join(word)
    word = sorted(word)
    
    anagram = anagram.lower().strip().split()
    anagram = ''.join(anagram)
    anagram = sorted(anagram)

    if word == anagram:
        return True

    else:
        return False
    
find_anagram("The country side", "No City Dust")