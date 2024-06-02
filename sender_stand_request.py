import configuration
import requests
import data

def post_new_user(body):# Funcion para crear nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # Concatenación de URL base y ruta.
                         json=body,# inserta el cuerpo de solicitud
                         headers=data.headers) # inserta los encabezados

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body):# Funcion para crear kit
    # Realiza una solicitud POST para crear kits
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, # Concatenación de URL base y ruta.
                         json=kit_body,# inserta el cuerpo de solicitud
                         headers=data.headers)# inserta los encabezados

response = post_new_client_kit(data.kit_body);
print(response.status_code)
print(response.json())

