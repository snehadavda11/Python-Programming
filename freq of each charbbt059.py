string= input("Enter a string")
freq={}
for char in string:
      freq[char]= freq.get(char,0)+1
      print("Character Frequency:",freq)
      
