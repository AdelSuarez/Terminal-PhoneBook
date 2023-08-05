import os

class Clear:
    def __init__(self) -> None:
        
        if os.name == 'nt':
            # Windows
            os.system("cls")
        else:
            #linux
            os.system("clear")