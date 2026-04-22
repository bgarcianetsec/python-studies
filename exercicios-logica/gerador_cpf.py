"""
ENUNCIADO: Algoritmo de Validação do Primeiro Dígito do CPF
O objetivo é calcular o primeiro dígito verificador de um CPF com base nos 9 primeiros números.

Regras:
1. Multiplicar os 9 primeiros dígitos por uma contagem regressiva de 10 até 2.
2. Somar todos os resultados dessas multiplicações.
3. Multiplicar a soma total por 10.
4. Obter o resto da divisão do resultado por 11.
5. Se o resto for maior que 9, o dígito é 0. Caso contrário, o dígito é o próprio resto.

Exemplo de cálculo para o CPF (fictício): 746.824.890-XX
Soma ponderada: (7*10)+(4*9)+(6*8)+(8*7)+(2*6)+(4*5)+(8*4)+(9*3)+(0*2) = 301
Cálculo final: (301 * 10) % 11 = 7
Dígito resultante: 7
"""

# Configuração inicial
contador = 10
cpf_lista = [7, 4, 6, 8, 2, 4, 8, 9, 0]
resultados_multiplicacao = []

# Etapa 1: Multiplicação ponderada dos dígitos
for digito in cpf_lista:
    # Multiplica o dígito atual pelo peso (10, 9, 8...) e guarda na lista
    resultados_multiplicacao.append(contador * digito)
    # Reduz o contador para o próximo dígito
    contador -= 1

# Etapa 2: Soma dos resultados obtidos
total_soma = sum(resultados_multiplicacao)

# Etapa 3: Cálculo do dígito verificador
# Multiplica por 10 e pega o resto da divisão por 11
resultado_final = (total_soma * 10) % 11

# Etapa 4: Lógica de validação (Se > 9, vira 0)
primeiro_digito = resultado_final if resultado_final <= 9 else 0

# Exibição dos resultados (Útil para Debug e Feedback)
print("-" * 30)
print(f"CPF Base: {''.join(map(str, cpf_lista))}")
print(f"Soma Ponderada: {total_soma}")
print(f"Primeiro Dígito Calculado: {primeiro_digito}")
print("-" * 30)

# Comentários de depuração (opcionais para o dev):
# print(f'Lista de somas: {resultados_multiplicacao}')
# print(f'Resto da divisão direta: {resultado_final}')
