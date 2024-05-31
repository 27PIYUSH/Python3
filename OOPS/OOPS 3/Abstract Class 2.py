from abc import ABC , abstractmethod
class TextReaderAbstract(ABC):
    def __init__(self,path,filename):
        self.path=path
        self.filename=filename

    @abstractmethod #htis is just an interface or rule
    def get_path(self):
        pass
    @abstractmethod
    def get_filename(self):
        pass

class TextReader(TextReaderAbstract):
    def get_path(self):
        return self.path
    
    def get_filename(self):
        return self.filename

myobj=TextReader("C:\Data Structures\OOPS\OOPS 3\Abstract Class 2.py","Abstract class 2")
print(myobj.get_path())
print(myobj.get_filename())