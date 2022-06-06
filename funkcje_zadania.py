print ("Nowy sposób")
def palindrome(s):
    r = "".join(reversed(s))
    print (s == r)
     

palindrome("!@mna, ")




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


