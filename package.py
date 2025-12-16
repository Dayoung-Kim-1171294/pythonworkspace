# Once you import the file, the code in the file is executed.(Thailand file executed)
import travel.thailand
# use basic constructor that comes from parent class(Object class)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()

from travel import *
trip_to3 = thailand.ThailandPackage()