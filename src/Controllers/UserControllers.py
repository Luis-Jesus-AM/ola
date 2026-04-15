from Models.UserMoldel import UsuarioModel
from Models.SchemasMoldel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            # validar datos con el schem,a 
            nuevo_usuario = UsuarioSchema(nombre=nombre, emai=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "usuario creado correctamente "
        except ValidationError as e: 
    # retoma el primer erro de validacion encontrado 
            return False, e.errors()[0]['msg']