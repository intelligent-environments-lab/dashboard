import os
import string

class Library:
    def __init__(self) -> None:
        self.path = 'figures'
        section_names = os.listdir(self.path)
        self.sections = {name:Section(self.path+'/'+name) for name in section_names}
        print()
    
    def show():
        for _, section in self.sections.items():
            section.show()
            
class Section:
    def __init__(self, path) -> None:
        self.path = path
        subsection_names = os.listdir(self.path)
        self.subsections = {name:Subsection(self.path+'/'+name) for name in subsection_names}
    
    def show():
        name = string.capwords(self.name.replace('_',' ').replace('and','&'))
        for _, subsection in self.subsections.items():
            subsection.show()
            
    @property
    def name(self):
        return self.path[self.path.rfind('/')+1:]
    
        
class Subsection:
    def __init__(self, path) -> None:
        self.path = path
        file_names = os.listdir(self.path)
    
    def show():
    @property
    def name(self):
        return self.path[self.path.rfind('/')+1:]
    
class Figure:
    
    def show():
        
test = Library()