import vk_api
import sqlite3  # можно использовать любой другой способ заполнения
from datetime import datetime

with sqlite3.connect("vk_p.db") as adb:
    cur = adb.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS vk_posts (
        sentences TEXT, 
        date TEXT
    )""")
    adb.commit()

    access_token = "token"
    group_id = "-xxxxxxxxx"  # минус должен присутствовать

    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()

    offset = 0  # смещение, чтобы продолжать с места остановки
    count = 50  # сколько постов берёт за один раз (больше 100 нельзя)
    total_count = 200  # всего публикации, которые нужно спарсить

    while offset < total_count:

        wall_posts = vk.wall.get(owner_id=group_id, count=count, offset=offset)

        for post in wall_posts['items']:
            if 'text' in post:
                text = post['text']

                timestamp = post['date']
                date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # форматирование даты

                cur.execute("INSERT INTO vk_posts (sentences, date) VALUES (?, ?)", (date, text))
                adb.commit()

        offset += count  # смещение на количество уже отработанных постов
