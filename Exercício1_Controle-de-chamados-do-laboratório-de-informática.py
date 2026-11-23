#Você foi contratado para desenvolver um sistema simples de controle de 
#chamados técnicos. 
#O programa deverá armazenar em um vetor a quantidade de chamados 
#registrados durante os cinco dias úteis da semana. 
#Requisitos obrigatórios 
#1. Criar um vetor vazio para armazenar os chamados. 
#2. Solicitar ao usuário a quantidade de chamados de segunda a sexta-feira. 
#3. Não permitir a entrada de quantidades negativas. 
##4. Armazenar os cinco valores no vetor. 
#5. Calcular o total de chamados da semana. 
#6. Calcular a média diária de chamados. 
#7. Identificar o dia com maior quantidade de chamados. 
#8. Informar quais dias apresentaram quantidade de chamados acima da 
#média. 
#9. Apresentar um relatório organizado na tela.




dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
chamados = []

for dia in dias:
    while True:
        qtd = int(input(f"Chamados de {dia}: "))
        if qtd >= 0:
            chamados.append(qtd)
            break
        print("Erro: digite um valor maior ou igual a zero.")

total = sum(chamados)
media = total / 5 
maior_qtd = max(chamados) 
dia_maior = dias[chamados.index(maior_qtd)]


print("\n --------------- Relatório da semana ------------------")
print(f"Total de chamados: {total}")
print(f"Média diária: {media}")
print(f"Dia com mais chamados: {dia_maior} ({maior_qtd})")
print("Dias acima da média: ")

for i in range(5):
    if chamados[i] > media:
        print(f"-{dias[i]} ({chamados[i]})")
#------------------------------------- --- - - --  ---------------------------------------------------------------------------------



