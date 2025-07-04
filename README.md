# Form Template Matcher

## Описание
Утилита для сопоставления пользовательских данных с шаблонами форм из базы TinyDB.

## Установка
```bash
pip install tinydb
```

## Загрузка шаблонов
```bash
python template_loader.py
```

## Использование
```bash
python app.py get_tpl --params customer=vasya order_id=vasya дата_заказа=26.06.2025 contact="+7 123 456 78 90"
python app.py get_tpl --params login=vasya@example.com tel="+7 123 456 78 90"
python app.py get_tpl --params f_name1=vasya@pukin.ru f_name2=26.06.2025
```
Если шаблон найден, будет выведено его имя. Если не найден — будет выведена структура полей с определёнными типами данных.

## Несовпадающие
```bash
python app.py get_tpl --params f_name1=aaa@bbb.ru
python app.py get_tpl --params login=yura f_name2=26.06.2025
python app.py get_tpl --params f_name1=yura f_name2=26.06.2025
python app.py get_tpl --params f_name1=26.06.2025 f_name2="+7 985 423 45 78"
python app.py get_tpl --params customer=yura order_id=yura contact="+7 985 456 78 90"
```
## Тестирование
```bash
python -m unittest tests/test_app.py
```