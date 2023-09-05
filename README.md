# next_level
## Запуск проекта
- Ввести комманду из папки ```infra```
```
sudo docker-compose up -d --build
```
- Проект готов к запуску

## Эндпоинты (относительно http://localhost/)
- При запуске контейнеров автоматически будет создан суперпользователь, для дальнейших команд поулчить токен для суперпользователя
- Также в админке можно создать пользователя и получить токен для него, все запросы доступны только по токену
- Изменение и удаление доступно только суперпользователю, создание контакта доступно только авторизованному пользователю
- (POST) Получение токена
```
/api/auth/token/login/
```
- request
```
{
    "email": "ad@ya.ru",
    "password": "admin"
}
```
- (GET, POST) Получить список всех контактов, создать новый контакт
```
api/contacts/
```
- response (GET)
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "admin",
            "last_name": "admin",
            "email": "ad@ya.ru",
            "phone_number": "+79999999999"
        },
        {
            "id": 2,
            "first_name": "Test name",
            "last_name": "Test last name",
            "email": "test@ya.ru",
            "phone_number": "+79991198876"
        }
    ]
}
```
- request (POST)
```
{
    "email": "test@ya.ru",
    "phone_number": "+79991198876",
    "first_name": "Test name",
    "last_name": "Test last name"
}
```
- response (POST)
```
{
    "id": 2,
    "first_name": "Test name",
    "last_name": "Test last name",
    "email": "test@ya.ru",
    "phone_number": "+79991198876"
}
```
- (DELETE, PATCH, PUT, GET) Удалить, обновить, получить контакт по идентификатору
```
api/contacts/1/
```
- (GET) Поиск по имени или фамилии
```
api/contacts?first_name=<first_name>
api/contacts?last_name=<last_name>
```
