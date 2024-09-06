from prenda_de_vestir import PrendaDeVestir

class Camisa(PrendaDeVestir):
    def __init__(self, nombre, talla, color, precio, manga_larga):
        super().__init__(nombre, talla, color, precio)
        self.manga_larga = manga_larga

    def mostrar_info(self):
        super().mostrar_info()
        if self.manga_larga:
            print("Tipo de prenda: Camisa de manga larga")
        else:
            print("Tipo de prenda: Camisa de manga corta")
