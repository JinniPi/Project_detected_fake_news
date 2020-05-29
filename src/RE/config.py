import configparser


def load_config(file_config='/Users/trangpi/PycharmProjects/Project_detected_fake_news/config/config.ini'):

    """
    load config from file .ini
    :param file_config:
    :return:
    """
    config = {}
    config_parser = configparser.ConfigParser()
    config_parser.read_file(open(file_config))
    # data
    config['path_movie_english'] = config_parser.get('PATH_FILE_DATA', 'path_movie_english')
    config['path_actor_english'] = config_parser.get('PATH_FILE_DATA', 'path_actor_english')
    config['path_director_english'] = config_parser.get('PATH_FILE_DATA', 'path_director_english')
    config['path_movie_vietnamese'] = config_parser.get('PATH_FILE_DATA', 'path_movie_vietnamese')
    config['path_actor_vietnamese'] = config_parser.get('PATH_FILE_DATA', 'path_actor_vietnamese')
    config['path_director_vietnamese'] = config_parser.get('PATH_FILE_DATA', 'path_director_vietnamese')
    config['path_key_actor'] = config_parser.get('PATH_FILE_DATA', 'path_key_actor')
    config['path_key_director'] = config_parser.get('PATH_FILE_DATA', 'path_key_director')
    config['path_key_release'] = config_parser.get('PATH_FILE_DATA', 'path_key_release')

    return config


if __name__ == "__main__":

    print(load_config())