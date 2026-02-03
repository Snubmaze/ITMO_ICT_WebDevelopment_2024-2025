# Расписание

## Получить расписание класса
``GET /api/schedule/``
По умолчанию возвращаются все записи, возможна фильтрация через query-параметры.

### Query parameters

| Параметр | Тип | Обязательный | Описание |
|--------|----|--------------|---------|
| class_id | int | да | Идентификатор класса |
| weekday | int | нет | Номер дня недели |

## Пример запроса
``GET /api/schedule/?class_id=1&weekday_id=2``

**Ответ**
```json
[
    {
        "id": 1,
        "school_class": 1,
        "subject": {
            "id": 8,
            "name": "Физкультура",
            "subject_type": "base"
        },
        "teacher": {
            "id": 4,
            "last_name": "Вадюхин",
            "first_name": "Алексей",
            "middle_name": "Сергеевич",
            "assigned_classroom": 5,
            "subjects": [
                8
            ]
        },
        "classroom": {
            "id": 5,
            "nubmer": "1",
            "is_sports_hall": true,
            "specialized_subjects": []
        },
        "weekday": {
            "id": 2,
            "name": "Понедельник",
            "order": 1
        },
        "time_slot": {
            "id": 1,
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:15:00"
        }
    },
    {
        "id": 2,
        "school_class": 1,
        "subject": {
            "id": 3,
            "name": "География",
            "subject_type": "base"
        },
        "teacher": {
            "id": 2,
            "last_name": "Маркова",
            "first_name": "Людмила",
            "middle_name": "Викторовна",
            "assigned_classroom": 3,
            "subjects": [
                3
            ]
        },
        "classroom": {
            "id": 3,
            "nubmer": "38",
            "is_sports_hall": false,
            "specialized_subjects": []
        },
        "weekday": {
            "id": 2,
            "name": "Понедельник",
            "order": 1
        },
        "time_slot": {
            "id": 4,
            "lesson_number": 4,
            "start_time": "11:20:00",
            "end_time": "12:05:00"
        }
    }    
]
```

## Создание записи расписания
`POST /api/schedule/`
### Тело запроса
```json
{
    "school_class": 1,
    "subject_id": 8,
    "teacher_id": 4,
    "classroom_id": 5,
    "weekday": 2,
    "time_slot": 1
}
```
## Изменение записи расписания
### Полное обновление

`PUT /api/schedule/{id}/`

### Частичное обновление

`PATCH /api/schedule/{id}/`

```json
{
    "teacher_id": 7
}
```

## Удаление записи

`DELETE /api/schedule/{id}/`

## Ограничения и бизнес-логика

В один и тот же момент времени (weekday + time_slot) у одного класса или учителя может быть только один урок
