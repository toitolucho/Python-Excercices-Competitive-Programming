def isPalindrome(word):
    for i in range(0,  len(word) if len(word)%2 == 2 else len(word)-1):
        #print(word[i] , '  ', word[(i+1)*-1])
        if word[i] != word[(i+1)*-1]:
            return False
    return True

def isPalindrome2(word):
    word = word.lower().replace(" ","")
    return word == word[::-1]

s = input()
print("Is Palindrome" if isPalindrome2(s) else "Not Palindrome" )

