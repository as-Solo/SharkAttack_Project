# SharkAttack_Project

Para este proyecto he utilizado el lenguaje de programación Python.

Como editores de texto me he apoyado en Jupyter Notebook y VsCode.

Las librerías usadas han sido pandas, seaborn, matplot y numpy.

El proyecto básicamente se trataba de recibir un csv, que es un archivo común para el tratamiento de datos, con ciertas singularidades,
y es que el archivo que ha llegado hasta mis manos se ha ido creando y ampliando en múltiples ocasiones por personas muy distintas y que no se
pusieron de acuerdo en como formatear los datos.

Me he creado un dataframe mediante el archivo, ya que es una herramienta de pandas que me permite, visualizar, contrastar, modificar toda la información
y además me lo organiza mediante indices, en forma de tabla.

Lo primero ha sido hacer una criba en cuanto a partes del dataframe a descartar. Una vez reducido lo que iba a ser ruido para mis propósitos he estudiado de qué
forma estaban escritas las entradas de la información que sí era relevante para mi, con el fin de intentar darle un formato homogéneo y poder trabajar sin problemas
con ello. Para esto he creado varias funciones que me iban limpiando las entradas de cada columna hasta que tuviesen un formato adecuado.

Cuando ya estaba todo limpio he exportado mi dataframe a un nuevo archivo csv para poder trabajar con él más tranquilamente en la visualización.

Lo siguiente se trataba de recordar mis hipótesis y encontrar entre las opciones de seaborn y matplot un gráfico que diese una respuesta visual a las mismas.

Por último y de nuevo ayudado por Jupyter como en todas las fases del proyecto, he puesto en común todos el proceso, respondiendo a las hipótesis con los gráficos elegidos.