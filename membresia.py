from abc import ABC, abstractmethod


class Membresia(ABC):
    @abstractmethod
    def _crear_nueva_membresia(self):
        pass

class Gratis(Membresia):

    costo = 0
    maximos_dispositivos = 1

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.correo_suscriptor = correo_suscriptor
        self.numero_tarjeta = numero_tarjeta
        self.dias_regalo = 0
        self.dispositivos = 0

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Gratis(self.correo_suscriptor, self.numero_tarjeta)
        
class Basico(Membresia):
    
    costo = 3000
    maximos_dispositivos = 2
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.correo_suscriptor = correo_suscriptor
        self.numero_tarjeta = numero_tarjeta
        self.dias_regalo = 0
        self.dispositivos = 0
        
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Familiar(Membresia):
    
    costo = 5000
    maximos_dispositivos = 5
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.correo_suscriptor = correo_suscriptor
        self.numero_tarjeta = numero_tarjeta
        self.dias_regalo = 7
        self.dispositivos = 0
        
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        
    def modificar_control_parental(self):
        pass
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class SinConexion(Membresia):
    
    costo = 3500
    maximos_dispositivos = 2
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.correo_suscriptor = correo_suscriptor
        self.numero_tarjeta = numero_tarjeta
        self.dias_regalo = 7
        self.dispositivos = 0
        
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        
    def cantidad_maxima_contenido(self):
        pass
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Pro(Membresia):
    
    costo = 7000
    maximos_dispositivos = 6
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.correo_suscriptor = correo_suscriptor
        self.numero_tarjeta = numero_tarjeta
        self.dias_regalo = 15
        self.dispositivos = 0
        
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        else:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
    
    def modificar_control_parental(self):
        pass
    
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)