#with open('O Principe.txt' , 'r', encoding='utf-8') as arquivo:
 #  for linha in arquivo:
 #      print(linha.rstrip())
with open('O Principe.txt' , 'r', encoding='utf-8') as arquivo:
   linhas = arquivo.readlines()

print(type(linhas))
print(linhas)