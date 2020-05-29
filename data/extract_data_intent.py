import csv
import json
import random


def load_data_csv(file_name):
    data = []
    with open(file_name, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def load_data_json(file_name):
    with open(file_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def get_born_actor(name_person, born, use_adj=False):
    res = []
    text_1 = "Diễn viên " + name_person + " sinh năm " + born + "."
    text_2 = "Năm sinh của diễn viên {} là {}.".format(name_person, born)
    text_3 = " {} là năm sinh của diễn viên {}.".format(born, name_person)
    if use_adj:
        sample = ["ngôi sao, nổi tiếng"]
        x = random.sample(sample, 1)[0]
        if x == "Ngôi sao":
            text_4 = "Năm sinh của ngôi sao {} là {} . ".format(name_person, born)
            res.append(text_4)
        else:
            text_4 = "Diễn viên nổi tiếng " + name_person + " sinh năm " + born + "."
            res.append(text_4)

    res.append(text_1)
    res.append(text_2)
    res.append(text_3)
    return res


def get_born_director(name_person, born, use_adj=False):
    res = []
    text_1 = "Đạo diễn {} sinh năm {} .".format(name_person, born)
    res.append(text_1)
    if use_adj:
        sample = ["thiên tài", "tài ba"]
        x = random.sample(sample, 1)[0]
        text_2 = "Đạo diễn {} {} sinh năm {} .".format(name_person, x, born)
        res.append(text_2)
    text_3 = "Năm sinh của đạo diễn {} là {} .".format(name_person, born)
    res.append(text_3)
    text_4 = "{} là năm sinh của đạo diễn {} .".format(born, name_person)
    res.append(text_4)
    return res


def get_move_of_actor(name_actor, name_move, year):
    res = []
    text_1 = "{} là diễn viên trong phim {} sản xuất năm {} .".format(name_actor, name_move, year)
    text_2 = "{} từng tham gia phim {} với tư cách là diễn viên.".format(name_actor, name_move)
    text_3 = "{} từng thủ vai chính trong phim {}.".format(name_actor, name_move)
    text_4 = "{} được mời nhận vai trong phim {}".format(name_actor, name_move)
    res.append(text_1)
    res.append(text_2)
    res.append(text_3)
    res.append(text_4)
    return res


def get_roles_of_actor(name_actor, name_roles, name_move):
    res = []
    text_1 = "{} từng đảm nhận vai {} trong phim {}".format(name_actor, name_roles, name_move)
    text_2 = "Nhân vật {} được diễn viên {} đảm nhận trong phim {}".format(name_roles, name_actor, name_move)
    text_3 = "Trong {}, {} hoá thân vào nhân vật {}.".format(name_move, name_actor, name_roles)
    res.append(text_1)
    res.append(text_2)
    res.append(text_3)
    return res


def get_move_of_director(name_director, list_move, use_adj=False):
    res = []
    move = random.sample(list_move, 1)[0]
    text_1 = "{} đã từng đạo diễn cho phim {} .".format(name_director, move)
    res.append(text_1)
    if use_adj:
        sample = ["thàng công", "xuất sắc"]
        adj = random.sample(sample, 1)[0]
        text_2 = "{} đã từng đạo diễn {} phim {}.".format(name_director, adj, move)
        text_3 = "Sự thành công của phim {} là nhờ sự đạo diễn tài tình của {}.".format(move, name_director)
        res.append(text_2)
        res.append(text_3)
    if len(list_move) >= 2:
        sample = random.sample(list_move, 2)
        text_4 = "{} từng làm đạo diễn các bộ phim như {}, {},.. ".format(name_director, sample[0], sample[1])
        res.append(text_4)
    return res


def get_release_of_move(name_move, years, name_director):
    res = []
    text_1 = "Bộ phim {} là bom tấn được ra mắt năm {} .".format(name_move, years)
    text_2 = "{} là bộ phim điện ảnh được ra mắt năm {} .".format(name_move, years)
    text_3 = "{} là bộ phim được phát hành vào năm {} do {} làm đạo diễn .".format(name_move, years, name_director)
    text_4 = "{} sản xuất năm {} .".format(name_move, years)
    text_5 = "{} được phát hành vào năm {}".format(name_move, years)
    res.append(text_1)
    res.append(text_2)
    res.append(text_3)
    res.append(text_4)
    res.append(text_5)
    return res


def get_director_of_move(name_move, list_name_director):
    res = []
    director = random.sample(list_name_director, 1)[0]
    text_1 = "Bộ phim {} do {} làm đạo diễn .".format(name_move, director)
    res.append(text_1)
    if len(list_name_director) >= 2:
        list_d = random.sample(list_name_director, 2)
        text_2 = "Bộ phim {} có {} và {} cùng làm đạo diễn. ".format(name_move, list_d[0], list_d[1])
        text_3 = "Bộ phim {} có các đạo diễn là {}, {}".format(name_move, list_d[0], list_d[1])
        res.append(text_2)
        res.append(text_3)
    text_4 = "{} được đạo diễn bởi {}.".format(name_move, director)
    text_5 = "{} là bộ phim được đạo diễn bởi {}. ".format(name_move, director)
    text_6 = "{} là dự án phim có sự đạo diễn của {}".format(name_move, director)
    res.append(text_4)
    res.append(text_5)
    res.append(text_6)
    return res


def get_actor_of_move(name_move, list_actor):

    res = []
    num_actor = len(list_actor)
    print(list_actor)
    actor = random.sample(list_actor, 1)[0]
    text_1 = "Phim {} có sự góp mặt của  diễn viên nổi tiếng {}.".format(name_move, actor)
    res.append(text_1)
    if num_actor == 2:
        text_2 = "Phim {} có sự góp mặt của hai diễn viên nổi tiếng {} và {}".format(name_move,
                                                                                     list_actor[0], list_actor[1])
        text_3 = "Phim {} có sự tham gia của hai ngôi sao nổi tiếng {} và {}".format(name_move,
                                                                                    list_actor[0], list_actor[1])
        res.append(text_2)
        res.append(text_3)
    if num_actor >= 3:
        list_actor_ = random.sample(list_actor, 3)
        text_4 = "Phim {} có sự tham gia của dàn sao nổi tiếng như {}, {}, {},..".format(name_move, list_actor_[0],
                                                                                         list_actor_[1], list_actor_[2])
        res.append(text_4)

    return res


def get_produced_director_of_move(name_move, list_produce, list_director):
    res = []
    produced = random.sample(list_produce, 1)[0]
    director = random.sample(list_director, 1)[0]
    text_1 = "{} do {} sản xuất và {} làm đạo diễn".format(name_move, produced, director)
    text_2 = "{} : bộ phim do {} sản xuất và {} làm đạo diễn.".format(name_move, produced, director)
    text_3 = "Nhà sản xuất {} hợp tác cùng đạo diễn {} trong bộ phim điện ảnh {} .".format(produced, director, name_move)
    res.append(text_1)
    res.append(text_2)
    res.append(text_3)
    return res


def get_data_born_of_actor(data, file_out):
    res = []
    for sample in data:
        if sample["type"]=="ACTED_IN":
            res_actor = get_born_actor(sample["name"], sample["born"])
            res.append(res_actor)
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_born_of_director(data, file_out):

    res = []
    for sample in data:
        if sample["type"] == "DIRECTED":
            res_actor = get_born_director(sample["name"], sample["born"])
            res.append(res_actor)
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_move_of_actors(data, file_out):

    res = []
    len_data = len(data)
    list_sample = random.sample(data, len_data)
    for sample in list_sample:
        if sample["type"]=="ACTED_IN":
            res_actor = get_move_of_actor(sample["name"], sample["title"], sample["released"])
            res.append(res_actor)
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_roles_of_actor(data, file_out):
    res = []
    len_data = len(data)
    list_sample = random.sample(data, len_data)
    for sample in list_sample:
        if sample["type"] == "ACTED_IN":
            res_actor = get_roles_of_actor(sample["name"], sample["roles"].replace(";", ""), sample["title"])
            res.append(res_actor)
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_release_of_move(data, file_out):

    res = []
    list_sample = random.sample(data, len(data))
    for sample in list_sample:
        try:
            res_move = get_release_of_move(sample["title"], sample["year"], sample["directors"][0])
            res.append(res_move)
        except:
            continue
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_director_of_move(data, file_out):
    res = []
    list_sample = random.sample(data, len(data))
    for sample in list_sample:
        try:
            res_move = get_director_of_move(sample["title"], sample["directors"])
            res.append(res_move)
        except:
            continue
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_actor_of_move(data, file_out):
    res = []
    list_sample = random.sample(data, len(data))
    for sample in list_sample:
        if sample["actors"]:
            res_actor = get_actor_of_move(sample["title"], sample["actors"])
            res.append(res_actor)

        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


# def get_data_produced_director_of_move(data, file_out):
#     res = []
#     title = set()
#     list_sample = random.sample(data, len(data))
#     for sample in list_sample:
#         res_actor = get_produced_director_of_move(sample["title"], sample["directors"])
#         res.append(res_actor)
#
#         if len(res) == 100:
#             break
#
#     with open(file_out, mode="w+") as txt_file:
#         for actor in res:
#             for ex in actor:
#                 txt_file.writelines(ex)
#     pass

def get_data_move_of_director(data, file_out):
    res = []
    len_data = len(data)
    list_sample = random.sample(data, len_data)
    for sample in list_sample:
        if sample["type"] == "DIRECTED":
            use_adj = random.sample([False, True], 1)[0]
            res_actor = get_move_of_director(sample["name"], [sample["title"]], use_adj=use_adj)
            res.append(res_actor)
        if len(res) == 100:
            break

    with open(file_out, mode="w+") as txt_file:
        for actor in res:
            for ex in actor:
                txt_file.write(ex + "\n")
    pass


def get_data_name_movie(data_csv, data_json, file_out):
    set_name_movie = set()
    for sample in data_json:
        set_name_movie.add(sample["title"])

    print(len(set_name_movie))

    for sample in data_csv:
        set_name_movie.add(sample["title"])
    print(len(set_name_movie))

    with open(file_out, "w", encoding="utf-8") as file_txt:
        for item in set_name_movie:
            line = item + "\n"
            file_txt.write(line)

def get_data_name_actor(data_csv, data_json, file_out):
    set_name_movie = set()
    for sample in data_json:
        if sample["actors"]:
            for x in sample["actors"]:
                set_name_movie.add(x)

    print(len(set_name_movie))

    for sample in data_csv:
        if sample['type'] == "ACTED_IN":
            set_name_movie.add(sample["name"])
    print(len(set_name_movie))

    with open(file_out, "w", encoding="utf-8") as file_txt:
        for item in set_name_movie:
            line = item + "\n"
            file_txt.write(line)

def get_data_name_directors(data_csv, data_json, file_out):
    set_name_movie = set()
    for sample in data_json:
        try:
            if sample["directors"]:
                for x in sample["directors"]:
                    set_name_movie.add(x)
        except:
            continue

    print(len(set_name_movie))

    for sample in data_csv:
        if sample['type'] == "DIRECTED":
            set_name_movie.add(sample["name"])
    print(len(set_name_movie))

    with open(file_out, "w", encoding="utf-8") as file_txt:
        for item in set_name_movie:
            line = item + "\n"
            file_txt.write(line)


def get_name_actor_vietnamesse(data, file_out):
    set_name_actor = set()
    actors = data[0]['Movie'].split(',')
    for item in actors:
        set_name_actor.add(item)

    with open(file_out, "w", encoding="utf-8") as file_txt:
        for item in set_name_actor:
            line = item + "\n"
            file_txt.write(line)







if __name__ == "__main__":
    file_csv = "/Users/trangpi/PycharmProjects/Project_detected_fake_news/src/data/comments.csv"
    file_json = "/Users/trangpi/Downloads/imdb_dataset.json"

    data_csv = load_data_csv(file_csv)
    # data_json = load_data_json(file_json)
    # print(data_csv[0]['Actor'])
    get_name_actor_vietnamesse(data_csv, "vietnamese_movie.txt")

