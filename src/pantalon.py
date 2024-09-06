from prenda_de_vestir import PrendaDeVestir

class Pantalon(PrendaDeVestir):
    def __init__(self, nombre, talla, color, precio, estilo):
        super().__init__(nombre, talla, color, precio)
        self.estilo = estilo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de prenda: Pantalón de estilo {self.estilo}")