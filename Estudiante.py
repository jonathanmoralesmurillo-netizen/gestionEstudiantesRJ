class Estudiante:
    def __init__(self,id,nombre, nota):
        if id < 0:
            raise ValueError("El id debe ser un numero")
        if not isinstance(nota, (int, float)) or nota < 0 or nota > 100:
            raise ValueError("El nota debe ser un numero")
        self.id = id
        self.nombre = nombre
        self.nota = nota
    def getId(self)-> int:
        return self.id
    def getNombre(self)-> str:
        return self.nombre
    def getNota(self)-> float:
        return self.nota
    def setId(self, id : int)->None:
        self.id=id
    def setNombre(self,nombre : str )->None:
        self.nombre=nombre
    def setnota(self,nota :float )->None:
        self.nota=nota
    def to_dict(self)->dict:
        return {
            "id":self.id,
            "nombre":self.nombre,
            "nota":self.nota
        }

    def __str__(self)->str:
        return f"Id:{self.id}, Nombre: {self.nombre}, Nota: {self.nota} "

"""
class Estudiante {
     -id: int
     - nombre: str
     - nota: float
     
+ __init__(id: int, nombre: str, nota: float)

+get_id() int
+ get_nombre() str
+ set_nombre(nombre: str) void
+ get_nota() float
+ set_nota(nota: float) void
+ to_dict() dict
+ __str__()
str
}
"""