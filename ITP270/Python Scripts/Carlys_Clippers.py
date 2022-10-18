# Three lists for Carly's Clippers
hairstyles = ['bouffant', 'buzz cut', 'crew cut', 'high fade', 'mullet']
prices = [32, 28, 25, 27, 30]
last_week = [5, 6, 2, 7, 1]

# Initializing total price variable
total_price = 0

# Summing total price of all haircuts for average
for price in prices:
    total_price = total_price + price

# Validating previous for loop
print(total_price)

# Calculating the average price of a haircut at Carly's
average_price = total_price/len(prices)
print("Average Haircut Price: " + str(average_price))

# Creating a new discounted haircut price list
new_prices = [prices[0]-5, prices[1]-5, prices[2]-5, prices[3]-5, prices[4]-5]
print(new_prices)

# Initialize total revenue variable
total_revenue = 0

# Finding last week's total revenue
for i in range(0, len(hairstyles)):
    total_revenue = total_revenue + (prices[i] * last_week[i])

print("Total Revenue: " + str(total_revenue))

# Initializing average daily revenue variable

average_daily_revenue = total_revenue / 7

# Printing the avg. daily revenue
print("Average Daily Revenue: " + str(average_daily_revenue))

# Creating a list of haircuts under 30 dollars
cuts_under_30 = new_prices

#Printing the list
print(cuts_under_30)
