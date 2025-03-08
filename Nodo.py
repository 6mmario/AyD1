class Nodo:
    def __init__(self, objeto, siguiente=None):
        self.objeto = objeto
        self.siguiente = siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente