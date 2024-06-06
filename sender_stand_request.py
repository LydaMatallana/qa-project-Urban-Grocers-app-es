import requests
import configuration
import data



def post_new_user(body):# Funcion para crear nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,# Concatenación de URL base y ruta.
                         json=body) # inserta el cuerpo de solicitud


def post_new_client_kit(kit_body, auth_token): # Funcion para crear un kit
    headers = {
        "Authorization": f"Bearer {auth_token}" # Concatenar el valor de authToken al encabezado
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, # Concatenación de URL base y ruta.
                         json=kit_body, # inserta el cuerpo de solicitud
                         headers=headers) # inserta los encabezados









