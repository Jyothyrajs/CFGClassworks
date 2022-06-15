oranges = 12
cost_per_orange = 0.5
total_cost  = oranges * cost_per_orange
output = "{} Oranges of {}  cost {}"
print(output.format(oranges,cost_per_orange,total_cost))

hat1_cost = 10
hat2_cost = 30
amount = 30
output = "You can buy {} hats of hat1 cost {}"
print(output.format(amount//hat1_cost,hat1_cost))
print(output.format(amount//
                    hat2_cost,hat2_cost))

disposable_amt = 30
price_hat_1 = 10
price_hat_2 = 30
print("With {} pounds you can buy {} hats costing {} per hat or {} hats costing {} per hat"
      .format(disposable_amt, disposable_amt/price_hat_1, price_hat_1, disposable_amt/price_hat_2, price_hat_2))

hat1 = 10
hat2 = 30
budget = 30

total1 = budget // hat1
total2 = budget // hat2

print('With a budget of £{} you can afford to buy {} of hat2'.format(budget, total1))
print('With a budget of £{} you can afford {} of hat2'.format(budget, total2))