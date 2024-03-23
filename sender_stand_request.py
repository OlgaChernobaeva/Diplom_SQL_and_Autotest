import configuration
import requests


#Создание заказа и получение его трек-номера
def post_new_orders(body):
    request = requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDERS,
                         json=body)
    return request.json()['track']

