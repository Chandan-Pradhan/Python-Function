def palindrome(letter):
    letter = letter.replace(' ','')
    return letter == letter[::-1]

print(palindrome('nurses run'))
