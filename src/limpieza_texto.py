import numpy as np
import pandas as pd


def year_sure(palabra):
    # quiero garantizar que todas mis entradas terminen con el año además, esta función me garantiza que
    #limpiar fecha no borre por error ningún dato. A lo mejor debería juntarlas ambas
    palabra = str(palabra)
    palabra = palabra.strip()
    palabra.replace('.', '')
    respuesta = str(palabra)
    
    while len(respuesta) > 0:
        
        if respuesta[-1].isnumeric():
            return respuesta
        else:
            #print (respuesta)
            respuesta = respuesta[:-1]
            
    #return palabra



def limpiar_fecha (palabra):
    # primero creo todo lo que voy a necesitar
    palabra = str(palabra)
    fecha_limpia = str()
    
    palabra = palabra.strip()
    for letra in reversed(palabra):
        if letra != ' ':
            fecha_limpia += letra
        else:
            return fecha_limpia[::-1]
    
    return palabra

        
def meses_to_num(palabra):
    
    palabra = str(palabra)
    meses_dict = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04', 'May' : '05', 'Jun' : '06', 'Jul' : '07',
              'Aug' : '08', 'Sep' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12',}
    
    palabra = palabra.strip()
    for key, value in meses_dict.items():
        if key in palabra:
            palabra = palabra.replace(key, value)
    
    palabra = palabra.replace('-', '/')
    return palabra



def especies_tiburon(palabra):
    
    palabra = str(palabra)
    palabra = palabra.strip()
    respuesta = palabra.lower()
    especies_dict = {'white' :'White Shark', 'hammerhead': 'Hammerhead Shark', 'tiger' : 'Tiger Shark', 'nurse' : 'Grey Nurse Shark', 'invalid' : 'Uknowm', 'copper' : 'Cooper Shark', 'cooper' : 'Cooper Shark', 'lemon' : 'Lemon Shark', 'sand' : 'Sand Shark', 'bull' : 'Bull Shark', 'zambezi' : 'Zambezi Shark', 'tawney' : 'Tawney Shark', 'blue' : 'Blue Pointer', 'bronze' : 'Bronze Whaler Shark', 'mako' : 'Mako Shark', 'wobbegong' : 'Wobbegong Shark', 'blacktip' : 'Blatip Shark', 'spinner' : 'Spinner Shark', 'brown' : 'Brown Shark', 'basking' : 'Basking Shark', 'goblin' : 'Goblin Shark'}

    for key, value in especies_dict.items():
        if key in respuesta:
            respuesta = value
            return respuesta
    
    return ' Regular Shark'


def renombrar_columnas(df):
    lista_columnas = list(df.columns)
    columns_newname = [element.strip() for element in lista_columnas]
    columns_newname = [element.replace(' ', '_')   for element in columns_newname]
    return columns_newname




def dayweek_clean(fecha):

    try:
        lista = fecha.split(sep = '/')
        fecha = '-'.join(reversed(lista))
        temp = pd.Timestamp(fecha)
        dia_semana = (temp.dayofweek, temp.day_name())
        return dia_semana[1]
    
    except:
        #print ('hola')
        return None


def columna_year_clean(palabra):

    try:
        palabra = str(palabra)
        palabra = palabra.strip()
        return palabra[-4:]
    
    except:
        return palabra

def decade(palabra):
    try:
        return palabra[:-1] + '0'
    except:
        return palabra


def repetitions(palabra):
    
    try:
        if '//' in palabra:
            palabra = palabra.replace('//', '/')
        return palabra
    
    except:
        return palabra



def quitar_letras(palabra):
    
    if palabra == None:
        return None

    respuesta = str()

    palabra = str(palabra)    
    palabra = palabra.strip()

    for c in palabra:
        if c.isnumeric() or c == '/':
            respuesta += c
    
    if '//' in respuesta:
        respuesta = respuesta.replace('//', '/')

    return respuesta

def impurezas(palabra):
    palabra = palabra.replace('/', '')
    return palabra


def limpiar_type(palabra):
    if palabra == 'Boat' or palabra == 'Boatomg':
        palabra = 'Boating'
        return palabra
    
    return palabra


def limpiar_decades(palabra):
    
    try:
        if palabra < '1000' or palabra > '2021':
            return None
        else:
            return palabra
    except:
        return None


def limpiar_decade(palabra):
    control = int(palabra)
    if control > 1000 and control < 2021:
        return str(palabra)

def limpiar_fatal(palabra):
    palabra = str(palabra)
    palabra = palabra.strip()
    comp = palabra.lower()
    if comp == 'n':
        return 'N'
    elif comp == 'y':
        return 'Y'
    elif palabra == 'UNKNOWN':
        return 'UNKNOWN'
    else:
        return None



###################################################################################################################################################################################
def standar_year(palabra):
    
    aux = str()
    if palabra.isnumeric():
        pass
    else:
        for character in palabra:
            if character.isnumeric:
                aux += character
        palabra = aux
    
    
        
    if len(palabra) == 4:
            return palabra

    elif len(palabra) == 3:
        
        conteo = int(palabra)
        if conteo > 202:
            palabra = '1' + palabra
            return palabra
        else:
            palabra = palabra + '0'
            return palabra

    elif len(palabra) == 2:
        palabra = '19' + palabra
        return palabra
    
    elif len(palabra) == 1:
        palabra = '200' + palabra
        return palabra

    else:
        return None