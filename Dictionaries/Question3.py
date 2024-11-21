#3) Given a dictionary representing items in a store with their prices,{'apple': 0.5, 'banana': 0.3, 'orange': 0.7},
# write a program that takes a list of items bought,['apple', 'orange', 'banana', 'banana'],and calculates the total cost.
def calculate_total_cost(items_bought, store_prices):
    total = 0
    for item in items_bought:
        total += store_prices.get(item, 0) 
    return total
store_prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = calculate_total_cost(items_bought, store_prices)
print(total_cost)  
