IntroStrings = input("Enter Your String : ")
CharacterCount = 0
WordCount = 1
for i in IntroStrings : 
    CharacterCount = CharacterCount + 1
    if(i == ' '):
        WordCount = WordCount + 1
print ("The Number Of Words in The String Is : ",WordCount)
print ("The Number Of Characters Are: ",CharacterCount)