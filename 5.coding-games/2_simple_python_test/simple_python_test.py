##############################################
#link of Question: https://www.codingame.com/playgrounds/156417/simple-python-test
#1: Given a list of stars in the galaxies, count the number of stars in the universe.(Star wars fan)
################################################

def count_all_stars(galaxies: list[int]) -> int:
    total_stars = 0
    for i in range(0, len(galaxies)):
        total_stars =total_stars +galaxies[i]

    return total_stars


##############################################
#2.Are theses numbers palindromes?
################################################

def is_int_palindrome(number: int) -> bool:
    flag = False
    if str(number) == str(number)[::-1]:
        flag = True
    return flag


##############################################
#link of Question: https://www.codingame.com/playgrounds/156417/simple-python-test
#3.What is the anagram of these sentences?
################################################

def is_anagram(word1: str, word2: str) -> bool:
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False
    
###########

