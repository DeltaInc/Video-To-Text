class DVP:
    def __init__(self,File_Path:str):
        self.File_Path = File_Path
        self.Outpot_Path = ""
        self.ffmpeg_Path = "<Your ffmpeg.exe Path>"#For Exmaple: E:/ffmpeg/bin/ffmpeg.exe

    def ToAudio(self):
        import os
        from check.format import Format
        from check.file_name import File_Name

        self.file_name = File_Name(self.File_Path,'/').get().split(".")[0]
        self.file_fname = self.File_Path.split('/')[len(self.File_Path.split('/')) - 1]
        self.file_address = self.File_Path.removesuffix(self.file_fname)
        self.new_file = str(self.file_address + self.file_name)

        self.File_Format = Format(self.File_Path).check()
        if self.File_Format == "mp4":
            self.Outpot_Path = f'{self.new_file}.mp3'
            os.system(f"{self.ffmpeg_Path} -i {self.File_Path} -map 0:a {self.Outpot_Path}")

        elif self.File_Format == "mkv":
            self.Outpot_Path = f'{self.new_file}.m4a'
            os.system(f"{self.ffmpeg_Path} -i {self.File_Path} -map 0:a {self.Outpot_Path}")

        elif self.File_Format == "avi":
            self.Outpot_Path = f'{self.new_file}.mka'
            os.system(f"{self.ffmpeg_Path} -i {self.File_Path} -map 0:a -c:a aac {self.Outpot_Path}")

    def ToText(self,Lang:str,EndFile_Path:str):
        from dap.core import DAP
        __class__(self.File_Path).ToAudio()
        DAP(self.Outpot_Path,Lang).ToText()