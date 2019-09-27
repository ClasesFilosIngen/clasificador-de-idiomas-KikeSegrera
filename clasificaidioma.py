from generadf import ngramas
import pandas as pd
import math as m

def calculaprob(ngramas, df, sumas, x, k):
        """
        Calcula las probabilidades P(idioma|documento) para los tres idiomas.
        Se utiliza el logaritmo en el calculo para evitar un underflow a cero, ya que las probabilidades son pequenias.

        Parametros:
        ngramas : lista de ngramas que componen al documento.
        df      : data frame con el conteo de los ngramas de los tres idiomas.
        sumas   : suma de los conteos de las columnas.
        x       : numero de clases.
        k       : parametro para el aplanado de Laplace.

        
        """
        probing = m.log(df['count_ingles'].gt(0).sum()+k) - m.log(len(list(df.index))+k*x)
        probesp = m.log(df['count_esp'].gt(0).sum()+k) - m.log(len(list(df.index))+k*x)
        probport = m.log(df['count_port'].gt(0).sum()+k) - m.log(len(list(df.index))+k*x)
        for n in ngramas:
                if n in list(df.index):
                        probing += m.log(list(df.loc[n])[0]+k) - m.log(sumas[0]+k*len(list(df.index)))
                        probesp += m.log(list(df.loc[n])[1]+k) - m.log(sumas[1]+k*len(list(df.index)))
                        probport += m.log(list(df.loc[n])[2]+k) - m.log(sumas[2]+k*len(list(df.index)))
        return [probing, probesp, probport]

def clasificaidioma(probidiomas):
        """
        Imprime el idioma que tenga la probabilidad mas grande.

        Parametros:
        probidiomas : lista con las probabilidades de cada idioma.
        """
        idioma = probidiomas.index(max(probidiomas))
        if idioma == 0:
                print("\nEl documento esta en ingles");
        elif idioma == 1:
                print("\nEl documento esta en espaniol");
        else:
                print("\nEl documento esta en portugues");

def main():
        """
        Ejecucion de las funciones en un main, donde se recibe el DataFrame generado en generadf.py
        y la entrada que se quiere clasificar.
        """
        numgramas = 3
        x = 3
        k = 1
        df = pd.read_csv("tabla.csv", index_col = 0)
        probidiomas = calculaprob(ngramas(numgramas, open("entrada.txt", encoding = "utf8")), df, list(df.sum()), x, k)
        clasificaidioma(probidiomas)
        
main()
