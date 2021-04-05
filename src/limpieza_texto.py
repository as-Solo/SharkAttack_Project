import numpy as np
import pandas as pd
import seaborn as sns


def year_sure(palabra):
    """
    Delete all the character at the end of the string until it founds a digit
    Args:
        object dataframe value
    Returns:
        String
    """
    
    palabra = str(palabra)
    palabra = palabra.strip()
    respuesta = str(palabra)
    
    while len(respuesta) > 0:
        #print (respuesta)
        if respuesta[-1].isnumeric():
            return respuesta
        else:
            respuesta = respuesta[:-1]



def limpiar_fecha (palabra):
    """
    Delete all character previous the last 'space' character
    Args:
        object dataframe value
    Returns:
        String
    """
    
    palabra = str(palabra)
    fecha_limpia = str()
    
    palabra = palabra.strip()
    
    for letra in reversed(palabra):
        
        if letra != ' ':
            fecha_limpia += letra
            #print(fecha_limpia)
            
        else:
            #print (fecha_limpia)
            return fecha_limpia[::-1]
    
    return palabra


def meses_to_num(palabra):
    """
    Turn the name of the months to digit and replace '-' for '/'
    Args:
        object dataframe value
    Returns:
        String
    """
    
    palabra = str(palabra)
    meses_dict = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04', 'May' : '05', 'Jun' : '06', 'Jul' : '07',
              'Aug' : '08', 'Sep' : '09', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12',}
    
    palabra = palabra.strip()
    for key, value in meses_dict.items():
        if key in palabra:
            palabra = palabra.replace(key, value)
    
    palabra = palabra.replace('-', '/')
    return palabra



def dayweek_clean(fecha):
    """
    Evaluate de day of the week in a date
    Args:
        object dataframe value
    Returns:
        String
    """

    try:
        lista = fecha.split(sep = '/')
        fecha = '-'.join(reversed(lista))
        temp = pd.Timestamp(fecha)
        dia_semana = (temp.dayofweek, temp.day_name())
        return dia_semana[1]
    
    except:
        #print ('hola')
        return None


    
def quitar_suciedad(palabra):
    """
    Remove '/' characters at the beggining and the end in a string
    Args:
        object dataframe value
    Returns:
        String
    """
    palabra = palabra.strip('/')
    return palabra


def columna_year(palabra):
    """
    Return the last four digits for the value taken if this value have 4 or more characters
    Args:
        object dataframe value
    Returns:
        String
    """
    if len(palabra) >= 4:
        return palabra[-4:]


def clean_year(palabra):
    """
    Remove all the data celds if the value is not in range 1000-2021 and remove all the '.' characters
    Args:
        object dataframe value
    Returns:
        String
    """
    palabra = str(palabra)
    palabra = palabra.replace('.', '')
    if palabra < '1000' or palabra > '2021':
        return None
    else:
        return palabra


def clean_year_suciedad(palabra):
    """
    Remove all the data celds if the length of the value is less than 4
    Args:
        object dataframe value
    Returns:
        String
    """

    try:
        if len(palabra) < 4:
            return None
        else:
            return palabra
    except:
        pass


def decade(palabra):
    """
    Return the argument taken changing the last character for a '0'
    Args:
        object dataframe value
    Returns:
        String
    """
    try:
        return palabra[:-1] + '0'
    except:
        return palabra



def limpiar_fatal(palabra):
    """
    Return Y, N, or UNKNOWN depends of the argument taken if argument doesn't match return None
    Args:
        object dataframe value
    Returns:
        String
    """
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




def limpiar_type(palabra):
    """
    Turns to Boating any argument calling boat or boatomg
    Args:
        object dataframe value
    Returns:
        String
    """
    if palabra == 'Boat' or palabra == 'Boatomg':
        palabra = 'Boating'
        return palabra
    
    return palabra



def especies_tiburon(palabra):
    """
    Looks for coincidents in the argument and return a formated Name
    Args:
        object dataframe value
    Returns:
        String
    """
    
    palabra = str(palabra)
    palabra = palabra.strip()
    respuesta = palabra.lower()
    especies_dict = {'white' :'White Shark', 'hammerhead': 'Hammerhead Shark', 'tiger' : 'Tiger Shark', 'nurse' : 'Grey Nurse Shark', 'invalid' : 'Uknowm', 'copper' : 'Cooper Shark', 'cooper' : 'Cooper Shark', 'lemon' : 'Lemon Shark', 'sand' : 'Sand Shark', 'bull' : 'Bull Shark', 'zambezi' : 'Zambezi Shark', 'tawney' : 'Tawney Shark', 'blue' : 'Blue Pointer', 'bronze' : 'Bronze Whaler Shark', 'mako' : 'Mako Shark', 'wobbegong' : 'Wobbegong Shark', 'blacktip' : 'Blatip Shark', 'spinner' : 'Spinner Shark', 'brown' : 'Brown Shark', 'basking' : 'Basking Shark', 'goblin' : 'Goblin Shark'}

    for key, value in especies_dict.items():
        if key in respuesta:
            respuesta = value
            return respuesta
    
    return ' Regular Shark'