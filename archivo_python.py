from enum import Enum, auto # Para darle valores a los componentes
import re                   # Para expresiones regulares
from texttable import Texttable



<<<<<<< HEAD
class Comics():
    Superman
    Batman
    El hombre araña
    iron man
=======
class Animalitos():
    spider
    bat
    goku
    naruto
>>>>>>> a8d4e10e03ed3caa383374d7d2dde86ca866bd6f





class TipoComponente(Enum):
    COMENTARIO      = auto()
    TEXTO           = auto()
    DOSPUNTOS       = auto()
    ESPACIO         = auto()
    PUNTUACION      = auto()
    COMILLA         = auto()
    
    INICIOCUENTO    = auto()
    FECHAPUBLICACION= auto()
    AUTOR           = auto()
    TITULO          = auto()
    TIPOCUENTO      = auto()

    NEGRITA         = auto()
    ITALICA         = auto()
    TAMANOLETRA     = auto()

    CONDICIONAL     = auto()
    REPETICION      = auto()
    # NUMEROS         = auto()
    ENTEROS         = auto()

    VAR             = auto()
    FUNCION         = auto()
    IDENTIFICADOR   = auto()

    OPERADORES      = auto()
    SALTOLINEA      = auto()
    TABULAR         = auto()
    ESPACIOS        = auto()

    FINCUENTO       = auto()
    ERROR           = auto()




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



    def procesar_linea(self,linea,n_linea):

        lineAlInicio = linea

        componentes = []

        while(linea != ""):
            
            for tipo_componente, regex in self.descriptores_componentes:

                respuesta = re.match(regex,linea)

                if respuesta is not None:

                    if tipo_componente is not TipoComponente.COMENTARIO and tipo_componente is not TipoComponente.ESPACIOS:
                        nuevo_componente = ComponenteLexico(tipo_componente, respuesta.group(), str(n_linea))
                        componentes.append(nuevo_componente)
                
                    if respuesta.end == 0:
                        linea = ""
                    else:
                        linea = linea[respuesta.end():]
                    break

            if lineAlInicio == linea:
                componente_error = ComponenteLexico(TipoComponente.ERROR, linea, str(n_linea))
                componentes.append(componente_error)
                break

            lineAlInicio = linea

        return componentes
