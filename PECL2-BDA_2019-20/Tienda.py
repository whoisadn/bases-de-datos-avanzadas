import random

#MÉTODO PARA CREAR EL ARCHIVO TXT CON LOS DATOS DE LA TABLA TIENDA
def crear_archivo(registros_tienda):
    f = open ('Tienda.txt',"w")
    for elemento in registros_tienda:
        f.write('%s \n' % elemento)
    f.close()    

#CREACION DE LA LISTA CON VALORES NO PK
nombre=["Pedro","Ana","Maria","Esther","Raul","Adrian","Roberto","Cristina","Alejandra","Marcos","Esteban","Adriana","Junior","Tomas","Javier","Fernando","Sandra","Arturo"
        ,"Marta","Laura","Mario"]
ciudad=["Ciudad11","Sevilla","Madrid","Barcelona","Valencia","Granada","Toledo","Palma","Salamanca","Ceuta", "Melilla","Avila"]
barrio=["Laurel","Centro", "Malagueta","Vegueta","Principal","Gracia","Russafa","Albaicin"]
provincia=["Barcelona","Alicante","Malaga","Vizcaya"]


#CREACION DEL REGISTRO QUE TENGO QUE GUARDAR EN EL TXT Y TENDRA EL TOTAL DE REGISTROS, Y PK
registros_tienda=[]
numeros=[]

#TAMAÑO DE LAS LISTAS
tamaño_nombre=len(nombre)
tamaño_ciudad=len(ciudad)
tamaño_barrio=len(barrio)
tamaño_provincia=len(provincia)
maximo=200000

print("CREAMOS LA LISTA CON LOS NUMEROS QUE SERÁN PK")
#CREAR EL NUMERO ALEATORIO SIN REPETICION
for j in range(maximo):
    numeros.append(j)
    

tamaño_numero=len(numeros)
print("CREAMOS LOS REGISTROS CON TODOS LOS CAMPOS")
#CREAMOS LOS REGISTROS CON TODO LOS CAMPOS
for i in range(maximo):
    aleatorio_nombre=random.randrange(1,tamaño_nombre)
    aleatorio_ciudad=random.randrange(1,tamaño_ciudad)
    aleatorio_barrio=random.randrange(1,tamaño_barrio)
    aleatorio_provincia=random.randrange(1,tamaño_provincia)
    print(i)
    #tengo que crear un registro para poder guardar datos de diferentes tipos //PORQUE AQUÍ LOS NÚMEROS LOS ESTOY CONVIRTIENDO A STR Y NO SÉ SI FUNCIONARÁ EN LA BASE DE DATOS
    registros_tienda.append(str(numeros[i])+","+nombre[aleatorio_nombre]+","+ciudad[aleatorio_ciudad]+","+barrio[aleatorio_barrio]+","+provincia[aleatorio_provincia])
    

crear_archivo(registros_tienda)



