class item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = profit/weight
        
def fractionalKnapSack(profit,weight, capacity):
    items = (item(profit[i],weight[i]) for i in range(len(profit)))
    items = sorted(items , key = lambda x : x.ratio)
    items.reverse()
    
    final_profit = 0
    
    for i in items:
        if i.weight <= capacity:
            capacity = capacity - i.weight
            final_profit = final_profit + i.profit
        else:
            final_profit = capacity * i.profit/i.weight
            break
        
    return final_profit
        

profit = [int(x) for x in input("Enter Profit").split()]
weight = [int(x) for x in input("Enter Weight").split()]
capacity = int(input("Enter Capacity"))
    
print(fractionalKnapSack(profit,weight,capacity))
    
