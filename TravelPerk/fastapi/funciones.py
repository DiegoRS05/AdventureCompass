from datetime import datetime
import pandas as pd
from models import TravelData

#COMPROBACIONES:

# class coche():
#     departureDate="12/03/2024"
#     returnDate="14/03/2024"
#     departureCity="Milan"
#     arrivalCity="London"

def travelWith(travel_data: TravelData):
    #Cargo el csv del estatico
    df=pd.read_csv('static/database.csv')
    #Filtro por ciudad de destino, de salida y fecha de salida
    df=df[(df["Departure City"]==travel_data.departureCity)&(df["Arrival City"]==travel_data.arrivalCity)]
    df=df[df["Departure Date"]==travel_data.departureDate]
    #Extraigo la columna del dataFrame en forma de una serie
    s=pd.Series(df["Traveller Name"])
    #Creo una lista
    list=[]
    #Recorro la seire y con el metodo apend introduzco los usuarios en la lista
    for element in s:
        list.append(element)
    #Por último retorno la lista
    return list


def howmanyDays(travel_data: TravelData):
    #Empleamos datatimes para guardar las fechas que anteriormente tenemos como strings
    fecha_dp=datetime.strptime(travel_data.departureDate,'%d/%m/%Y')
    fecha_rt=datetime.strptime(travel_data.returnDate,'%d/%m/%Y')
    #El valor absoluto devuelve un objeto de tipo timedelta
    #Extraemos los dias del objeto timedelta con el método days
    return abs(fecha_rt-fecha_dp).days


#Esta función es un calco salvo por dos matices, especificados abajo
def returnWith(travel_data: TravelData):
    #Cargo el csv del estatico
    df=pd.read_csv('static/database.csv')
    #Aqui si nos damos cuenta ahora departure city para filtrar en la bd sera arrival city, lo mismo con arrival city
    df=df[(df["Departure City"]==travel_data.arrivalCity)&(df["Arrival City"]==travel_data.departureCity)]
    df=df[df["Departure Date"]==travel_data.returnDate]
    #Extraigo la columna del dataFrame en forma de una serie
    s=pd.Series(df["Traveller Name"])
    #Creo una lista
    list=[]
    #Recorro la serie y con el metodo apend introduzco los usuarios en la lista
    for element in s:
        list.append(element)
    #Por último retorno la lista
    return list



def activities(travel_data: TravelData): 
    #Cargo el csv del estatico 
    df=pd.read_csv('static/database.csv') 
    #Filtro por ciudad de destino, de salida y fecha de salida 
    df=df[(df["Arrival City"]==travel_data.arrivalCity)] 
    df=df[(df["Departure Date"]>travel_data.departureDate)&(df["Return Date"]<travel_data.returnDate)] 
    #Extraigo la columna del dataFrame en forma de una serie 
    s=pd.Series(df["Activities"]) 
    #Creo una lista 
    list=[] 
    for element in s:
        for i in element.split(","):

            list.append(i.strip())
    list=set(list)
    #Por último retorno la lista 
    return list

