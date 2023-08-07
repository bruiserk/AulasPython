tabela = {"13": '97.99', "20": '180.00', "45": '390.00'}

while True:
    produto = input("Digite o nome do produto ou fim para terminar: ")

    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço: R$ {tabela[produto]:.2f}")
    else:
        print("Produto não encontrado.")
