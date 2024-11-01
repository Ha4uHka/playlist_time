## project_3

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список из кортежа строк и кортежа вещественных чисел
#   * словарь
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any
import random 

playlist_d = [
    ("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
    (5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_b = {
    'Портофино': 3.32,
    'Снег': 4.35,
    'Попытка №5': 3.23,
    'Тополиный Пух': 3.53,
    'Если хочешь остаться': 4.48,
    'Зеленоглазое такси': 5.52,
    'Ты не верь слезам': 3.1,
    'Nowhere to Run': 2.58,
    'Салют, Вера': 4.44,
    'Улетаю': 3.24,
    'Опять метель': 3.37,
}

def get_random_songs(playlist, n):
    merge_playlist = list(zip(playlist_d[0], playlist_d[1]))
    random.shuffle(merge_playlist)
    return merge_playlist[:n]

# print(get_random_songs(playlist_b, 3))

def get_duration(playlist, n):
    counter = 0
    songs = get_random_songs(playlist, n)
    
    for i in range(len(songs)):
        counter += songs[i][1]
    return counter

n = 3
print(get_duration(playlist_d, n))



