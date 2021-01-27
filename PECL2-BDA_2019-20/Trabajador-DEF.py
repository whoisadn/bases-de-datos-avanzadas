import random
#MÉTODO PARA CREAR EL TXT CON LOS DATOS DE LA TABLA TRABAJADOR
def crear_archivo(registros_trabajador):
    f = open ('trabajador.txt',"w")
    for elemento in registros_trabajador:
        f.write('%s \n' % elemento)
    f.close()    

#LISTAS CON VALORES NO PK
nombre=["Pedro","Ana","Maria","Esther","Raul","Adrian","Roberto","Cristina","Alejandra","Marcos","Esteban","Adriana","Junior","Tomas","Javier","Fernando","Sandra","Arturo","Adina","Victoria","Marta","Laura","Mario"]
apellidos=["Casas","Apellido2","De la Mata","De Palma","Da Casa","Garcia","Gonzales","Roales", "Perez", "Sanchez", "Gomez", "Fernandez", "Moreno", "Moron", "Blanco", "Jimenez","Apellido3","Apellidos4"]
puesto=["Reponedor", "Encargado", "Cajero", "Almacen", "Responsable seccion", "Degustacion", "Otros" ]

#Listas Vacias
id_tienda=[]
registros_trabajador=[]
codigo_trabajador=[]

#LONGITUD DE LAS LISTAS INICIALES
tamaño_nombre=len(nombre)
tamaño_apellidos=len(apellidos)
tamaño_puesto=len(puesto)



#FPK DE ID_TIENDA
for j in range(1000000):
    id_tienda.append(j)
tamaño_tienda=len(id_tienda)
#CREAR LA PK DE CODIGO_TRABAJADOR
for t in range(1000000):
    codigo_trabajador.append((t))

#CREAMOS LOS REGISTROS CON TODO LOS CAMPOS
for i in range(1000000):
    aleatorio_nombre=random.randrange(1,tamaño_nombre)
    aleatorio_apellidos=random.randrange(1,tamaño_apellidos)
    aleatorio_puesto=random.randrange(1,tamaño_puesto)
    salario=random.randrange(1000,5000)
    dni=random.randrange(100000000,999999999)
    aleatorio_tienda=random.randrange(1,tamaño_tienda)
    print(i)
    #ESTAMOS CREANDO OTRA LISTA QUE GUARDARA LOS DIFERENTES DATOS 
    registros_trabajador.append(str(codigo_trabajador[i])+","+str(dni)+","+nombre[aleatorio_nombre]+","+apellidos[aleatorio_apellidos]+","+puesto[aleatorio_puesto]+","+str(salario)+","+str(id_tienda[aleatorio_tienda]))
    

crear_archivo(registros_trabajador)
