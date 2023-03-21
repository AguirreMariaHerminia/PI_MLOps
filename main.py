from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
async def ruta():
    return {'API de MHAguirre'}

#cargo los csv para empezar a trabajar
plataformas = pd.read_csv(r'/Users/herminiaaguirre/Desktop/Henry/Proyectos varios/4.PI/MLOps/ML_ETL.csv')

@app.get('/max_duration')
#funcion 1: devulve la pelicula con mayor duracion del año indicado segun cada plataforma
def get_max_duration(año, plataforma,tipo_duracion):
    lista = plataformas[(plataformas['release_year'] == año) & (plataformas['duration_type'] == tipo_duracion) & (plataformas['plataform'] == plataforma)]
    lista = lista.loc[lista['duration_int'] == lista['duration_int'].max()]
    respuesta = lista['title']
    return respuesta

@app.get('/cantidad de peliculas')
#funcion 2: devuelve la cantidad de películas
def get_score_count (plataforma,puntaje,año):
    lista2 = plataformas[(plataformas['plataform'] == plataforma) & (plataformas['score'] > puntaje) & (plataformas['release_year'] == año)]
    respuesta2 = lista2.shape[0]
    return respuesta2

@app.get ('/cantidad de peliculas por plataforma')
#funcion 3: devuelve la cantidad de películas por plataforma
def get_count_plataform(plataform):
    lista3 = plataformas[(plataformas['plataform']==plataform)]
    count = lista3.shape[0]
    return count


@app.get ('/actor mas recurrente por año y por plataforma ')
#funcion 4: 
def get_actor(plataforma, año):
    result = plataformas[(plataformas['plataforma']==plataforma) & (plataformas['release_year']==año)]
    for i in result['cast']:
        if i != 'Sin dato ':
            i=i.replace(', ' , ',')
        else:
            pass
   
    lista4=[]
    for i in result['cast']:
        if i != 'Sin dato':
            s=i.split(',')
            for j in range(len(s)):             
                if s[j] not in lista4:
                    lista4.append(s[j])
                else:
                    pass
        else:
            pass
        
    lista4=list(set(lista4))
    contador = 0
    dict={}
    for i in lista4:
        contador = 0
        for j in result['cast']:
            if i in j.split(','):
                contador+=1
        dict[i]=contador
    if len(dict)==0:
        return 'la plataforma no brinda esta informacion'
    else:
        return max(dict,key=dict.get)
