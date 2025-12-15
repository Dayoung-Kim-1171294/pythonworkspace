class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,
              self.price, self.completion_year)
        
house1 = House("Gangnam", "apt", "buying", "10", "2010")
house2 = House("Mapo", "officetel", "yearly rent", "5", "2007")
house3 = House("Songpa", "villa", "monthly rent", "500/50", "2000")        

houses = [house1, house2, house3]
print("Total number of houses: {}".format(len(houses)))

for house in houses:
    house.show_detail()