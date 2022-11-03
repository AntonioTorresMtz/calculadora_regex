import re
# .     Any Character Except a new Line
#\d     Digit (0-9)
#\D     Not  a digit (0-9)
#w      Word character (a-z, A-Z, 0-9, _)
#\W      Not  a word character
#s      White space (space, tab, newline)
#S      Not white space (space, tab, newline)
#b      Word boundary
#B      Not a Word boundary
#^      Beginning of a String, tambien lo niega
#$      End of a String
# []    Matches characters  in brackets
#Quatifiers:
# * Cerradura de kleanee
# + Cerradura positiva
# ? 0 or One
# {3}  Exact Number
#{3,4} Range of numbers (Minimun, Maximum)
# a-zA-z Todas las letras en mayusculas o minusculas
#18:00

sentence = "Start a abc Mr. Antonio $4x43 Ms. Elizabeth Mr $45x3 Andrade  5 sentence $86 and $97 .then this 46 47 abc end 425-100-6712 425.118.1587 800-564-9876"
productos = ["T500 + plus", "Inpods 12", "Correa silicon"]
#pattern = re.compile(r'[89]00[.-]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'([$]\d*)([xX]\d*)?')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

#matches = pattern.finditer(sentence)

total = 0

with open('data2.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
        if (match.group(2) == None):
            cantidad = match.group(1)[1:]
            total = total + int(cantidad)
        else:
            cant1 = match.group(1)[1:]
            cant2 = match.group(2)[1:]
            cant = int(cant1) * int(cant2)
            total = total + cant

print("El total es $" + str(total))



    #total = total + int(cantidad)
