from check.file_name import File_Name

class DAP:#@Delta Audio Processors
    def __init__(self,File_Path:str=None,EndFile_Path:str=None,Lang:str=None):#@adr_file@to@adr_endfile@lang
        self.File_Path = File_Path
        self.Lang = Lang
        self.EndFile_Path = EndFile_Path
        if File_Path != None:
            self.file_name = File_Name(self.File_Path).get().split(".")[0] 
        else:
            self.file_name = None

    def ToText(self):
        DAP.__Start_Process(self)
        DAP.__WRIF(self)
        DAP.__Finish_Process(self)

    def __Start_Process(self):
        print("start!")

        import speech_recognition as sr

        self.Recognizer = sr.Recognizer()
        print(self.File_Path)
        self.Audio_file = sr.AudioFile(str(self.File_Path))
        with self.Audio_file as Source:
            self.Recognizer.adjust_for_ambient_noise(Source)
            self.audio = self.Recognizer.record(Source)
            self.Result = self.Recognizer.recognize_google(self.audio,language=str(self.Lang))

    def __WRIF(self):
        self.File =  open(str(self.EndFile_Path),'w+', encoding="utf-8")
        self.File.write(str(self.Result))
        self.File.close()
    
    def __Finish_Process(self):
        print("finish!")
