
class Menu:
  """fill in class definition here"""
  def __init__(self,item,rate):
    self.item=item
    self.rate=rate
  
  def __setattr__(self,item,rate):
    print(f"You set {item} ={rate} ")
    self.__dict__[item]=rate
  
m = Menu('Poori','30')

m.idly=10
m.vada=20
m.dosa=30
print("\033[1m Printing Menu in Dictionary Type \033[0m")
print(m.__dict__)
