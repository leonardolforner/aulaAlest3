from queue import PriorityQueue

def main():
    mochilaM = 165
    mochilaC = 0
    mochila = []
    pesos = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    valores = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    tuplas = []

    pqueue = PriorityQueue
    

    counter = 0
    #enche uma pQueue com (index, peso), idex -> valor/peso
    for peso in pesos:
        tuplas.append([valores[counter]/pesos[counter], counter])
        trueVal = valores[counter]/pesos[counter]
        pqueue.put(trueVal, tuplas[counter])
        counter += 1
        
    for peso in pqueue:
        atual = pqueue.get()
        if (pesos[atual[1]] < (mochilaM - mochilaC)):
            mochila.append(atual[1])



    
main()

