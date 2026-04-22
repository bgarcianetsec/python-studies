import random

# --- Título do Projeto ---
print(5 * "-", " GERADOR DE CPF ", 5 * "-")

# --- PASSO 1: Gerar os 9 primeiros dígitos ---
cpf_lista = []
for i in range(9):
    # Sorteia os números do cpf de 0 a 9
    cpf_lista.append(random.randint(0, 9))

# --- PASSO 2: Cálculo do Primeiro Dígito Verificador ---
contagem_1 = 10
soma_1 = 0

for digito in cpf_lista:
    soma_1 += digito * contagem_1
    contagem_1 -= 1

resto_1 = (soma_1 * 10) % 11
primeiro_digito = resto_1 if resto_1 <= 9 else 0
cpf_lista.append(primeiro_digito)

# --- PASSO 3: Cálculo do Segundo Dígito Verificador ---
# A lógica é a mesma, mas a contagem começa em 11
contagem_2 = 11
soma_2 = 0

for digito in cpf_lista:
    soma_2 += digito * contagem_2
    contagem_2 -= 1

resto_2 = (soma_2 * 10) % 11
segundo_digito = resto_2 if resto_2 <= 9 else 0
cpf_lista.append(segundo_digito)

# --- PASSO 4: Formatação para Exibição ---
# Transformando a lista em string sem vírgulas ou espaços
cpf_final = "".join(map(str, cpf_lista))

# Exibição com máscara (pontos e traço)
cpf_formatado = f"{cpf_final[:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:]}"

print(f"CPF Gerado com sucesso: {cpf_formatado}")
print(5 * "-", " FIM DO PROGRAMA ", 5 * "-")




