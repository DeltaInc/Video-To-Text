class File_Name:

    def __init__(self,File_Path:str,Split:str=None):
        self.File_Path = File_Path
        if Split == None:
            self.Split = "\\"
        
        else:
            self.Split = Split
            
    def get(self):
        file_address = self.File_Path.removesuffix(self.File_Path.split(self.Split)[len(self.File_Path.split(self.Split)) - 1])
        file_name = self.File_Path.removeprefix(file_address)
        
        return file_name