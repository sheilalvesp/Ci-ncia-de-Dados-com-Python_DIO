texto = input("Informe um texto: ")
VOGAIS = "AEIOU"    

#Exemplo usando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: 
    print() #adiciona quebra de linha
    
#Exemplo usando a função built-in range
for numero in range(0,51,5):
    print (numero, end=" ")