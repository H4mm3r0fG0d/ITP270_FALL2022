#1- print the list of the pizza toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#2- create a list of the pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

#testing the code

#3- print the number of times two dollars appears in the price list
print(num_two_dollar_slices)

#4- find the length of the toppings list
num_pizzas = len(toppings)

#5- Print the value of the number of pizzas in a string
pizza_string = f"We sell {num_pizzas} different kinds of pizza!"
print(pizza_string)

#6- create a two-dimensional list of pizza toppings and associated prices
pizza_and_prices = [[prices[0], toppings[0]],
                    [prices[1], toppings[1]],
                    [prices[2], toppings[2]],
                    [prices[3], toppings[3]],
                    [prices[4], toppings[4]],
                    [prices[5], toppings[5]],
                    [prices[6], toppings[6]]]

#7- print the list
print(pizza_and_prices)

#8- sort the list of pizza and prices in ascending order
pizza_and_prices.sort()

#9- store the cheapest pizza in a variable, print it out
cheapest_pizza = [pizza_and_prices[0]]
print(cheapest_pizza)

#10- a guest wants the priciest pizza, print it out
mstexp_pizza = [pizza_and_prices[-1]]
print(mstexp_pizza)

#11- remove anchovies from the toppings list
pizza_and_prices.pop()
print(pizza_and_prices)

pizza_and_prices.insert( int(2.5), 'peppers')
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
