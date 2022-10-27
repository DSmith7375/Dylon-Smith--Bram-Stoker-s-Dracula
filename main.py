# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")
#Variable to read dict
draculaText = readBook()
#create a list for words 
wordList = {}
#spilt the words in the book and store in variable  
words = draculaText.spilt() 

#Create a iteration through the word variable 
for word in words: 
  wordList[word] += 1
  
# Create a loop for the words lowercase 
for word in words.lower() == "":
 print(wordList[draculaText])  