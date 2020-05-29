import sys
sys.path.append(".")
from src.RE.utils import *
from src.RE.ner import word_tokenize_vncorenlp
from src.RE.config import load_config
from underthesea import sent_tokenize, word_tokenize
from src.RE.ner import ner_vncorenlp
config = load_config()

DICT_MOVIE = load_entity_in_set(config['path_movie_english'])
DICT_ACTOR = load_entity_in_set(config['path_actor_english'])
DICT_DIRECTOR = load_entity_in_set(config['path_director_english'])
key_actor = load_entity_in_set(config['path_key_actor'])
key_director = load_entity_in_set(config['path_key_director'])
key_release = load_entity_in_set(config['path_key_release'])
relation_ = {"actors_of", "director_of", "release"}


def extract_relation(text):
    """
    return all re of text
    :param text: list of sent
    :return:
    """
    list_sent = sent_tokenize(text)
    relation_text = []
    for sent in list_sent:
        relation_sent = extract_re_sent(sent)
        if len(relation_sent) > 0:
            relation_text.append(relation_sent)
    return relation_text


def extract_re_sent(sent):
    """
    return re of sent
    :param sent:
    :return:
    """
    relation = []
    # list_token = word_tokenize(sent)
    movie, actor, director, years = sent_ner(sent)
    print("movie", movie)
    print("actor", actor)
    print("director", director)
    print(years)
    if len(movie) != 0:
        if len(movie) == 1:
            # print("len director", len(director))
            # 1 movie, nhieu actor
            if len(director) == 0 and len(actor) >= 1:
                check_relation_actor = check_key_relation(sent, key_actor)
                if check_relation_actor:
                    for x in actor:
                        relation_x = {x: "ACTOR", "re": "actor_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                else:
                    check_relation_director = check_key_relation(sent, key_director)
                    if check_relation_director:
                        for x in actor:
                            relation_x = {x: "ACTOR", "re": "director_of", movie[0]: "MOVIE"}
                            relation.append(relation_x)
            # 1 movie, nhieu director
            elif len(director) >= 1 and len(actor) == 0:
                # print("vao day")
                check_relation_director = check_key_relation(sent, key_director)
                if check_relation_director:
                    # print(check_relation_director)
                    for x in director:
                        relation_x = {x: "DIRECTOR", "re": "director_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                else:
                    check_relation_director = check_key_relation(sent, key_actor)
                    if check_relation_director:
                        for x in director:
                            relation_x = {x: "DIRECTOR", "re": "actor_of", movie[0]: "MOVIE"}
                            relation.append(relation_x)
            # 1 movie, co actor + director
            elif len(director) > 0 and len(actor) > 0:
                check_relation_actor = check_key_relation(sent, key_actor)
                check_relation_director = check_key_relation(sent, key_director)
                if check_relation_director is True and check_relation_actor is True:
                    for x in actor:
                        relation_x = {x: "ACTOR", "re": "actor_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                    for x in director:
                        relation_x = {x: "DIRECTOR", "re": "director_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                elif check_relation_director is True and check_relation_actor is False:
                    for x in director:
                        relation_x = {x: "DIRECTOR", "re": "director_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                elif check_relation_director is False and check_relation_actor is True:
                    for x in actor:
                        relation_x = {x: "ACTOR", "re": "actor_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
            else:
                if len(years) == 1:
                    year = years[0]
                    check_year_release = check_key_relation(sent, key_release)
                    if check_year_release:
                        relation_x = {year: "TIME", "re": "release_of", movie[0]: "MOVIE"}
                        relation.append(relation_x)
                else:
                    entity_person = ner_vncorenlp(sent)
                    if len(entity_person) != 0:
                        check_key_actors = check_key_relation(sent, key_actor)
                        check_key_directors = check_key_relation(sent, key_director)
                        if check_key_actors is True and check_key_directors is False:
                            for x in actor:
                                relation_x = {x: "PER", "re": "actor_of", movie[0]: "MOVIE"}
                                relation.append(relation_x)
                        if check_key_actors is False and check_key_directors is True:
                            for x in actor:
                                relation_x = {x: "PER", "re": "director_of", movie[0]: "MOVIE"}
                                relation.append(relation_x)
        else:
            # 1 actor nhieu movie
            if len(actor) == 1:
                check_relation_actor = check_key_relation(sent, key_actor)
                if check_relation_actor:
                    for x in movie:
                        relation_x = {actor[0]: "ACTOR", "re": "actor_of", x: "MOVIE"}
                        relation.append(relation_x)
                else:
                    check_relation_director = check_key_relation(sent, key_director)
                    if check_relation_director:
                        for x in movie:
                            relation_x = {actor[0]: "ACTOR", "re": "director_of", x: "MOVIE"}
                            relation.append(relation_x)
            # 1 director nhieu movie
            elif len(director) == 1:
                check_relation_director = check_key_relation(sent, key_director)
                if check_relation_director:
                    for x in movie:
                        relation_x = {director[0]: "DIRECTOR", "re": "director_of", x: "MOVIE"}
                        relation.append(relation_x)
                else:
                    check_relation_actor = check_key_relation(sent, actor)
                    if check_relation_actor:
                        for x in movie:
                            relation_x = {actor[0]: "DIRECTOR", "re": "actor_of", x: "MOVIE"}
                            relation.append(relation_x)
            # xet truong hop ko bat dc actor va director
            elif len(actor) == 0 and len(director) == 0:
                entity_person = ner_vncorenlp(sent)
                # chi xet duoc trong truong hop 1 PER
                if len(entity_person) == 1:
                    check_key_actors = check_key_relation(sent, key_actor)
                    check_key_directors = check_key_relation(sent, key_director)
                    if check_key_actors is True and check_key_directors is False:
                        for x in actor:
                            relation_x = {x: "PER", "re": "actor_of", movie[0]: "MOVIE"}
                            relation.append(relation_x)
                    if check_key_actors is False and check_key_directors is True:
                        for x in actor:
                            relation_x = {x: "PER", "re": "director_of", movie[0]: "MOVIE"}
                            relation.append(relation_x)





    return relation


def check_key_relation(sent, dict_relation):
    for key_relation in dict_relation:
        if key_relation.lower() in sent.lower():
            return True
    return False


def sent_ner(sent):
    """
    return list entity of sent
    :param sent:
    :return:
    """
    list_token = word_tokenize(sent)
    # print("list_token of vncore nlp", list_token)
    movie = get_name_move_use_dictionary(list_token, sent, DICT_MOVIE)
    actor = get_entity_actor(list_token, DICT_ACTOR)
    director = get_entity_director(list_token, DICT_DIRECTOR)
    year = get_years(sent)
    return movie, actor, director, year

if __name__ == "__main__":
    from underthesea import word_tokenize

    text = "Cuối năm 2017, Wonder Woman của đạo diễn Patty Jenkins đã trở thành một cú nổ lớn khi cán mốc 700 triệu USD trên toàn thế giới và trở thành bộ phim live-action có doanh thu cao nhất được làm ra bởi một nữ đạo diễn."
    print(word_tokenize(text))
    print(extract_relation(text))
