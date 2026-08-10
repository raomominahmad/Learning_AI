daily_sales = [5,10,17,7,3,8,9,15]


# generator 
# (expression for item in iterable)
total_cups = sum (sale for sale in daily_sales if sale > 5)
# total_cups = [ sale for sale in daily_sales if sale > 5]

print(total_cups)

