# Clasificador de idiomas con Naive Bayes

Repositorio de un clasificador de idiomas implementado mediante Bayes ingenuo en Python.
Funciona con dos códigos principales, que deben ejecutarse en el orden en el que se describen:

1. `generadf.py` se encarga de generar un DataFrame con el conteo de los ngramas por idioma a partir de los archivos:
   * `ingles.txt`
   * `espanol.txt`
   * `portugues.txt`

   El DataFrame se guarda como valores separados por comas en el archivo `tabla.csv`. (Este archivo se genera para que el conteo de los
los documentos fuente únicamente se realice una vez y se haga independiente de la entrada que se quiera probar).

1. `clasificaidioma.py` realiza los cálculos de probabilidades necesarios para determinar el idioma del documento en el archivo
`entrada.txt`, utilizando el DataFrame guardado en `tabla.csv`. Como salida, se imprime en consola el idioma que tiene la mayor
probabilidad con base en los cálculos.

__NOTA:__ Los archivos de entrada y documentos de los idiomas se pueden modificar.
