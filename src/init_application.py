from src.src_builder.src_creator import ProjectStructureCreator

class ProjectInitManager: 
    def __init__(self, directory_path):
        self.__directory_path = directory_path  
    def init_project(self):
        project_strucutre = ProjectStructureCreator(self.__directory_path)
        application_directory = project_strucutre.create_project_directory()
        application_directory_files = project_strucutre.create_application_main_files()
        
        
        return application_directory, application_directory_files