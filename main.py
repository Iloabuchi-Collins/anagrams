# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

#author: iloabuchi_collins
#I4G-ZURI scholarship task

def find_anagram(word, anagram):
    if sorted(str(word)) == sorted(str(anagram)):
        return "--> True"
    return "--> False"

print(find_anagram(10011, 11100))
print(find_anagram("peace", "violence"))
print(find_anagram("desoxystatin", "deoxystatins"))
print(find_anagram("100023", "32001"))
print(find_anagram("choleferol 200", "200 choleferol"))