class Spends:
    
    def __init__(self):
        pass

    def get_total(self, costs, items, tax):
        total=0
        for item in items:
            if item in costs:
                total+=costs[item]
        return round(total+(total*tax),2)

if __name__ == "__main__":
    s = Spends()
    costs = {'socks':5, 'shoes':60, 'sweater':30}
    print(s.get_total(costs, ['socks','shoes'], 0.09))
    print(s.get_total(costs, ['socks','shoes','sweater','hat','shirt'], 0.10))