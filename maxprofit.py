def max_profit(prices):
    i=0
    if len(prices) < 1 or len(prices) > pow(10,5) or prices[i] < 1 or prices[i] > pow(10,4):
        return ValueError("price out of the range")
    
    if not prices:
        return 0
        

    min_price = prices[0]  
    max_profit = 0  

    for price in prices:
        
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


prices = list(map(int,input().split()))
result = max_profit(prices)
print("Max profit from this transaction:",result)
