import random 

#MÉTODO PARA CREAR EL ARCHIVO TXT CON LOS DATOS DE LA TABLA PRODUCTO
def crear_archivo(tienda_productos):
    f = open ('Tiendas_productos.txt',"w")
    for elemento in tienda_productos:
        f.write('%s \n' % elemento)
    f.close()    



#LISTAS VACIAS
numeros=[]
codigo_barras=[]
tienda_productos=[]


maximo_tienda=200000 #Tienda
maximo_cod_bar=1000000 #Maximo para codigo de barras

print("CREAMOS LA LISTA CON LOS NUMEROS QUE SERÁN PK")
#CREAR LA FPK DE TIENDA
for j in range(maximo_tienda):
    numeros.append(j)
    

tamaño_numero=len(numeros)

#CREAR LA FPK  DE CODIGO_BARRAS
for j in range(maximo_cod_bar):
    codigo_barras.append(str(j)+'P')

tamaño_codigo=len(codigo_barras)

#CREAMOS LOS REGISTROS CON TODO LOS CAMPOS
for i in range(20000000):
    tienda=random.randrange(1,tamaño_numero)
    codigo=random.randrange(1,tamaño_codigo)
    stock=random.randrange(10,200)
    print(i)
    #LISTA CON DIFERENTES REGISTROS
    tienda_productos.append(str(numeros[tienda])+","+str(codigo_barras[codigo])+","+str(stock))
    

crear_archivo(tienda_productos)
