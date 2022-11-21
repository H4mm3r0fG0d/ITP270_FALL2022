class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = {}
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        self.purchased_items = {}
        total = 0
        for item in purchased_items:


brunch = Menu("Brunch", {'pancakes':7.50, 'waffles':9.00, 'burger':11.00, 'home fries':4.50, 'coffee':1.50, 'espresso':3.00, 'tea':1.00, 'mimosa':10.50, 'orange juice':3.50}, "11:00 AM", "4:00 PM")

early_bird = Menu("Early-bird Dinner", {'salumeria plate':8.00, 'salad and breadsticks (serves 2, no refills)':14.00, 'pizza with quattro formaggi':9.00, 'duck ragu':17.50, 'mushroom ravioli (vegan)':13.50, 'coffee':1.50, 'espresso':3.00}, "3:00 PM", "6:00 PM")

dinner = Menu("Dinner", {'crostini w/ eggplant caponata':13.00, 'caesar salad':16.00, 'pizza with quattro formaggi':11.00, 'duck ragu':19.50, 'mushroom ravioli(vegan)':13.50, 'coffee':2.00, 'espresso':3.00}, "5:00 PM", "11:00 PM")

kids = Menu("Kids", {'chicken nuggets':6.50, 'fusilli w/ wild mushrooms':12.00, 'apple juice':3.00}, "11:00  AM", "9:00 PM")

# Testing the __repr__ function 
#print(brunch)
#print(early_bird)
#print(dinner)
#print(kids)
