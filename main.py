from time import sleep


class Computadora:
    # Metodo constructor de la clase
    # macbook_m2 = Computadora("Apple", "MacBook Pro 2022", "M2", "macos", "512 gb", "8 gb", 13, [], "30000 mAh)
    def __init__(self, marca, modelo, procesador, sistema_operativo, disco_duro, ram, pantalla, perifericos):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo
        self.disco_duro = disco_duro
        self.ram = ram
        self.pantalla = pantalla
        self.perifericos = perifericos

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def encender(self):
        print("Arrancando...")
        sleep(2)
        print("Bienvenido, estamos listos para trabajar!")

    def apagar(self):
        print("Cerrando todas las aplicaciones y programas...")
        sleep(3)
        print("Hasta luego!")

    #### METODOS PARA HACER DE TAREA
    def programar(self):
        pass

    def abrir_programa(self, nombre_programa):
        pass

    def ver_image(self, imagen):
        pass

    def navegar_en_internet(self, sitio_web):
        pass
    #### AQUI TERMINA LA TAREA
    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Disco duro: {self.disco_duro}")
        print(f"RAM: {self.ram}")
        print(f"Pantalla: {self.pantalla}")
        print(f"Perifericos: {self.perifericos}")


class Laptop(Computadora):
    def __init__(self, marca, modelo, procesador, sistema_operativo, disco_duro, ram, pantalla, perifericos, bateria):
        super().__init__(marca, modelo, procesador, sistema_operativo, disco_duro, ram, pantalla, perifericos)
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo
        self.disco_duro = disco_duro
        self.ram = ram
        self.pantalla = pantalla
        self.perifericos = perifericos
        self.bateria = bateria

    def abrir_pantalla(self):
        pass