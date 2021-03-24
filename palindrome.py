# test if a word is a palindrome

def palindrome (word):
   newword = list(word) # ['b,u,b,b,l,e']
   res = newword[::-1] # [e,l,b,b,u,b]
   resword = ''.join(res) #  ' ' + []= 'elbbub'
   if word == resword:
       print("This word, "+ word +", is a palindrome!")
   else:
       print("This word, " + word + ", is not a palindrome!")   

palindrome("bubble")
palindrome("kayak")
