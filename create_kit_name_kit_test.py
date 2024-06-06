import sender_stand_request
import data


# Crea un nuevo diccionario user_body a partir del diccionario user_body de data.py
def get_kit_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    user_body = data.user_body.copy()
    # Se cambia el valor del parámetro first name
    user_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return user_body


# Nueva función para recuperar el valor contenido en campo authToken en JSON de la respuesta de método post_new_user
def get_user_token(first_name):
    user_body = get_kit_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]


# Función de prueba positiva
def positive_assert(kit_body, auth_token):
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Compara el nombre que se tiene en la variable kit_body con el nombre que trae la respuesta del JSON
    assert kit_body["name"] == response.json()["name"]


# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres

def negative_assert_symbol(name, auth_token):
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(name, auth_token)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_name(kit_body, auth_token):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400


# Prueba 1. Kit creado con éxito. El parámetro Kit_Body contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_user_token("Andrea")
    positive_assert({"name": "a"}, auth_token)

# Prueba 2. Kit creado con éxito. El parámetro Kit_Body contiene 511 caracteres
def test_create_kit_511_letter_in_kit_body_get_success_response():
    auth_token = get_user_token("Andrea")
    positive_assert({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}, auth_token)

# Prueba 3. Error. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_kit_body_get_error_response():
    auth_token = get_user_token("Andrea")
    negative_assert_symbol({"name": ""}, auth_token)

# Prueba 4. Error. El parámetro Kit_Body contiene 512 caracteres, es mayor que la cantidad permitida
def test_create_kit_512_letter_in_kit_body_get_error_response():
    auth_token = get_user_token("Andrea")
    negative_assert_symbol({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}, auth_token)

# Prueba 5. Kit creado con éxito. El parámetro Kit body contiene caracteres especiales
def test_create_kit_has_special_symbol_in_kit_body_get_success_response():
    auth_token = get_user_token("Andrea")
    positive_assert({"name": "№%@"}, auth_token)

# Prueba 6. Kit creado con éxito. El parámetro Kit body permite espacios
def test_create_kit_has_space_in_kit_body_get_sucess_response():
    auth_token = get_user_token("Andrea")
    positive_assert({"name": "A Aaa"}, auth_token)

# Prueba 7. Kit creado con éxito. El parámetro Kit body permite números
def test_create_kit_has_number_in_kit_body_get_sucess_response():
    auth_token = get_user_token("Andrea")
    positive_assert({"name": "123"}, auth_token)

# Prueba 8. Error. Falta el parámetro Kit Body en la solicitud
def test_create_kit_no_kit_body_get_error_response():
    auth_token = get_user_token("Andrea")
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable kit_body
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body, auth_token)

# Prueba 9. Error. Se ha pasado un tipo de parámetro Kit Body diferente (número)
def test_create_kit_number_type_kit_body_get_error_response():
    auth_token = get_user_token("Andrea")
    negative_assert_symbol({"name": 123}, auth_token)