import bcrypt
from .database import Database 

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        # encriptar contraseña 
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario-data.password.encode('utf-8'),salt)
        
        