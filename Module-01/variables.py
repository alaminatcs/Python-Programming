name_first_letter = 'a'             #char type
print(name_first_letter)

full_name = 'Alamin Hasan'          #string type
print(full_name)

int = 7
print(int)                          #intergr type

dbl = 7.2

print(type(int), type(full_name), type(dbl))    #data type of variables

text = "Alamin "  + "Hasan"             #string concatenation using +
text2 = f"{full_name}, age = {int}"     #string concatenation using f-strings
print(text)
print(text2)