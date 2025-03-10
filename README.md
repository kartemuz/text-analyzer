# Анализатор текста для задач извлечения данных

Версия Python - **Python 3.10**.

## Виртуальное окружение

### Создание

```commandline
python3.10 -m venv venv
```

### Активация

**Linux**:

```commandline
source venv/bin/activate
```

**Windows**:

```commandline
venv\Scripts\activate.bat
```

### Установка зависимостей из файла `requirements.txt`

```commandline
pip install -r requirements.txt
```

### Установка русскоязычной модели `spacy`

```commandline
python -m spacy download ru_core_news_sm
```

## Запуск приложения

**Linux**:

```commandline
python src/main.py
```

**Windows**:

```commandline
python src\main.py
```