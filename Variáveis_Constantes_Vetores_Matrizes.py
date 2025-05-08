# ---------- VARIÁVEIS ----------

# String (texto)
nome = "Rafaella"

# Número inteiro
idade = 23

# Booleano (verdadeiro ou falso)
estudante = True

# ---------- CONSTANTES ----------

# Por convenção, usamos letras maiúsculas para constantes
CURSO = "Sistemas de Informação"
ANO_ATUAL = 2025
AMA_PROGRAMAR = True

# ---------- VETORES (LISTAS) ----------

# Lista de strings
frutas = ["kiwi", "banana", "morango"]

# Lista de números
notas = [8.5, 9.0, 7.3]

# Lista de valores booleanos
respostas = [True, False, True]

# Acessando elementos de listas
print("Primeira fruta:", frutas[0])  # índice 0 = primeiro item
print("Segunda nota:", notas[1])     # índice 1 = segundo item

# ---------- MATRIZES (LISTAS DE LISTAS) ----------

# Matriz numérica 3x3
matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elemento da 2ª linha e 3ª coluna (índice começa em 0)
print("Elemento da 2ª linha, 3ª coluna:", matriz_numeros[1][2])  # resultado: 6

# Matriz de nomes 2x2
matriz_nomes = [
    ["Fernanda", "Luis Fernando"],
    ["Luis Gustavo", "Kyara"]
]

# Acessando elemento específico da matriz
print("Nome na posição [0][1]:", matriz_nomes[0][1])  # resultado: Luis Fernando

# ---------- EXIBIÇÃO FINAL ----------

print("Nome:", nome)
print("Idade:", idade)
print("Estudante?", estudante)
print("Curso:", CURSO)
print("Ano Atual:", ANO_ATUAL)
print("Ama programar?", AMA_PROGRAMAR)
