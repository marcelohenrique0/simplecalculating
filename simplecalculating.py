def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Divisão por zero não é permitida"
    else:
        return a / b

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    escolha = input("Digite o número da operação desejada: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", add(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtract(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiply(num1, num2))
        elif escolha == '4':
            print("Resultado:", divide(num1, num2))
        
        outra_operacao = input("Deseja fazer outra operação? (s/n): ")
        if outra_operacao.lower() != 's':
            break
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida (1/2/3/4).")