from underthesea import ner
from vncorenlp import VnCoreNLP
annotator = VnCoreNLP(address="http://127.0.0.1", port=9000)


def word_tokenize_vncorenlp(sent):
    res = annotator.tokenize(sent)[0]
    res_ = []
    for x in res:
        res_.append(x.replace("_", " "))
    return res_

def ner_underthesea(sent):

    entity = []
    res = ner(sent)
    print(res)
    list_token = [x[0] for x in res]
    list_tag_entity = [x[3] for x in res]
    flag = False
    current_entity = []
    for index, x in enumerate(list_tag_entity):
        if x == "B-PER" and flag is False:
            flag = True
            current_entity.append(list_token[index])
            if index + 1 <= len(list_tag_entity) - 1:
                if list_tag_entity[index + 1] != "I-PER":
                    entity_current = " ".join(current_entity)
                    entity.append(entity_current)
                    flag = False
                    current_entity = []
            elif index == len(list_tag_entity) - 1:
                entity_current = " ".join(current_entity)
                entity.append(entity_current)
                flag = False
                current_entity = []

        if x == "I-PER" and flag is True:
            current_entity.append(list_token[index])
            if index + 1 <= len(list_tag_entity) - 1:
                if list_tag_entity[index + 1] != "I-PER":
                    entity_current = " ".join(current_entity)
                    entity.append(entity_current)
                    flag = False
                    current_entity = []
            elif index == len(list_tag_entity) - 1:
                entity_current = " ".join(current_entity)
                entity.append(entity_current)
                flag = False
                current_entity = []

    return entity


def ner_vncorenlp(sent):
    res = annotator.ner(sent)[0]
    list_token = [x[0] for x in res]
    list_tag_entity = [x[1] for x in res]
    entity = []
    flag = False
    current_entity = []
    for index, x in enumerate(list_tag_entity):
        if x == "B-PER" and flag is False:
            flag = True
            current_entity.append(list_token[index])
            if index + 1 <= len(list_tag_entity) - 1:
                if list_tag_entity[index + 1] != "I-PER":
                    entity_current = " ".join(current_entity)
                    entity.append(entity_current)
                    flag = False
                    current_entity = []
            elif index == len(list_tag_entity) - 1:
                entity_current = " ".join(current_entity)
                entity.append(entity_current)
                flag = False
                current_entity = []

        if x == "I-PER" and flag is True:
            current_entity.append(list_token[index])
            if index + 1 <= len(list_tag_entity) - 1:
                if list_tag_entity[index + 1] != "I-PER":
                    entity_current = " ".join(current_entity)
                    entity.append(entity_current)
                    flag = False
                    current_entity = []
            elif index == len(list_tag_entity) - 1:
                entity_current = " ".join(current_entity)
                entity.append(entity_current.replace("_", ""))
                flag = False
                current_entity = []
    return entity


if __name__ == "__main__":
    text = " Nam diễn viên hạng A, Ansel Elgort cũng đã góp phần không nhỏ cho sự thành công của tác phẩm Chàng trai năm ấy."
    print(ner_underthesea(text))
    print(ner_vncorenlp(text))