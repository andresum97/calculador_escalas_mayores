# Alberto Andrés Urízar Mancía
# Carnet 17632

NOTAS = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

FORMULA = [2,2,1,2,2,2,1]
ACORDESF = [0,2,4]
ACORDESMAYOR = [4,7]
ACORDESMENOR = [3,7]
ACORDESDIS = [3,6]
ACORDESAUM = [4,8]


def calculoEscala(nota):
    indice = NOTAS.index(nota)
    resultado = []
    indice_escala = 0
    cont_tono = 0
    for tono in FORMULA:
        cont_tono = cont_tono + tono
        indice_escala = (indice + cont_tono)
        resultado.append(NOTAS[indice_escala%12])

    return resultado


def calculoAcordes(notas):
    for nota in notas:
        indice = notas.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESF:
            indice_escala = indice + cont
            # print("indice escala",indice_escala)
            resultado.append(notas[indice_escala%7])

        # print("Primer resultado",resultado)
        indice_raiz = NOTAS.index(resultado[0])
        # indice_tercera1 = NOTAS.index(resultado[1])
        # indice_tercera2 = NOTAS.index(resultado[2])


        indice_tercera1 = -1
        indice_tercera2 = -1
        cont = indice_raiz
        while indice_tercera1 == -1 or indice_tercera2 == -1:
            i = cont % 12
            if resultado[1] == NOTAS[i]:
                indice_tercera1 = cont
            if resultado[2] == NOTAS[i]:
                indice_tercera2 = cont
            cont += 1

        # print("indices",indice_raiz," ,",indice_tercera1," ,",indice_tercera2," ,")

        primer_tercera = indice_tercera1 - indice_raiz
        segunda_tercera = indice_tercera2 - indice_raiz

        temp = [primer_tercera,segunda_tercera]
        tipo = ""
        # print("temp",temp)
        if temp == ACORDESMAYOR:
            tipo = "mayor"
        elif temp == ACORDESMENOR:
            tipo = "menor"
        elif temp == ACORDESDIS:
            tipo = "disminuido"
        elif temp == ACORDESAUM:
            tipo = "aumentado"

        
        print("Acorde de ",nota," : ",resultado, "| ",tipo)


if __name__ == "__main__":
    print("Notas permitidas: ",NOTAS)
    nota = input("Ingrese la nota en formato de letra (ej: C o E#)")
    res = calculoEscala(nota)
    print("Las notas en la escala de ",nota," son: ",res)
    print("===== Acordes mayores =====")
    calculoAcordes(res)