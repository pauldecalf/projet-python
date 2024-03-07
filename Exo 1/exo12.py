# Écrivez un programme qui compte combien de mots dans une liste sont des palindromes. Un palindrome est un mot qui se lit de la même manière de gauche à droite et de droite à gauche.

def count_palindromes(words):
    return sum(word == word[::-1] for word in words)