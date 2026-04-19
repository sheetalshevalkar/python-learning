#Exercise 12. Count vowels and consonants in a sentence
my_string = "Loops are Fun!"
vowels = ["a","e","i","o","u"]
d = { "vowels": {},
    "consonants": {}} # nested dictionary to store count of vowels and consonants
l = len(my_string)
for i in range(0,l-1):
   if my_string[i].isalnum() and my_string[i] in vowels: # will check char is not special char and is vowel
      d["vowels"].update({my_string[i] : my_string.count(my_string[i])}) #update the count of vowel in dictionary using update method
   elif my_string[i].isalnum():
      d["consonants"].update({my_string[i] : my_string.count(my_string[i])})
   else:
      continue
   
for i,j in d.items():
   for x,y in j.items():
      print (f"no of {x}: {y} ")


# Simple way to count vowels and consonants

my_string = "Loops are Fun!"
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for ch in my_string.lower():
    if ch.isalpha():          # only letters
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)