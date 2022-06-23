print ("Zadanie: Palindrom")


def palindrome(text):
    text = text.lower()
    signs = ""
    for s in text:
        if s.isalnum():
            signs += s
    return signs == signs[::-1]  

print(palindrome("!Kajak"))
print(palindrome("!Kobyła Ma Mały bok?!"))
print(palindrome("to nie jest palindrom"))


print("-----------------------------------------------------------------")

print ("Zadanie: Palindrom")


def palindrome(word):
    word = word.lower()
    drow = "".join(reversed(word))
  
    if word.isalnum():
        print("Podane słowo jest ok")
        print (word == drow)
    else: 
        print("Podane słowo posiada niedozwolone znaki specjalne")

palindrome("!Kajak")

print("-----------------------------------------------------------------")

print ("Nowy sposób")
def palindrome(s):
    "s".isalpha()
    r = "".join(reversed(s))
    print (s == r)
     
palindrome("55kajak o kajak")


print("1 sposób")
def pali(word: str):
    return print(word == word [::-1]) 
    
pali("12  mm  21")


print("2 sposób")
def pali(word: str):
    return word == word [::-1]
  
print(pali("123abc"))
print(pali("12  mm  21"))
print(pali("!!,?/   "))




print("3 sposób")
slowo = "kajak"
lista1=[]
lista2=[]

for letter in slowo:
    lista1.append(letter)
lista1.reverse()

for letter1 in lista1:
    lista2.append(letter1)
lista2.reverse()

print(lista1)
print(lista2)

if lista1 == lista2:
    print(f"Brawo!! Podane słowo {slowo} jest palindromem!!")
elif lista1 != lista2:
    print(f"Podane słowo {slowo} nie jest palindromem.")



print("4 sposób")
def palindrom (sslowo):
    """
        Function, checks if a given word is a palindrome.
        A palindrome is a word that sounds the same when read from left to right and right to left.
        Examples: "level", "racecar".
        The argument of the function palindrom() is str
    """
    lista3=[]
    lista4=[]
    for letter in sslowo:
        lista3.append(letter)
    lista3.reverse()
    for letter1 in lista3:
        lista4.append(letter1)
    lista4.reverse()
    if lista3 == lista4:
        print(f"Brawo!! Podane słowo {sslowo} jest palindromem!!")
    elif lista3 != lista4:
        print(f"Podane słowo {sslowo} nie jest palindromem.")

palindrom("zapiekanka")


