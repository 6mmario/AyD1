class Nodo:
    def __init__(self, objeto, siguiente=None, atras = None):
        self.objeto = objeto
        self.siguiente = siguiente
        self.atras = atras

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente