import requests
from bs4 import BeautifulSoup
from prefect import task, flow
def get_product_price(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.select_one('#priceblock_ourprice')
    if price_element:
        price = price_element.text.strip()
        return price
    else:
        return None
@flow(log_prints=True)
def showProduct():
    product_url = 'https://www.amazon.com.mx/Asus-DUAL-RTX4060-O8G-extensión-garantía/dp/B0C7YPGFFW/ref=sr_1_2?__mk_es_MX=ÅMÅŽÕÑ&crid=2CSRBI1K4EFKZ&dib=eyJ2IjoiMSJ9.zOED4fg2-TZnoL9l0zqj-aSzqxmzCd6hRAAV-x66Y_mnlmAucmJ_Hw0V81vTooIRvWcCw4P4HM4BBjtqkJYLlgSW5KsN0yG3xCOzTK_-AwsYoC4yZHTXdGEIbl8x8G3nIffL1JMFBBoBMSvmvO6LHbeuS1abqJy0C9dbzEZ6aRq2hgsMU6iLw-wKt7inQjiV0lK9_-voYr7bzMvosLXZpyYlH93RgpzzVDTseuq_--4RMVQTBwLTufE_heQnTkHQDhw1pT8WWxnkQJ1-YMHSkc_l1mS4cSJdLHFfy4Y4XXI.k8D-vj94WENWmJ9X5Cu6JpJjXtg3Z-nuVCk5umSQq-4&dib_tag=se&keywords=NVIDIA+GeForce+RTX+2060&qid=1710130098&sprefix=nvidia+geforce+rtx+2060%2Caps%2C217&sr=8-2&ufe=app_do%3Aamzn1.fos.8c7b929b-80a3-4a0f-851f-6de37ce634c2'  # Reemplaza con la URL del producto que deseas verificar
    price = get_product_price(product_url)
    print(f'El precio del producto es: {price}')


if __name__ == '__main__':
    showProduct.serve(name="GraphicCardPrice",
                      tags=["onboarding"],
                      interval=60)
