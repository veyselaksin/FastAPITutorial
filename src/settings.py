from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:

    DB_PATH = Path.joinpath(BASE_DIR / 'blog.db')

    @property
    def db_path(self):
        return self.DB_PATH
    
    @db_path.setter
    def set_db_path(self, path):
        self.DB_PATH = path
    
    @db_path.getter
    def get_db_path(self):
        return self.DB_PATH
    
    @db_path.deleter
    def del_db_path(self):
        self.DB_PATH = None
    
    def get_db_url(self):
        return f'sqlite:///{self.DB_PATH}'

    