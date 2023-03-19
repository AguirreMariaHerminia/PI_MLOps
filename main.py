from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
async def ruta():
    return {'API de MHAguirre'}

#cargamos los csv para empezar a trabajar 
plataformas = pd.read_csv('./ML_ETL.csv')

@app.get('/max_duration')
#funcion 1 : devulve la pelicula con mayor duracion del año indicado segun cada plataforma
def get_max_duration(año:int,tipo_duracion:str, platforma:str):
    lista = plataformas[(plataformas['release_year'] == año) & (plataformas['duration_type'] == tipo_duracion) & (plataformas['plataform'] == platforma)]
    lista = lista.loc[lista['duration_int'] == lista['duration_int'].max()]
    respuesta = lista['title']
    return respuesta

@app.get('/cantidad de peliculas')
def get_score_count (plataforma:str,puntaje:float,año:int):
    lista2 = plataformas[(plataformas['plataform'] == plataforma) & (plataformas['score'] > puntaje) & (plataformas['release_year'] == año)]
    respuesta2 = lista2.shape[0]
    return respuesta2

@app.get ('/cantidad de peliculas por plataforma')
def get_count_plataform(plataform:str):
    lista3 = plataformas[(plataformas['plataform']==plataform)]
    count = lista3.shape[0]
    return count


@app.get ('/actor mas recurrente por año y por plataforma ')
def get_actor(plataform:str, año:int):
    result = plataformas[(plataformas['plataform']==plataform) & (plataformas['release_year']==año)]
    result['cast'] = np.replace(np.nam, 'Sin dato')
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
