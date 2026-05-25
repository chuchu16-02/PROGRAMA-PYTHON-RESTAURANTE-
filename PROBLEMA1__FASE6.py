nombre_restaurante = "RESTAURANTE LAS DELICUAS"
print(nombre_restaurante)

menu = [
    ["ARROZ CON LECHE","POSTRE", 2000],
    ["SOPA DE POLLO","SOPAS Y CREMAS", 6000],
    ["LIMONADA","BEBIDAS", 1000],
    ["MANZANA POSTOBON","GASEOSAS",3000],
    ["SUPER PICADA LAS DELICIAS", "COMIDAS RAPIDAS", 20000],
    ["CAFE CON LECHE", "BEBIDAS", 2000],
    ["JUGO NATURAL DE GUANABANA EN JARRA", "BEBIDAS", 4000],
    ["HELADO DE VAINILLA CONO", "POSTRE", 3000],
    ["HAMBURGUESA CON QUESO", "COMIDAS RAPIDAS", 15000],
    ["SALCHIPAPA SUPER", "COMIDAS RAPIDAS", 12000]
     
     ]

def calcular_precio(producto):
    NOMBRE = producto[0]
    CATEGORIA = producto[1] 
    PRECIO = producto[2]

    if CATEGORIA == "COMIDAS RAPIDAS" and PRECIO > 10000:
        return PRECIO * 0.85
    else:
        precio_total = PRECIO
    return precio_total

for producto in menu:
    precio_final = calcular_precio(producto)
    
    NOMBRE= producto[0]
    CATEGORIA = producto[1]
    PRECIO = producto[2]

    DESCUENTO = PRECIO - precio_final

    print("PRODUCTO:", NOMBRE)
    print("CATEGORIA:", CATEGORIA)
    print ("PRECIO UNITARIO:", PRECIO)
    print("PRECIO FINAL: ", precio_final)
    print("-----------------------------")

    if PRECIO != precio_final:
        print("DESCUENTO: 15%")
        print("DESCUENTO APLICADO EXITOSAMENTE")
        print ("-----------------------------")

    else:
        print("DESCUENTO NO APLICADO")

        print ("-----------------------------")

    





    