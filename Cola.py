from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, siguiente=None):
        self.nombre = nombre
        self.siguiente = siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente


class Cola:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def encolar(self, nombre):
        nuevo_nodo = Nodo(nombre)

        if self.ultimo_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo

        self.ultimo_nodo = nuevo_nodo
        print(f"'{nombre}' ha sido encolado.")

    def desencolar(self):
        if self.primer_nodo is None:
            print("La cola está vacía.")
            return None

        nombre = self.primer_nodo.nombre
        self.primer_nodo = self.primer_nodo.siguiente

        if self.primer_nodo is None:
            self.ultimo_nodo = None

        print(f"'{nombre}' ha sido desencolado.")
        return nombre

    def mostrar_cola(self):
        if self.primer_nodo is None:
            print("La cola está vacía.")
            return

        actual = self.primer_nodo
        print("Elementos en la cola:")
        while actual:
            print(f"- {actual.nombre}")
            actual = actual.siguiente

    def graficar_cola(self):
        if self.primer_nodo is None:
            print("No hay elementos en la cola para graficar.")
            return

        dot = Digraph()
        dot.attr(rankdir="LR")  # Orientación de izquierda a derecha

        actual = self.primer_nodo
        while actual:
            dot.node(actual.nombre, actual.nombre)  # Nodo con el nombre
            if actual.siguiente:
                dot.edge(actual.nombre, actual.siguiente.nombre)  # Conectar nodos
            actual = actual.siguiente

        # Guardar y mostrar el gráfico
        dot.render("cola", format="png", cleanup=True)
        print("Cola graficada y guardada como 'cola.png'. ¡Revísala!")

def menu():
    cola = Cola()

    while True:
        print("\nMenú:")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Mostrar cola")
        print("4. Graficar cola")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre a encolar: ")
            cola.encolar(nombre)
        elif opcion == "2":
            cola.desencolar()
        elif opcion == "3":
            cola.mostrar_cola()
        elif opcion == "4":
            cola.graficar_cola()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        elif opcion == "6":
            print("Es mi primer programa")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
