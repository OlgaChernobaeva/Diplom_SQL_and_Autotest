import requests

import configuration
import sender_stand_request
import data


# Ольга Чернобаева, 14-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_accept_orders():
    track = sender_stand_request.post_new_orders(data.orders_body) #Получение трек-номера при создании нового заказа
    response = requests.get(configuration.URL_SERVICE+configuration.ACCEPT_ORDERS+"?t="+str(track)) #запрос на получения заказа по треку заказа
    assert response.status_code == 200 #Проверка, что код ответа равен 200
