from prefect import task, flow
import requests

class colores:
    RESET = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    INVERTIDO = '\033[7m'
    
    # Colores de texto
    NEGRO = '\033[30m'
    ROJO = '\033[31m'
    VERDE = '\033[32m'
    AMARILLO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    BLANCO = '\033[37m'
    
    # Colores de fondo
    BG_NEGRO = '\033[40m'
    BG_ROJO = '\033[41m'
    BG_VERDE = '\033[42m'
    BG_AMARILLO = '\033[43m'
    BG_AZUL = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_BLANCO = '\033[47m'

class Drink:
    def __init__(self, data):
        self.name = data['strDrink']
        self.category = data['strCategory']
        self.isAlcoholic = True if data['strAlcoholic'] == 'Alcoholic' else False
        self.instructions = data['strInstructions']
        self.ingredient = []
        self.measure = []
        i = 1
        while data['strIngredient' + str(i)]:
            self.ingredient.append(data['strIngredient' + str(i)])
            i+=1
        i = 1
        while data['strMeasure' + str(i)]:
            self.measure.append(data['strMeasure' + str(i)])
            i+=1


@task
def obtener_json(url):
    try:
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Devolver el JSON
            return response.json()
        else:
            print("Error al realizar la solicitud. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

@task
def procesarData(data):
    pared = colores.NEGRITA + ' | ' + colores.RESET
    drink = Drink(data["drinks"][0])
    mensaje = colores.NEGRITA + '| Drink: '+colores.RESET 
    mensaje += colores.VERDE + drink.name + colores.RESET  
    mensaje += pared + colores.ROJO + drink.category + colores.RESET + pared
    if drink.isAlcoholic:
        mensaje += colores.AZUL + 'Alcoholic' + colores.RESET
    else:
        mensaje += colores.AZUL + ' | Non Alcoholic |' + colores.RESET
    
    mensaje += pared + colores.CYAN + drink.instructions + colores.RESET + pared
    print(mensaje)
    print(colores.VERDE + 'Happy drinking 🤓' + colores.RESET)
    return drink

# Crear un flujo Prefect
@flow(log_prints=True)
def getTheDrinkOfTheDay(url: str = "https://www.thecocktaildb.com/api/json/v1/1/random.php?"):
    url_api = url
    datos_json = obtener_json(url_api)
    trago = procesarData(datos_json)

# Ejecutar el flujo
if __name__ == "__main__":
    getTheDrinkOfTheDay.serve(
        name="DrinkFlow",
        tags=["drinking", "testing"],
        description="Get what im'bout to get drunk to today...",
        version="tutorial/deployments",
    )




