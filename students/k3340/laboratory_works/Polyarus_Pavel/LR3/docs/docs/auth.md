# Авторизация и регистрация

В системе используется токенная аутентификация (DRF + Djoser).

## Регистрация
``POST /auth/users/``

```json
{
  "username": "zavuch",
  "password": "12345678",
  "re_password": "12345678"
}
```

## Авторизация
``POST /auth/token/login/``

```json
{
  "username": "zavuch",
  "password": "12345678",
}
```

**Ответ:**
```json
{
  "auth_token": "token"
}
```

## Текущий пользователь
``POST /auth/users/me/``

**Header:**

``Authorization: Token <token>``

**Ответ:**
```json
{
    "email": "",
    "id": 2,
    "username": "zavuch"
}
```
