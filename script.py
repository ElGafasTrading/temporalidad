from functions import *

if __name__ == "__main__":
    ticks = buscarTicks()
    ticksNumber = len(ticks)
    print("NUMERO DE TICKS: " + str(ticksNumber))
    for tick in ticks:
        analizarmoneda(tick)
    showResults()
