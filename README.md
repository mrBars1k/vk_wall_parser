# vk_wall_parser
Простой парсер стены vk, который собирает весь текст публикации со стены группы в sqlite базу данных.

Инструкция по получению токена и id сообщества:

1. Перейдите по ссылке: https://vk.com/dev
2. Вверху нажмите на Мои приложения
3. Создайте приложение, указав платформу Standalone-приложение
4. Переходим в настройки приложения: редактировать -> настройки
5. Возьмите оттуда ID приложения
6. Вставьте в следующую ссылку свой ID в указанном месте
https://oauth.vk.com/authorize?client_id=ВАШ_ID_ПРИЛОЖЕНИЯ&display=page&scope=wall,offline&response_type=token&v=5.131
7. Дайте разрешения, который просит
8. В адресовой строке браузера появится новая ссылка, где есть ваш access_token. Скопируйте его
(после знака "=" и до первого знака "&")
9. Вставьте этот токен к себе в файл с парсером в поле access_token
10. Вместо group_id, укажите цифры ID вашей группы (пример club24108422, взять только цифры), минус не нужно убирать

После этого укажите количество постов, которое нужно спарсить и сколько за один заход будет вносить в таблицу (или другой метод, который вы допишите).
Запускайте.
