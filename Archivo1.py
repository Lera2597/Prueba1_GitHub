
import numpy as np
valor = np.sin(np.pi)
print(f"El valor de seno de pi es :{valor}")


def imprimir(bandera):

    print (f"se imprimio: {'positivo' if bandera else 'negativo'}")

imprimir(True)