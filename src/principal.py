from camisa import Camisa
from pantalon import Pantalon

if __name__ == "__main__":
    camisa_manga_corta = Camisa("Camisa Casual", "M", "Azul", 35000, False)
    pantalon_chino = Pantalon("Pantalón Jean", "L", "Negro", 75000, "Slim Fit")

    camisa_manga_corta.mostrar_info()
    print("\n")
    pantalon_chino.mostrar_info()
