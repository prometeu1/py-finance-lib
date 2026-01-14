from finance_lib.asset import Action
from finance_lib.portfolio import Portfolio

portfolio = Portfolio()

apple = Action("AAPL", "Apple Inc.", 10, 150.0, 175.0)
tesla = Action("TSLA", "Tesla Inc.", 5, 200.0, 250.0)

portfolio = portfolio + apple + tesla

print(f"Nombre d'actions: {len(portfolio)}")
print(f"Valeur totale: {portfolio.get_total_value()}€")

for action in portfolio:
    print(f"{action} -> profit: {action.profit}€ ({action.profit_percent}%)")
