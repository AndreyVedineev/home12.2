datam = {"vcs": "mercurial", "dds": "venera", "pps": "mars"}
l_str = ['AAA', 'BBB', 'CCC']


def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
.
    :param collection:
    :param key:
    :param default:
    :return:
    """
    if len(collection) == 0:
        return default
    if collection.get(key):
        return collection.get(key)
    else:
        return default


def append_str(dates, value):
    """
    Добавляет элемент в список, если value имеет тип - str
    :param value:
    :param dates:
    :param velue:
    :return:
    """
    if type(value) == str:
        dates.append(value)
    return dates



