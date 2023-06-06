PRECIO_TICKET = 70
DESCUENTOS = {
    "PRIMARIO": 0.5,
    "SECUNDARIO": 0.6,
    "UNIVERSITARIO": 0.7,
    "JUBILADO": 0.75,
}
DESACTIVADO = "desactivado"
ACTIVADO = "activado"

class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"
        self.precio_ticket = PRECIO_TICKET

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario is not None:
            return self.precio_ticket * DESCUENTOS[self.grupo_beneficiario]
        return self.precio_ticket
    def pagar_pasaje(self):
        if self.estado == "desactivado":
            raise UsuarioDesactivadoException
        if self.saldo - self.obtener_precio_ticket() < 0:
            raise NoHaySaldoException
        self.saldo -= self.obtener_precio_ticket()
    def cambiar_estado(self, estado):
        if estado != ACTIVADO and estado != DESACTIVADO:
            raise EstadoNoExistenteException
        self.estado = estado
