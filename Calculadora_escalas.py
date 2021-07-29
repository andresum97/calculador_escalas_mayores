# Alberto Andrés Urízar Mancía
# Carnet 17632

NOTAS = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

FORMULA = [2,2,1,2,2,2,1]
ACORDESF = [0,4,7]


def calculoEscala(nota):
    indice = NOTAS.index(nota)
    resultado = []
    indice_escala = 0
    cont_tono = 0
    for tono in FORMULA:
        cont_tono = cont_tono + tono
        indice_escala = (indice + cont_tono)
        # print("Tono ",cont_tono)
        # print("indice",indice)
        # print("Indice escala", indice_escala%12)
        resultado.append(NOTAS[indice_escala%12])

    return resultado


def calculoAcordes(notas):
    for nota in notas:
        indice = NOTAS.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESF:
            indice_escala = indice + cont
            # print("Tono ",cont)
            # print("indice",indice)
            # print("Indice escala", indice_escala%12)
            resultado.append(NOTAS[indice_escala%12])
        
        print("Acorde de ",nota," : ",resultado)




if __name__ == "__main__":
    print("Notas permitidas: ",NOTAS)
    nota = input("Ingrese la nota en formato de letra (ej: C o E#)")
    res = calculoEscala(nota)
    print("Las notas en la escala de ",nota," son: ",res)
    calculoAcordes(res)