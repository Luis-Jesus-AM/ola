from src.models.TareaModel import TareaModel 

class TareaControlller: 
    def __init__(self):
        self.model = TareaModel()
        
    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self, id_usuario, titulo, desc, prio, clas):
        if not titulos:
            return False, "El titulos es obligatorio"
        self.model.crear(id_usuarioo, titulo, desc, prio, clas)
        return True, "Tarea guardada"