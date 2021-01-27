import random

#MÉTODO PARA CREAR EL ARCHIVO TXT CON LOS DATOS DE LA TABLA PRODUCTO
def crear_archivo(registros_ticket):
    f = open ('Ticket.txt',"w")
    for elemento in registros_ticket:
        f.write('%s \n' % elemento)
    f.close()   

#Listas Vacias
registros_ticket=[]
codigo_trabajador=[]
codigo_ticket=[]
fecha=[]


maximo_trabajador=1000000
maximo_ticket=5000000


#CREAR LA FPK DE CODIGO_TRABAJADOR
for t in range(maximo_trabajador):
    codigo_trabajador.append((t))

tamaño_trabajador=len(codigo_trabajador)

#CREACION PK NUMERO DE TICKET
for s in range(maximo_ticket):
    codigo_ticket.append(s)

total_ticket=len(codigo_ticket)

#CREACIÓN DE FECHA
for i in range(100):
    dia = str(random.randrange(1, 31))
    mes = str(random.randrange(1, 12))
    año = '2019'
    fecha.append(dia +'/'+mes+'/'+año)

tamaño_fecha=len(fecha)

for i in range(maximo_ticket):
    importe=random.randrange(100,10000)
    numero_fecha=random.randrange(1,tamaño_fecha)
    trabajador=random.randrange(1,tamaño_trabajador)
    print(i)
    #ESTAMOS CREANDO OTRA LISTA QUE GUARDARA LOS DIFERENTES DATOS 
    registros_ticket.append(str(codigo_ticket[i])+","+str(fecha[numero_fecha])+","+str(importe)+","+str(trabajador))



crear_archivo(registros_ticket)
