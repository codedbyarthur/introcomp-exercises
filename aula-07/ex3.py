n = int(input("Quantidade de números: "))
maior = None

for i in range(n):
    num = int(input("Digite um número: "))
    if maior is None or num > maior:
        maior = num

print("Maior:", maior)
