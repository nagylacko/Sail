

class Buoys:
    
    def __init__(self):
        self.buoys = []
        
        self.buoys.append(_Buoy(400,500))
        self.buoys.append(_Buoy(300,200))        
        self.buoys.append(_Buoy(600,100))
        self.buoys.append(_Buoy(600,600))
        self.buoys.append(_Buoy(60,100))
        
    def __getitem__(self, index):
        return self.buoys[index]
        
    def __iter__(self):
        return self.buoys.__iter__()
    
    def __len__(self):
        return len(self.buoys)

class _Buoy:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
