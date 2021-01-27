import random

#MÉTODO PARA CREAR EL ARCHIVO TXT CON LOS DATOS DE LA TABLA Ticket_Productos

def crear_archivo(ticket_producto):
    f = open ('Ticket_Productos.txt',"w")
    for elemento in ticket_producto:
        f.write('%s \n' % elemento)
    f.close()   

#Listas Vacias
codigo_ticket=[]
codigo_barras=[]
ticket_producto=[]

maximo_producto=1000000
maximo_ticket=5000000
maximo=10000000

#CREAR LA FPK DE CODIGO_PRODUCTO
for j in range(maximo_producto):
    codigo_barras.append(str(j)+'P')

tamaño_codigo=len(codigo_barras)

#CREACION FPK NUMERO DE TICKET
for s in range(maximo_ticket):
    codigo_ticket.append(s)

total_ticket=len(codigo_ticket)


for i in range(maximo):
    aleatorio_ticket=random.randrange(1,total_ticket)
    cantidad=random.randrange(1,10)
    aleatorio_producto=random.randrange(1,tamaño_codigo)
    print(i)
    #ESTAMOS CREANDO OTRA LISTA QUE GUARDARA LOS DIFERENTES DATOS 
    ticket_producto.append(str(codigo_ticket[aleatorio_ticket])+","+codigo_barras[aleatorio_producto]+","+str(cantidad))



crear_archivo(ticket_producto)
