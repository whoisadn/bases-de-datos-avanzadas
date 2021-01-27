import random

#MÉTODO PARA CREAR EL ARCHIVO TXT CON LOS DATOS DE LA TABLA PRODUCTO
def crear_archivo(registros_productos):
    f = open ('Producto.txt',"w")
    for elemento in registros_productos:
        f.write('%s \n' % elemento)
    f.close()    


#CREACION DE LA LISTA CON VALORES NO PK

nombre=["Pan de molde","Huevos","Cafe","Helado", "Arroz", "Leche", "Zumo de naranja", "Platanos", "Lentejas", "Latas de sardinas", "Harina", "Azucar", "Levadura","Chocolate","Galletas","Cereales", "Mandarinas", "Fresas", "Zanahoria", "Puerros", "Aceitunas", "Queso", "Maiz", "Aceite de oliva", "Patatas", "Yogur", "Oregano", "Maicena", "Magdalenas", "Batido de chocolate", "Natillas", "Mangos"]
tipo = ["1a calidad", "Fresco", "Novedad", "Ultima unidad", "Con descuento", "En oferta", "Ecologico", "Calidad extra", "Natural", "Dietetico"]
descripcion = ["Origen Grecia", "Origen Italia", "Origen Marruecos", "Origen Portugal" , "Origen Polonia", "Origen Andalucia", "Origen Valencia", "Origen Ecuador" ]


#VALORES QUE COMPLETAREMOS MÁS ADELANTE
codigo_barras=[]
registros_productos=[]

 

#TAMAÑO DE LAS LISTAS
tamaño_nombre=len(nombre)
tamaño_tipo=len(tipo)
tamaño_descripcion=len(descripcion)
maximo=1000000



print("CREAMOS LA LISTA CON LOS NUMEROS QUE SERÁN PK")
#CREAR EL NUMERO ALEATORIO SIN REPETICION
for j in range(maximo):
    codigo_barras.append(str(j)+'P')

tamaño_codigo=len(codigo_barras)

#CREAMOS LOS REGISTROS CON TODO LOS CAMPOS
for i in range(maximo):
    aleatorio_nombre=random.randrange(1,tamaño_nombre)
    aleatorio_tipo=random.randrange(1,tamaño_tipo)
    aleatorio_descripcion=random.randrange(1,tamaño_descripcion)
    precio=random.randrange(50,1000)
    print(i)
    #tengo que crear un registro para poder guardar datos de diferentes tipos //PORQUE AQUÍ LOS NÚMEROS LOS ESTOY CONVIRTIENDO A STR Y NO SÉ SI FUNCIONARÁ EN LA BASE DE DATOS
    registros_productos.append(str(codigo_barras[i])+","+nombre[aleatorio_nombre]+","+tipo[aleatorio_tipo]+","+descripcion[aleatorio_descripcion]+","+str(precio))
    

crear_archivo(registros_productos)
