# DjangoMenuTag
Меню, реализованное через template tag. Хранится в БД, активный пункт меню определяется из текущего url.

# To run the project:

```
git clone https://github.com/Nekttuman/DjangoMenuTag.git
```

```
cd .\DjangoMenuTag\
python -m venv env
.\env\Scripts\activate.bat
```

```
pip install -r requirements.txt 
```

```
python manage.py runserver
```

Open localhost: http://127.0.0.1:8000/


# Task
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД

 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 
 ```
 {% draw_menu 'main_menu' %}
 ```

 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

 # Описание решения

 Меню хранятся в  модели Menu items. Добавление нового элемента в меню:
 ![image](https://github.com/Nekttuman/DjangoMenuTag/assets/54391498/39d2f603-1272-4e8e-b477-bb40fb3ed972)

 Поскольку запрос к Бд дожен быть единственным при отрисовке меню, в draw_menu, фала menu_tags.py используем:
 ```
menu_items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')
```

Выбран пункт меню "Услуги"
![image](https://github.com/Nekttuman/DjangoMenuTag/assets/54391498/de30ba98-3c5a-452f-8c67-4d91bff06e5f)

Выбран пункт меню "Модбильные приложения"
![image](https://github.com/Nekttuman/DjangoMenuTag/assets/54391498/38e75c85-efd6-435a-a9e7-e5af2bc1596a)

Выбран пункт меню "1.1 Definition of Concepts"
![image](https://github.com/Nekttuman/DjangoMenuTag/assets/54391498/74957140-6ceb-408b-8a04-2db2572f3813)

