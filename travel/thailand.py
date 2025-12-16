class ThailandPackage:
    def detail(self):
        print("Thailand 5 nights 6 days package")   

print("__name__:", __name__)
if __name__ == "__main__":
    print("Thailand module is being run directly")
    trip = ThailandPackage()
    trip.detail()
else:
    #__name__: travel.thailand
    print("Thailand module imported")