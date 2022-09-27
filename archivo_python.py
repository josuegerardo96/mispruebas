from enum import Enum, auto # Para darle valores a los componentes
import re                   # Para expresiones regulares
from texttable import Texttable




class pruebas_rendimiento:

    print("Esto es una prueba")
    print("Esto es otra prueba")
    print("ajaaaaaa")






class ComponenteLexico:
    
    tipo : TipoComponente
    texto: str
    linea: str

    def __init__(self, tipo_nuevo: TipoComponente, texto_nuevo: str, linea_en_codigo: str):
        self.tipo = tipo_nuevo
        self.texto = texto_nuevo
        self.linea = linea_en_codigo

    def __str__(self):
        resultado = resultado = f'{self.tipo:30} {self.texto} {self.linea}'
        return resultado




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
