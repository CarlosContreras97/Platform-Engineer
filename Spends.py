class Spends:
    
    def __init__(self):
        pass

    def get_total(self, costs, items, tax):
        total=0
        for item in items:
            if item in costs:
                total+=costs[item]
        return total+(total*tax)

if __name__ == "__main__":
    s = Spends()
    costs = {'socks':5, 'shoes':60, 'sweater':30}
    print(s.get_total(costs, ['socks','shoes'], 0.09))
    print(s.get_total(costs, ['socks','shoes','sweater'], 0.10))