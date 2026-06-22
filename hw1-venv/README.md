Задание: создание виртуального окружения Python

##Виртуальное окружение создавалось на Ubuntu

## Что сделано

- Создано виртуальное окружение `my-venv`
- Установлены библиотеки из `requirements.txt`
- Создан скрипт `dchart.py`
- Построен график `gauss.png`

## Запуск

```bash
python3 -m venv my-venv
source my-venv/bin/activate
pip install -r requirements.txt
python dchart.py
