from unicodedata import normalize

# Verifica se uma lista de listas é uma matriz
def check_matrix(matrix: list[list]) -> tuple :
    n = len(matrix[0])
    for line in matrix:
        if len(line) != n :
            return -1, -1
    return len(matrix), n

# Função para criar uma matriz de dimensões lin x col
def new_matrix(lin:int,col:int) -> list[list]:
    if lin > 0 and col > 0 :
        matrix = []
        for _ in range(lin):
            matrix.append([None]*col)
        return matrix
    return [[]]

# Função de transposição de matriz
def transpose_matrix(matrix:list[list]) -> list[list]:
    if check_matrix(matrix) != (-1,-1):
        nova = [list(col) for col in zip(*matrix)]
        return nova
    return [[]]

# Converte uma lista de strings de literais inteiros em uma lista de números inteiros
def list_str_to_int(lista:list[str]) -> list :
    saida = []
    for elemento in lista:
        if elemento.isdecimal():
            saida.append(int(elemento))
        elif (elemento[0] == "-" or elemento == "+") and elemento[1:].isdecimal() :
            saida.append(int(elemento))
        else : return [None]
    return saida

# Converte uma lista de strings de literais reais em uma lista de números reais
def list_str_to_float(lista: list[str]) -> list:
    saida = []
    for elemento in lista:
        if elemento.isdecimal():
            saida.append(float(elemento))
        elif (elemento[0] == "-" or elemento == "+") and elemento[1:].count(".") == 1 and elemento[1:].replace(".", "").isdecimal() :
            saida.append(float(elemento))
        elif elemento.count(".") == 1 and elemento.replace(".", "").isdecimal() :
            saida.append(float(elemento))
        else:
            return [None]
    return saida

# Remove acentos e símbolos especiais
def remove_diacritics(texto: str) -> str:
    norm = normalize("NFKD",texto)
    norm = norm.encode("ASCII","ignore")
    return norm.decode("ASCII")