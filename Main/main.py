# Now I retrieve Variables and values

from Dao.Artist import *
obj1=Artist()
obj1.getter()
#obj1.setter()
#obj1.update()
#obj1.delete()
print("............................")

from Dao.Artwork import *
obj2=Artwork()
obj2.getter()
#obj2.setter()
#obj2.update()
#obj2.delete()

print(".................................")

from Dao.User import *
obj3=User()
obj3.getter()
#obj3.setter()
#obj3.update()
#obj3.delete()

print(".....................................")

from Dao.Gallery import *

obj4=Gallery()
obj4.getter()
#obj4.setter()
#obj4.update()
#obj4.delete()

print(".......................")

from Exception.ArtWorkNotFoundException import *

obj5=ArtworkException()
obj5.RaiseException()
print(".........................")

from Exception.UserNotFoundException import *

obj6=UserException()
obj6.RaiseException()