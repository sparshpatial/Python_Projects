from langdetect import detect
text = input("Enter any text in any language: ")#taking user input
print(detect(text))#printing out the kind of language 
