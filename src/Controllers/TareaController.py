from Moldels.TareaMoldel import TareaMoldel 

class TareaController:
    def __init__(self):
        self.model=TareaMoldel()
    
    def obtener_lista(self,id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self,id_usuario,titulo,desc,prio,clas):
        if not titulo:
            return False,"El titulo es obligatorio"
        
        self.model.crear(id_usuario,titulo,desc,prio,clas)
        return True, "Tarea guardada"