from configparser import ConfigParser

config_file_path = 'C:\\Users\\mchtt\\OneDrive\\Masaüstü\\Germany\\sqlalchemy_simple_project\\app\\app.config'


def get_db_url():
    config = ConfigParser()
    config.read(config_file_path)
    return config['database']['URL']
