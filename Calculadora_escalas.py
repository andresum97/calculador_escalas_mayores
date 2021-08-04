# Alberto Andrés Urízar Mancía
# Carnet 17632

NOTAS = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

FORMULA = [2,2,1,2,2,2,1]
ACORDESF = [0,4,7]
ACORDESM = [0,3,7]
ACORDESD = [0,3,6]
ACORDESA = [0,4,8]


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


def calculoAcordesMayores(notas):
    for nota in notas:
        indice = NOTAS.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESF:
            indice_escala = indice + cont
        
            resultado.append(NOTAS[indice_escala%12])
        
        print("Acorde de ",nota," : ",resultado)

def calculoAcordesMenores(notas):
    for nota in notas:
        indice = NOTAS.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESM:
            indice_escala = indice + cont
            resultado.append(NOTAS[indice_escala%12])
        
        print("Acorde de ",nota,"m : ",resultado)

def calculoAcordesDisminuidas(notas):
    for nota in notas:
        indice = NOTAS.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESD:
            indice_escala = indice + cont
            resultado.append(NOTAS[indice_escala%12])
        
        print("Acorde de ",nota,"dim : ",resultado)

def calculoAcordesAumentados(notas):
    for nota in notas:
        indice = NOTAS.index(nota)
        resultado = []
        indice_escala = 0
        for cont in ACORDESA:
            indice_escala = indice + cont
            resultado.append(NOTAS[indice_escala%12])
        
        print("Acorde de ",nota,"aug : ",resultado)



if __name__ == "__main__":
    print("Notas permitidas: ",NOTAS)
    nota = input("Ingrese la nota en formato de letra (ej: C o E#)")
    res = calculoEscala(nota)
    print("Las notas en la escala de ",nota," son: ",res)
    print("===== Acordes mayores =====")
    calculoAcordesMayores(res)
    print("===== Acordes menores =====")
    calculoAcordesMenores(res)
    print("===== Acordes disminuidos =====")
    calculoAcordesDisminuidas(res)
    print("===== Acordes aumentados =====")
    calculoAcordesAumentados(res)