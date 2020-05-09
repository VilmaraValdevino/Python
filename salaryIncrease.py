#Algorithm that calculates a salary increase.
#He requests the salary amount and the percentage of the increase, and then displays the amount of the raise and the new salary


s = float(input('Salary: '))
i = float(input('Increase%: '))
increase = s * i / 100
new = s + increase
print(f'Increase: R$ {increase:.2f}')
print(f'New salary: R$ {new:.2f}')
