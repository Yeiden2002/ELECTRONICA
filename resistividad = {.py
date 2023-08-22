#Resistencia en un conductor electrico
#R=p*(L/S)
#este programa va a contener caract de materiales precargadas
#es un arreglo agregamos nombre del material y resistividad
resistividad = {
    "Al": (0.028, "Aluminio"),
    "Cu": (0.017, "Cobre"),
    "Au": (0.023, "Oro"),
    "Sn": (0.12, "Estaño"),
    "Hg": (0.96, "Mercurio"),
    "Pt": (0.11, "Platino"),
    "Fe": (0.13, "Hierro"),
    "Zn": (0.061, "Zinc"),
    "Ag": (0.16, "Plata")
}

L = float(input("Ingresa la longitud del conductor en [m]: "))
S = float(input("Ingresa la sección del conductor en [mm2]: "))
material = input("Ingresa el símbolo del material: ").strip() 


if material in resistividad:
    p = resistividad[material][0]
    print("Resistividad de ", resistividad[material][1], " = [ohm.mm1/m]")
    
    if S == 0:
        print("Error, la sección no puede ser cero, ingresa una sección diferente.")
    else:
        R = p * L / S
        print("La resistencia es de", R, "ohms")
else:
    print("Material no encontrado en la base de datos.")
