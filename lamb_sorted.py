
letras = ['A', 'B', 'C','a', 'D', 'E']
print(sorted(letras))
# ['A', 'B', 'C', 'D', 'E', 'a']

print("\n")
print(sorted(letras, key=lambda i : i.upper()))
# ['A', 'a', 'B', 'C', 'D', 'E']

print("\n")
print(sorted(letras, key=lambda i : i.lower()))
# ['A', 'a', 'B', 'C', 'D', 'E']

nomes = []
nomes.append({"id":1,"nome":"Hector","idade":"27",
    "filhos" : ['Ana','João']});
nomes.append({"id":2,"nome":"Luis","idade":"34",
    "filhos" : ['Pedro', 'Paulo']});
nomes.append({"id":3,"nome":"Alan","idade":"36",
    "filhos": ['DeLon', 'Parson']});
nomes.append({"id":4,"nome":"Thiago","idade":"32",
    "filhos": ['Letícia', 'Janaína']});

#classifica em ordem alfabética
print("\n")
for i in sorted(nomes, key=lambda i : i['nome']):
    print(i)

#classifica da menor idade para a maior
print("\n")
for i in sorted(nomes, key=lambda i : i['idade']):
    print(i)

#classifica da maior idade para a menor
print("\n")
for i in sorted(nomes, reverse= True, key=lambda i : i['idade']):
    print(i)

#classifica alfabeticamente pelo nome do segundo filho
print("\n")
for i in sorted(nomes, key=lambda i : i['filhos'][1]):
    print(i["filhos"])

#classifica alfabeticamente pelo nome do segundo filho
print("\n")
for i in [i["filhos"] for i in sorted(nomes, key=lambda i : i["filhos"][1])]:
    print(i)