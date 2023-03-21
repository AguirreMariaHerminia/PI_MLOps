

<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **Proyecto Individual Nº1 ML_Ops** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>


En este momento les doy la bienvenida a mi primer proyecto individual en el bootcamp, en la etapa de Labs en Henry!
Les mostraré el trabajo realizado desde el rol de una data engineering. 

En primer lugar, comencé el realizando las transformaciones de los datos (ETL), que fueron requeridas específicamente por el equipo de Labs. Las mismas se llevan a cabo para que estén accesibles mediante la API, a cual se accede mediante render.

En segundo lugar,  ejecuté un prceso de EDA a los datos recibidos, para armar el sistema de recomendación de películas con machine learnig. 



<hr>  

<b>Luego de la creación de la API, se espera que pueda responder diferentes consultas 📑: </b>


+ Funcion 1 : devulve la pelicula con mayor duracion del año indicado segun cada plataforma.

    El request debe ser: get_max_duration(año, plataforma,tipo_duracion[min o season])

+ Funcion 2: devuelve la cantidad de películas.

    El request es: def get_score_count (plataforma,puntaje,año)

  
+ Funcion 3: devuelve la cantidad de películas por plataforma

    El request def get_count_plataform(plataform:str):

+ Funcion 4: devuelve en nombre del actor por plataforma y por año, más recurrente.
     
    El request debe ser: get_actor(plataforma, año)  
</ul>

<hr>


En el siguiente link se puede acceder al deploy realizado https://aguirremariaherminia.onrender.com/docs#/


Para realizar este proyecto, primero ingesté y normalicé los datos, lo que se puede ver en los archivos adjuntos en este repositorio</h3>


Link para visualiazar el EDA con la librería sweetviz file:///Users/herminiaaguirre/Desktop/Henry/Proyectos%20varios/4.PI/MLOps/SWEETVIZ_REPORT.html


<b> Para una explicación más profunda sobre cómo funciona el proyecto, les dejo un link al video: **https://youtu.be/6BszacRFFlk**</b>



<p> Muchas gracias por llegar hasta acá! 