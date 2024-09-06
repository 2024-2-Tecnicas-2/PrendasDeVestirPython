class PrendaDeVestir:
    def __init__(self, nombre, talla, color, precio):
        """
        Constructor de la clase.
        
        :param nombre: nombre de la prenda
        :param talla: talla de la prenda
        :param color: color de la prenda
        :param precio: precio de la prenda
        
        Complejidad temporal: O(1) Tiempo constante.
        """
        self.nombre = nombre
        self.talla = talla
        self.color = color
        self.precio = precio

    def get_precio(self):
        """
        Método para obtener el precio de la prenda en formato de moneda colombiana.
        
        :return: precio formateado en moneda colombiana
        
        Complejidad temporal: O(1) Tiempo constante.
        """
        # Formatear el precio en formato colombiano
        precio_formateado = "${:,.0f}".format(self.precio).replace(",", ".").replace(".", ",", 1)
        return precio_formateado

    def mostrar_info(self):
        """
        Método para imprimir en consola los datos de la prenda.
        
        Complejidad temporal: O(1) Tiempo constante.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.get_precio()}")
