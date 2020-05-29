import sys
sys.path.append(".")
import re
from src.RE.config import load_config
config = load_config()

path_dict_movie_vietnamese = config['path_movie_vietnamese']

pattern_1 = r'(\"[\w|\s|\W]+\")'
pattern_5 = r'(\“[\w|\s|\W]+\”)'
pattern_2 = r'(\'[\w|\s]+\')'
pattern_3 = r'(\([\d]{4}\))'
pattern_4 = r'[\d]{4}'


def get_name_move_pattern(sent):
    res = []
    res_1 = re.findall(pattern_1, sent)
    res_2 = re.findall(pattern_2, sent)
    res_3 = re.findall(pattern_5, sent)
    if len(res_1) > 0:
        for x in res_1:
            res.append(x)
    if len(res_2) > 0:
        for x in res_2:
            res.append(x)
    if len(res_3) > 0:
        for x in res_3:
            res.append(x)
    return res


def check_string_in_movie(list_token):
    res = []
    for t in list_token:
        count = 0
        for j in list_token:
            if t != j and ((t in j) or (j in t)):
                if len(j) > len(t) and j not in res:
                    res.append(j)
                elif len(t) > len(j) and t not in res:
                    res.append(t)
            else:
                count += 1
        if count == len(list_token):
            res.append(t)
    return res


def check_part_of_word(token, list_word):
    for t in list_word:
        if token in t and len(token) < len(t):
            return True
    return False


def get_name_move_use_dictionary(sent_token, sent_text, dictionary):
    res = []
    # for move in dictionary:
    #     if move in sent_token and len(move) > 1:
    #         res.append(move)
    # print("movie in dic + token", res)

    for movie in dictionary:
        if len(movie) > 1:
            if movie in sent_text and check_part_of_word(movie, sent_token) is False:
                res.append(movie)
    if len(res) > 0:
        res = check_string_in_movie(res)
        # print("movie in so khop text english", res)

    movie_vietnamese = load_entity_in_set(path_dict_movie_vietnamese)
    for move_vn in movie_vietnamese:
        if move_vn in sent_text:
            res.append(move_vn)
    # print("movie afer so vietnames", res)

    name_movie_pattern = get_name_move_pattern(sent_text)
    if len(name_movie_pattern) > 0:
        for movie_ in name_movie_pattern:
            movie_ = movie_.replace("'", "").replace("\"", "")
            res.append(movie_)
        res = check_string_in_movie(res)
        # print("movie in pattern", res)
    return res


def get_entity_person(person, diction_actor, diction_director):
    if person in diction_actor and person not in diction_director:
        return 1
    elif person in diction_director and person not in diction_actor:
        return 2
    elif person not in diction_actor and person not in diction_director:
        return 3
    else:
        return 4


def get_entity_actor(sent, dic_actor):
    res = []
    for actor in dic_actor:
        if actor in sent:
            res.append(actor)

    return res


def get_entity_director(sent, dic_director):
    res = []
    for director in dic_director:
        if director in sent:
            res.append(director)
    return res


def get_years(sent):
    res_1 = re.findall(pattern_3, sent)
    if res_1 == []:
        res_2 = re.findall(pattern_4, sent)
        if res_2 != []:
            return res_2
        else:
            return 0
    else:
        return res_1


def load_entity_in_set(file_data):
    res = set()
    with open(file_data, 'r', encoding="utf-8") as file_txt:
        data = file_txt.read()
        key_list = data.split("\n")
        for key in key_list:
            if key != "":
                res.add(key.strip())

    return res


if __name__ == "__main__":
    # file_data = "//Users/trangpi/PycharmProjects/Project_detected_fake_news/src/data/diction_directors.txt"
    # print(load_entity_in_set(file_data))
    list_test = ["fast", "fast & furious", "high"]
    text = "Bộ phim a được sản xuất năm 2017"
    print(get_years(text))
    # print(check_string_in_movie(list_test))
