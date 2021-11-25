from check.file_name import File_Name 

class Format:

    def __init__(self,File_Path):

        self.File_Path = File_Path
        
    def check(self):

        file_name = File_Name(self.File_Path).get()
        file_type = file_name.split('.')[len(file_name.split(".")) - 1]

        return file_type
