
import difflib

words = [ 'tengo' , "caca" ,
 'no' , 'soporto', ]
 
frase = input('write something: ')

def corrector(frase):
    for word in frase.casefold().split():
        if word not in words:
            similar =  difflib.get_close_matches(word, words) 
            print(similar[0], end=" ") 
        else:
            print(word, end=" ")

print(corrector(frase))


corrector('Tenjo caka no zoporto')





