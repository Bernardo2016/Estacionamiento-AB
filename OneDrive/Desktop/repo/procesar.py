import csv
import datetime
import sys

archivo_entrada = "datos.csv"
archivo_salida = "aprobados.csv"
archivo_log = "backup.log"

version = sys.argv[1] if len(sys.argv) > 1 else "v1.0-manual"

try:
    with open(archivo_entrada, mode='r', encoding='utf-8') as file:
        lector = csv.DictReader(file)
        filtrados = [fila for fila in lector if int(fila['Calificacion']) >= 70]

    with open(archivo_salida, mode='w', encoding='utf-8', newline='') as file:
        escritor = csv.DictWriter(file, fieldnames=lector.fieldnames)
        escritor.writeheader()
        escritor.writerows(filtrados)

    resultado = f"Exito: Se filtraron {len(filtrados)} datos (alumnos aprobados)."
except Exception as e:
    resultado = f"Error durante el procesamiento: {str(e)}"

fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{fecha_hora}] Archivo: {archivo_entrada} | Resultado: {resultado} | Version: {version}\n"

with open(archivo_log, mode='a', encoding='utf-8') as log:
    log.write(log_entry)

print(f"Proceso finalizado. {resultado}")
