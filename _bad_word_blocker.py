password = input("Enter your Project access key: ")
if password == "Soham@123":
  print("Welcome to the Bad Word Blocker Project!")
else :
   print("Incorrect accesss key, Try another again")
   exit()

print("*"*50)
print("Bad Word Blocker".center(50))
print("*"*50)

# word to be block
bad_words =  (
    "idiot", "stupid", "dumb", "fool", "loser",
    "hate", "kill", "ugly", "fat", "nonsense",
    "trash", "jerk", "nasty", "dork", "shut up",
    "moron", "sucks", "crazy", "mad", "freak",
    "bloody", "lame", "stinker", "clown", "weirdo",
    "gross", "dirtbag", "crap", "hell", "damn"
)

# inputs
sentence = input("enter your sentence: ")
# blocker
for word in bad_words: 
    sentence = (sentence.replace(word, "***"))
# display 
print("modified sentence: ", sentence)