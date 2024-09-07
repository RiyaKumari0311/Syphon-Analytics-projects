'''
10. You work for a manufacturer, and have been asked to calculate the total profit made on the sales
of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per
unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest
dollar.
Examples
profit({
"cost_price": 32.67,
"sell_price": 45.00,
"inventory": 1200
}) ➞ 14796
'''

def profit(sales_data):
    cost_price = sales_data["cost_price"]
    sell_price = sales_data["sell_price"]
    inventory = sales_data["inventory"]
    
    # Calculate profit per unit
    profit_per_unit = sell_price - cost_price
    
    # Calculate total profit
    total_profit = profit_per_unit * inventory
    
    # Return rounded total profit
    return round(total_profit)

sales_data = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}

print(profit(sales_data))  # Output: 14796
