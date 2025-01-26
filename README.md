# **Домашняя работа по Django(проект интернет-магазина).** 
___
### **Описание:**
Данная работа была создана при помощи фреймворка Django.
###  **Этап № 1.**
В папке config главной дирректории были сделанны следующие настройки в файле settings:
1. В список ALLOWED_HOSTS добавлен символ *
2. В список INSTALLED_APPS добавлено приложение catalog
3. В TIME_ZONE изменен часовой пояс на "Europe/Moscow"
4. Для STATIC_URL = "static/" добавлен путь STATICFILES_DIRS = (BASE_DIR / 'static',)
___
В файле utils той же директории добавлены маршруты для страниц contacts.html и 
home.html
___
В главную дирректорию добавленна папка catalog с приложением и файлами через Django.
Создан файл utils для описания маршрутов.
___
В файле views описанны контроллеры.
___
Папка для шаблонов страниц templates.
___
### **Этап № 2.**
1. Настройки DATABASES в проекте заменены на подключение к PostgreSQL, 
указаны ENGINE, NAME, USER, PASSWORD, HOST, PORT.
2. В зависимости добавлена библиотека psycopg2-binary.
3. Настройки работы с БД вынесены в переменные окружения в файл .env
4. Создана модель продукта и категории в файле models.py.
5. Сделаны и запушены миграции с полями моделей.
6. Установлен и зафиксирован в зависимостях пакет Pillow.
7. Для продуктов и категорий настроено отображение в административной панели.
8. Установлена библиотека ipython и зафиксирована в зависимостях проекта.
9. Реализованы фикстуры и кастомная команда для загрузки объектов.
___
### **Этап № 3.**
1. Созданы новые контроллеры для одного товара и списка товаров(product_info и product_list).
2. Созданы и изменены шаблоны для одного товара, списка товаров и контактов.
3. Вынесены отдельные шаблоны и подшаблоны: базовый, 'футер', главное меню.
4. Внесены соответствующие корректировки в URLS.
### **Этап № 4.**
1. Переведены имеющиеся в проекте контроллеры с FBV на CBV.
2. Созданно новое приложение my_blog.
3. Для работы с my_blog реализован полный CRUD для новой модели, используя CBV.
4. Модифицирован вывод и обработка запросов, добавлена логика на уровне контроллеров:
    - Увеличение счетчика просмотров статьи при каждом просмотре
    - Фильтрация опубликованных статей по положительному признаку публикации
    - Перенаправление на статью после её редактирования
### **Этап № 5.**
1. Создан класс формы для продукта.
2. Реализованы CRUD-операции для продуктов с помощью форм.
3. Собраны шаблоны с использованием форм.
4. Форма подключена в соответствующие контроллеры работы с продуктом.
5. В форме отображены все поля для создания/обновления объекта продукта.
6. Собран шаблон для подтверждения удаления продукта.
7. Реализована валидация на запрещенные слова отдельно для имени и отдельно для описания.
8. Добавлена кастомная валидация для поля purchase_price.
9. Формы продукта стилизованы.
### **Этап № 6.**
1. Создано новое приложение users для работы с пользователями.
2. Реализована модель пользователя, которая отнаследована от AbstractUser.
3. В модель добавлены поля email, аватар, номер телефона, страна в соответствующих типах.
4. В модель добавлены поля email, аватар, номер телефона, страна в соответствующих типах.
5. В настройках проекта заменена AUTH_USER_MODEL на текущую созданную.
6. Создана форма для регистрации пользователя.
7. Определены и собраны шаблоны для регистрации.
8. В интерфейс интегрирована кнопка регистрации.
9. Переопределен метод form_valid() в контроллере регистрации, в который интегрирована отправка приветственного сообщения.
10. Произведены настройки почтового сервера в настройках проекта.
11. Реализована авторизация пользователя.
12. Реализована форма авторизации.
13. Реализован шаблон авторизации.
14. В интерфейс интегрирована кнопка входа.
15. Контроллеры для работы с продуктами дополнительно наследуются от LoginRequiredMixin.
16. Общедоступной для неавторизованных пользователей осталась только страница просмотра списка товаров.
### **Этап № 7.**
1. Создана группа «Модератор продуктов».
2. У модели продукта добавлено право на отмену публикации продукта.
3. Для группы «Модератор продуктов» настроено право на отмену публикации продукта.
4. Для группы «Модератор продуктов» настроено право на удаление любого продукта.
5. Проверяется наличие прав у пользователя при попытке отменить публикацию или удалить продукт.
6. Приложена фикстура с группами 'CATgroups.json'
7. Добавлено поле владельца к модели продукта.
8. Поле владельца связано с моделью пользователя через ForeignKey.
9. При создании нового продукта поле owner автоматически заполняется текущим авторизованным пользователем.
10. Реализована проверка прав доступа в представлениях для редактирования и удаления продуктов, чтобы только владелец мог выполнять эти действия.
11. При запросе удаления проверяется дополнительно наличие группы модератора у пользователя.
### **Этап № 8.**
1. Подключен Redis и внесены для него необходимые настройки в проект.
2. Произведены настройки CACHE_ENABLED и CACHES.
3. Настроено кеширование страницы отображения информации об одном продукте.
4. Реализовано низкоуровневое кеширование списка продуктов.
5. Создана сервисная функция для работы с продуктами, которая будет возвращать список всех продуктов в указанной категории.
6. Реализовано отдельное представление и шаблон для отображения продуктов в указанной категории на сайте.
## **Лицензия**

Этот проект можно использовать безвозмездно для любых, 
не противоречащих законодательству целей.