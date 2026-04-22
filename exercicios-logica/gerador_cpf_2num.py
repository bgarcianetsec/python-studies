"""
ENUNCIADO: Algoritmo de Validação do Segundo Dígito do CPF

O objetivo é calcular o segundo dígito verificador utilizando os 9 dígitos iniciais 
mais o primeiro dígito verificador recém-calculado.

Regras:
1. Multiplicar os 10 dígitos por uma contagem regressiva que começa em 11 e vai até 2.
2. Somar os resultados.
3. Multiplicar a soma por 10.
4. Obter o resto da divisão por 11.
5. Se o resto for maior que 9, o dígito é 0. Caso contrário, é o próprio resto.

Exemplo de cálculo:
CPF Base: 746.824.890 + Digit 1 (7)
Pesos: 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
Soma total: 363
Cálculo: (363 * 10) % 11 = 0
Dígito resultante: 0
"""

# Configuração inicial
# Agora incluímos o 7 (primeiro dígito calculado) na lista
cpf_com_primeiro_digito = [7, 4, 6, 8, 2, 4, 8, 9, 0, 7]
contador = 11
lista_resultados = []

# Etapa 1: Multiplicação ponderada (Contagem regressiva de 11 a 2)
for digito in cpf_com_primeiro_digito:
    produto = digito * contador
    lista_resultados.append(produto)
    contador -= 1  # Decrementa o peso para o próximo dígito

# Etapa 2: Soma dos produtos
soma_total = sum(lista_resultados)

# Etapa 3 e 4: Cálculo do resto da divisão
# Multiplicamos a soma por 10 e verificamos o resto por 11
resultado_multiplicado = soma_total * 10
resto_divisao = resultado_multiplicado % 11

# Etapa 5: Lógica final do dígito
# Uso de operador ternário para manter o código limpo (Pythonic Way)
segundo_digito = resto_divisao if resto_divisao <= 9 else 0

# Exibição formatada para o terminal
print("-" * 35)
print(f"Lista de entrada: {''.join(map(str, cpf_com_primeiro_digito))}")
print(f"Soma acumulada: {soma_total}")
print(f"Segundo Dígito Calculado: [ {segundo_digito} ]")
print("-" * 35)

# Comentários de debug (para conferência de valores):
# print(f"Produtos individuais: {lista_resultados}")
# print(f"Valor após multiplicação por 10: {resultado_multiplicado}")





    
    
