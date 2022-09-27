from enum import Enum, auto # Para darle valores a los componentes
import re                   # Para expresiones regulares
from texttable import Texttable



<<<<<<< HEAD
class Naruto():
    Naruto
    Sasuke
    Sakura




=======
class OnePiece():
    Luffy
    Zoro
    Nami
    Sanji
=======
>>>>>>> 68de19badca6dae4e13e44d6e61ee1e67f4b684d
class Animalitos():
    spider
    bat
    goku
    naruto







class Manga():
    Naruto
    One Piece
    Dragon ball


class Explorador:

    descriptores_componentes = [

        (TipoComponente.INICIOCUENTO,   r'InicioCuento'),
        (TipoComponente.FECHAPUBLICACION,r'FechaPublicacion'),
        (TipoComponente.AUTOR,          r'Autor'),
        (TipoComponente.TITULO,         r'Titulo'),
        (TipoComponente.TIPOCUENTO,     r'TipoCuento'),

        (TipoComponente.INTRODUCCION,   r'Introduccion'),
        (TipoComponente.DESARROLLO,     r'Desarrollo'),
        (TipoComponente.CONCLUSION,     r'Conclusion'),
        (TipoComponente.FINCUENTO,      r'FinCuento'),

        (TipoComponente.COMENTARIO,     r'\$\w*\n'),
        (TipoComponente.ESPACIOS,        r'\s'),
        (TipoComponente.TEXTO,          r'[a-zA-ZÑñÁáÉéÍíÓóÚú]([a-zA-ZÑñÁáÉéÍíÓóÚú])*'),
        (TipoComponente.DOSPUNTOS,      r':'),
        (TipoComponente.PUNTUACION,     r'[.,;]'),
        (TipoComponente.COMILLA,        r'"'),

        (TipoComponente.ABRECORCHETE,   r'{'),
        (TipoComponente.CIERRACORCHETE, r'}'),

        (TipoComponente.ABREPARENTESIS,   r'\('),
        (TipoComponente.CIERRAPARENTESIS, r'\)'),
        
        (TipoComponente.NEGRITA,        r'negrita'),
        (TipoComponente.ITALICA,        r'italica'),
        (TipoComponente.TAMANOLETRA,    r'TamanoLetra'),
        
        (TipoComponente.CONDICIONAL,    r'if'),
        (TipoComponente.REPETICION,     r'while'),
        # (TipoComponente.NUMEROS,        r'[1-9]+'),
        (TipoComponente.ENTEROS,        r'[1-9]([0-9])*'),

        (TipoComponente.VAR,            r'var'),
        (TipoComponente.FUNCION,        r'funcion'),
        (TipoComponente.IDENTIFICADOR,  r'_[a-zA-Z]([a-zA-z0-9])*'),

        (TipoComponente.OPERADORES,     r'[><=]')
    ]

    def __init__(self, contenido_archivo):
        self.texto = contenido_archivo
        self.componentes = []

    
    
    def explorar(self):
        n_linea = 1
        for linea in self.texto:
            resultado = self.procesar_linea(linea, n_linea)
            self.componentes = self.componentes + resultado
            n_linea += 1


    def imprimir_componentes(self):
        tt = Texttable()
        tt.add_row(["Tipo de componente léxico", "Texto del componente léxico", "línea"])
        for componente in self.componentes:
            # print(componente)
            tt.add_row([str(componente.tipo), str(componente.texto), str(componente.linea)])
        
        print("\n\n")
        print("Explorador para lenguajes de programación (Cuento) ")
        print(tt.draw())


ME GUSTAAAAAAA EL PESCADO
