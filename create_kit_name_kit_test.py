import sender_stand_request
import data

def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor

    # String que debe estar en el cuerpo de respuesta
    str_kit = kit_body["name"]



# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El campo del cuerpo de la respuesta coincide con el campo del cuerpo de la solicitud"

# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_name(kit_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400


# Prueba 1. Kit creado con éxito. El parámetro Kit_Body contiene 1 caracter
def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert("a")

# Prueba 2. Kit creado con éxito. El parámetro Kit_Body contiene 511 caracteres
def test_create_kit_511_letter_in_kit_body_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. Error. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_kit_body_get_error_response():
    negative_assert_symbol("")

# Prueba 4. Error. El parámetro Kit_Body contiene 512 caracteres, es mayor que la cantidad permitida
def test_create_kit_512_letter_in_kit_body_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Kit creado con éxito. El parámetro Kit body contiene caracteres especiales
def test_create_kit_has_special_symbol_in_kit_body_get_success_response():
    positive_assert("№%@")

# Prueba 6. Kit creado con éxito. El parámetro Kit body permite espacios
def test_create_kit_has_space_in_kit_body_get_sucess_response():
    positive_assert("A Aaa")

# Prueba 7. Kit creado con éxito. El parámetro Kit body permite números
def test_create_kit_has_number_in_kit_body_get_sucess_response():
    positive_assert("123")

# Prueba 8. Error. Falta el parámetro Kit Body en la solicitud
def test_create_kit_no_kit_body_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable kit_body
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body)

# Prueba 9. Error. Se ha pasado un tipo de parámetro Kit Body diferente (número)
def test_create_kit_number_type_kit_body_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(123)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400