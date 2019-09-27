import pandas as pd

def ngramas(num, documento):
        """
        Separa el documento en ngramas de num caracteres.
        Regresa una lista con los ngramas obtenidos.

        Parametros:
        num       : cantidad de caracteres por ngrama
        documento : documento que se quiere dividir en ngramas.
        """
        salida, texto = [], ''
        for linea in documento.readlines():
                texto += linea
        texto = texto.replace('\n', ' ')
        texto = eliminasimbolos(texto)
        texto = texto.lower()
        for i in range(0,len(texto)-num):
                salida.append(texto[i:i+num])
        return salida

def eliminasimbolos(texto):
        """
        Elimina los simbolos innecesarios a partir de su Unicode.
        Regresa el texto limpio.

        Parametros:
        texto : texto del que se quieren eliminar simbolos
        """
        for c in texto:
                if ord(c) in range(34,39) or ord(c) in range(40,63) or ord(c) in range(64,65) or ord(c) in range(91,97) or ord(c) in range(123,161) or ord(c) in range(162,191):
                        texto = texto.replace(c, '')
        return texto

def crearbanco(ngramas):
        """
        Genera un diccionario con los ngramas como llaves y su conteo en su valor.

        Parametros:
        n     : lista con los ngramas
        """
        banco = {}
        for grama in ngramas:
                if grama not in banco.keys():
                        banco[grama] = 1
                else: 
                        banco[grama] += 1
        return banco 

def creartabla(ing, esp, port):
        """
        Genera un dataframe con el conteo de los tres idiomas en una misma tabla.
        Si algun ngrama no aparece en el idioma se le asigna un conteo de cero.

        Parametros:
        ing     : diccionario de los ngramas en ingles
        esp     : diccionario de los ngramas en espaniol
        port    : diccionario de los ngramas en portugues
        """
        llaves = list(ing.keys()) + list(esp.keys()) + list(port.keys())
        llaves = list(set(llaves))
        llaves.sort()
        counti, counte, countp = [], [], []
        for k in llaves:
                if k in ing.keys():
                        counti.append(ing[k])
                else:
                        counti.append(0)
                if k in esp.keys():
                        counte.append(esp[k])
                else:
                        counte.append(0)
                if k in port.keys():
                        countp.append(port[k])
                else:
                        countp.append(0)
        dic = {'count_ingles':counti, 'count_esp':counte, 'count_port':countp}
        tabla = pd.DataFrame(dic)
        tabla.index = llaves
        return tabla

def main():
        """
        Ejecucion de las funciones en un main, al terminar se exporta el DataFrame a un .csv,
        para no repetir este proceso en cada ejecucion y poder usar esa misma tabla en clasificaidioma.py.
        """
        numgramas = 3

        bancoing = crearbanco(ngramas(numgramas, open("ingles.txt", encoding = "utf8")))
        bancoesp = crearbanco(ngramas(numgramas, open("espanol.txt", encoding = "utf8")))
        bancoport = crearbanco(ngramas(numgramas, open("portugues.txt", encoding = "utf8")))

        df = creartabla(bancoing, bancoesp, bancoport)
        export_csv = df.to_csv("tabla.csv", index = True, header = True)

main()
