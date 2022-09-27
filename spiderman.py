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

    INTRODUCCION    = auto()
    DESARROLLO      = auto()
    CONCLUSION      = auto()
    ABRECORCHETE    = auto()
    CIERRACORCHETE  = auto()
    ABREPARENTESIS  = auto()
    CIERRAPARENTESIS= auto()

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


