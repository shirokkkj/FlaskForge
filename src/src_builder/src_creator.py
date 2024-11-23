
from src.src_builder.utils import create_directory, create_file_in_directory

class ProjectStructureCreator:
    def __init__(self, directory_path):
        self.__directory_path = directory_path
        
    def create_project_directory(self):
        paths = [
            f'{self.__directory_path}\\src',
            f'{self.__directory_path}\\src\\controllers',
            f'{self.__directory_path}\\src\\models',
            f'{self.__directory_path}\\src\\static',
            f'{self.__directory_path}\\src\\templates',
            f'{self.__directory_path}\\src\\forms',
            f'{self.__directory_path}\\src\\utils',
            f'{self.__directory_path}\\src\\static\\js',
            f'{self.__directory_path}\\src\\static\\css',
        ]
        creation_status = create_directory(paths)
        
        if creation_status == 'Fail':
            return 'Failed to create the project directory.'
        
        return 'The project directory "src" has been successfully created!'
    
    def create_application_main_files(self):
        files_to_create = [
        ('app.py', '''
from config_app import config_app
         
         
app = config_app()
         
         
if __name__ == '__main__':
    app.run(debug=True)

'''),
        ('config_app.py', '''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config_routes import config_routes TURN THIS ON WHEN YOUR CONTROLLER'S/ROUTES ARE REGISTEREDS
from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv('SECRET_KEY') # ALTER THE SECRET KEY IN .ENV FILE
DB_URI = getenv('DB_URI') # ALTER THE DB_URI KEY IN .ENV FILE

db = SQLAlchemy()

def config_app():
    app = Flask(__name__)         
    app.config['SECRET_KEY'] = f'{SECRET_KEY}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_URI}'
    
    db.init_app(app)
    
    # config_routes(app) - TURN THIS ON WHEN YOUR CONTROLLER'S/ROUTES ARE REGISTEREDS
    
    return app
               
'''),
        ('config_routes.py', '''
from controllers.yourcontrollers import yourcontroller
# add more if necessary


def config_routes(app):
    app.register_blueprint(yourcontroller)         
    # add more if necessary
'''),
        ('.gitignore', '.env'),
        ('.env', '''         
SECRET_KEY=YOURSECRETKEY
DB_URI=YOURDBURI        
''')
    ]
        
        creation_status = create_file_in_directory(f'{self.__directory_path}\\src', files_to_create)
        
        return creation_status