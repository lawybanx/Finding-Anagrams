# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word = word.lower()
    anagram = anagram.lower()
    if len(word) != len(anagram) or sorted(word) != sorted(anagram):
        return False
    return True


input_word = input("Enter Word: ")
input_anagram = input("Enter anagram: ")
print(find_anagram(input_word, input_anagram))
