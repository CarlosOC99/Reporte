import csv 
import json

total = 0
sin_descripcion = 0
estado_activo = 0
estado_inactivo = 0

with open('usuarios.csv') as f:
    reader = csv.reader(f)
    print("\nContenido del documento:")
    for row in reader:
        total += 1

        # Asegurarse de que hay al menos 4 columnas
        if len(row) < 4:
            continue

        id, nombre, descripcion, estado = row

        if descripcion.strip() == '':
            sin_descripcion += 1

        if estado.lower() == 'activo':
            estado_activo += 1
        elif estado.lower() == 'inactivo':
            estado_inactivo += 1
        print("id: ", row[0],"nombre: ", row[1],"descripcion: ", row[2],"estado: ", row[3].format(row[0], row[1], row[2], row[3]))
        

# Estructura del resumen
resumen = {
    "total_elementos": total,
    "sin_descripcion": sin_descripcion,
    "estado": {
        "activo": estado_activo,
        "inactivo": estado_inactivo
    }
}

with open('resumen.json', 'w', encoding='utf-8') as json_file:
    json.dump(resumen, json_file, ensure_ascii=False, indent=4)

print("\nResumen guardado en 'resumen.json'")