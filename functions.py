import config
import requests


# Функция отправки запроса на создание заказа.
# Возвращаемое значение: трек-номер для созданного заказа.
def createOrder(body):
    url = config.URL_SERVICE + config.CREATE_ORDERS
    response = requests.post(url, json=body)
    track_number = response.json()["track"]
    return track_number


# Функция отправки запроса на получение заказа по его трек-номеру.
# Возвращаемое значение: ответ на запрос с информацией о заказе.
def getOrderByTrackNumber(track_number):
    url = f"{config.URL_SERVICE}/v1/orders/track?t={track_number}"
    response = requests.get(url)
    return response