# Карпенко Сергей, 13-я когорта — Диплом. Инженер по тестированию плюс

import functions
import config


# Тест на создание и получения заказа по трек-номеру.
def test_order_creation_and_receiving():
    track_number = functions.createOrder(config.ORDER_BY_DATA)

    response = functions.getOrderByTrackNumber(track_number)
    assert response.status_code == 200