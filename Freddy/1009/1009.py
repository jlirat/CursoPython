name = input()
salary = float(input())
totalsales = float(input())
sellsextra = totalsales * 0.15
finalsalary = salary + sellsextra
print('Total = $R {:.2f}'.format(finalsalary))