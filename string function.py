story = "onces upon a time there was a boy named Kunal."

# STRING Functions
 
print(len(story))                           # to get length of string
print(story.endswith("unal."))              # returns true/false after checking the string ends wtih given string
print(story.count("a"))                     # Counts the total number of occurence of a character/word
print(story.capitalize())                   # capitalizes the first character of the string
print(story.find("kunal"))                  # returns the index of first occurence if present, else returns -1
print(story.replace("Kunal", "Kunnu"))      # replaces all values(Kunal) with "Kunnu"
