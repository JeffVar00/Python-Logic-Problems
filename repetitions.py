repeticiones = int(input())

for i in range(repeticiones):
	entradas = input()
	total = 0
	menor = 0
	for j in range(len(entradas)):
		if(entradas[j] == "<"):
			menor += 1
		if(entradas[j] == ">" and menor > 0):
			total += 1
			menor -= 1

	print(total)
