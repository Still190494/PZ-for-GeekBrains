# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
from utils.currency_rates import currency_rates
import sys
print(currency_rates(sys.argv[1]))