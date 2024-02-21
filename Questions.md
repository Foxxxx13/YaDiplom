# Дипломный проект по курсу Яндекс.Практикума - инженер тестирования плюс.

# Работа с базой данных
## Задание 1.1 с правками

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.

Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

### Решение
```sql
SELECT c.login, COUNT(ord.id)
FROM "Couriers" AS c
LEFT JOIN "Orders" AS ord ON c.id = ord."courierId"
WHERE ord."inDelivery" = true
GROUP BY c.login;
```
![](images/SQL%20задание%201.1%20с%20правками%20.png)

## Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы. 

Статусы определяются по следующему правилу:
* Если поле finished == true, то вывести статус 2.
* Если поле canсelled == true, то вывести статус -1.
* Если поле inDelivery == true, то вывести статус 1.
* Для остальных случаев вывести 0.

Технические примечания:

Доступ к базе осуществляется с помощью команды `psql -U morty -d scooter_rent`. Пароль: `smith`.

У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, `select * from “Orders”`.

### Решение
```sql
SELECT track,
CASE 
    WHEN finished IS true THEN 2
    WHEN cancelled IS true THEN -1
    WHEN "inDelivery" IS true THEN 1
    ELSE 0
END
FROM "Orders";
```
![](images/SQL%20задание%202.png)
---