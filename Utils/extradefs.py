import random
from Databases import userdatabase, filmsdatabase


def make_list_films():
    global num_of_films
    num_of_films = list(range(1, filmsdatabase.get_num_of_films() + 1))


def shuffle_list_of_films(uid):
    random.shuffle(num_of_films)
    userdatabase.update_film_list(','.join(map(str, num_of_films)), uid)


def end_score_message(score):
    if score <= 3:
        return f"Постарайся еще!\nТвой счет всего {score} 😢"
    elif 4 <= score <= 8:
        return f"Твой счет {score} Неплохо!"
    elif 9 <= score <= 15:
        return f"Хорошо! Твой счет {score}"
    elif 16 <= score <= 25:
        return f"Твой счет {score}\nЭто отличный результат!"
    elif 26 <= score <= 49:
        return f"Замечательный результат!\nТвой счет {score}"
    elif 50 <= score <= 149:
        return f"Ты превосходно разбираешься в фильмах, ведь твой счет {score}"
    elif score >= 150:
        return (f"Поздравляю! 🥳\nТеперь ты можешь называть себя профессиональным кинокритиком!"
                f"\n Не каждый способен получить счет равный {score}")


