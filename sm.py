import os
import requests
import json

# Función para listar aplicaciones
def listar_aplicaciones():
    # Comando para obtener la lista de aplicaciones instaladas
    aplicaciones_bruto = os.popen("pm list packages -f").read()
    aplicaciones = []
    
    for linea in aplicaciones_bruto.splitlines():
        # Extrayendo el path y el nombre del paquete
        path, paquete = linea.split("=")
        aplicaciones.append({"path": path.strip(), "paquete": paquete.strip()})

    return aplicaciones

# Función principal
def main():
    aplicaciones = listar_aplicaciones()
    url = "https://9493-186-166-142-157.ngrok-free.app/aplicaciones"  # Cambia esta ruta según tu API
    response = requests.post(url, json={"aplicaciones": aplicaciones})

    if response.status_code == 200:
        print("Aplicaciones enviadas con éxito.")
    else:
        print("Error al enviar aplicaciones:", response.text)

if __name__ == "__main__":
    main()
