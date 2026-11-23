produtos = ["Camisetas","Canecas","Bonés" ]
periodos = ["Dia 1 - Manhã", "Dia 1 - Tarde", "Dia 2 - manhã", "Dia 2 - Tarde "]

matriz = [] 

for produto in produtos:
    linha = [] 
    for periodo in periodos:
        while true:
            qtd = int(input(f"VEndas de {produto} ({periodo}): "))
            if qtd > 0:
                linha.append(qtd)
                break
            print("Digite um valor maior ou igual a zero ")
    matriz.append(linha)

total_produto = []
total_periodo = []
total_tudo    = sum(total_produto) 

