from asyncio.windows_events import NULL
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if int(valor.dpi) < int(nodo_actual.valor.dpi):
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif int(valor.dpi) > int(nodo_actual.valor.dpi):
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return None
        if int(nodo_actual.valor.dpi) == int(valor.dpi):
            return valor
        elif int(valor.dpi) < int(nodo_actual.valor.dpi):
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual
        
        # Determinar en qué subárbol está el nodo a eliminar
        if int(valor.dpi) < int(nodo_actual.valor.dpi):
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif int(valor.dpi) > int(nodo_actual.valor.dpi):
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            # Si el nodo tiene un solo hijo o ninguno
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            # Si el nodo tiene dos hijos
            nodo_actual.valor = self.min_value_node(nodo_actual.derecha).valor
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, nodo_actual.valor)

        return nodo_actual

    def buscar_por_nombre(self, name):
        resultados = []
        self._buscar_por_nombre_recursivo(self.raiz, name, resultados)
        return resultados

    def _buscar_por_nombre_recursivo(self, nodo_actual, name, resultados):
        if nodo_actual:
            self._buscar_por_nombre_recursivo(nodo_actual.izquierda, name, resultados)
            
            if nodo_actual.valor.name == name:
                resultados.append(nodo_actual.valor)
            
            self._buscar_por_nombre_recursivo(nodo_actual.derecha, name, resultados)

    def buscar_por_dpi(self, dpi):
        resultados = []
        self._buscar_por_dpi_recursivo(self.raiz, dpi, resultados)
        return resultados

    def _buscar_por_dpi_recursivo(self, nodo_actual, dpi, resultados):
        if nodo_actual:
            self._buscar_por_dpi_recursivo(nodo_actual.izquierda, dpi, resultados)
            
            if nodo_actual.valor.dpi == dpi:
                resultados.append(nodo_actual.valor)
            
            self._buscar_por_dpi_recursivo(nodo_actual.derecha, dpi, resultados)


    def min_value_node(self, nodo):
        current = nodo
        while(current.izquierda is not None):
            current = current.izquierda
        return current