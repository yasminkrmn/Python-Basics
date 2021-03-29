# Statements - Loops - Comprehensions

# if-elif-else
num = 10
if num > 0:
    print("Number is positive")
elif sayi < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
# Number is positive


# for - while loops
counter = 0
while counter < 36:
    if counter % 8 == 0:
        print(counter)
    counter += 1

# 0
# 8
# 16
# 24
# 32

# Break & Continue
for num in range(1, 36):
    if num % 8 == 0:
        if num in [8,24]:
            continue
        print(num)
# 16
# 32

while True:
    num = int(input("Enter a number (Press 0 to quit): "))
    if num == 0:
        print("The program has been successfully terminated.")
        break
    elif num < 0:
        print("Number is negative.")
    else:
        print("Number is positive.")

# Enter a number (Press 0 to quit): >? 10
# Number is positive.
# Enter a number (Press 0 to quit): >? -5
# Number is negative.
# Enter a number (Press 0 to quit): >? 0
# The program has been successfully terminated.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, "=", x, "*", int(n/x))
            break
    else:
         print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 = 2 * 2
# 5 is a prime number
# 6 = 2 * 3
# 7 is a prime number
# 8 = 2 * 4
# 9 = 3 * 3

# Compherensions

# List comprehensions
# [expression iteration]
[num for num in range(0, 10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [expression iteration condition]
[num for num in range(0, 10) if num < 6]
# [0, 1, 2, 3, 4, 5]

# [expression1 if condition else expression2 iteration]
["positive" if num > 0 else "negative" for num in [-4, 2, -1, 8, -9]]
# ['negative', 'positive', 'negative', 'positive', 'negative']

# [expression1 if condition1 else (expression2 if condition2 else expression3) iteration]
["positive" if num > 0 else ("negative" if num < 0 else "zero") for num in [-5, 2, 0, -1, 0, -9]]
# ['negative', 'positive', 'zero', 'negative', 'zero', 'negative']

# [[expression iteration] iteration]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    print(matrix[i])
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
transposed = []
for i in range(3):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)
transposed
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
for i in range(3):
    print(transposed[i])
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# Same result via comprehension
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
for i in range(3):
    print(transposed[i])
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# [expression1 iteration expression2 iteration]
my_list = [['40', '20', '10', '30'],
           ['30', '20', '30', '50', '10', '30', '20', '20', '20'],
           ['100', '100'], ['100', '100', '100', '100']]

new_list = []
for sub_list in my_list:
    for num in sub_list:
        new_list.append(int(num))
new_list
# [40,
#  20,
#  10,
#  30,
#  30,
#  20,
#  30,
#  50,
#  10,
#  30,
#  20,
#  20,
#  20,
#  100,
#  100,
#  100,
#  100,
#  100,
#  100]

[int(num)
 for sub_list in my_list
 for num in sub_list]
# [40,
#  20,
#  10,
#  30,
#  30,
#  20,
#  30,
#  50,
#  10,
#  30,
#  20,
#  20,
#  20,
#  100,
#  100,
#  100,
#  100,
#  100,
#  100]

# Dict Compherensions

# Creating a dictionary by assigning id values to the list ["REG", "LOJ", "GBM", "CART", "RF"] starting from 1.
my_list = ["REG", "LOJ", "GBM", "CART", "RF"]
# Long way
my_dict = {}
for id, name in enumerate(my_list, start=1):
    my_dict[id] = name
my_dict
# {1: 'REG', 2: 'LOJ', 3: 'GBM', 4: 'CART', 5: 'RF'}

# Easy way
{id:name for id, name in enumerate(my_list, start=1)}
# {1: 'REG', 2: 'LOJ', 3: 'GBM', 4: 'CART', 5: 'RF'}


#-------------------Some Examples-------------------
# EXP 1: Expected Output for car crashes dataset:

# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.dtypes
# total             float64
# speeding          float64
# alcohol           float64
# not_distracted    float64
# no_previous       float64
# ins_premium       float64
# ins_losses        float64
# abbrev             object
# dtype: object

agg_list = ['mean', 'min', 'max', 'var']

# Long way
num_list = []
for col in df.select_dtypes(include=["float64"]):
    num_list.append(col)
# ['total',
#  'speeding',
#  'alcohol',
#  'not_distracted',
#  'no_previous',
#  'ins_premium',
#  'ins_losses']

agg_dict = {}
for col in num_list:
    agg_dict[col] = agg_list

agg_dict
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

# Short way
num_list = [col for col in df.select_dtypes(include=["float64"])]
{col: agg_list for col in num_list}
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}


# EXP 2: Create dictionary using numerical variables in tips dataset.
# Expected Output:
# {'total_bill': ['total_bill_mean', 'total_bill_min', 'total_bill_max', 'total_bill_sum'],
#  'tip': ['tip_mean', 'tip_min', 'tip_max', 'tip_sum'],
#  'size': ['size_mean', 'size_min', 'size_max', 'size_sum']}

df = sns.load_dataset("tips")
df.dtypes
# total_bill     float64
# tip            float64
# sex           category
# smoker        category
# day           category
# time          category
# size             int64
# dtype: object

# Long way:
agg_list = ['mean', 'min', 'max', 'sum']
num_cols = [col for col in df.select_dtypes(include=["int64", "float64"])]
# ['total_bill', 'tip', 'size']

agg_dict = {}
for col in num_cols:
    concat_list = []
    for stat in agg_list:
        concat_list.append(str(col + "_" + stat))
    agg_dict[col] = concat_list
agg_dict

# {'total_bill': ['total_bill_mean', 'total_bill_min', 'total_bill_max', 'total_bill_sum'],
#  'tip': ['tip_mean', 'tip_min', 'tip_max', 'tip_sum'],
#  'size': ['size_mean', 'size_min', 'size_max', 'size_sum']}

# Short way
agg_dict2 = {col: [str(col) + "_" + stat for stat in agg_list] for col in num_cols}
# {'total_bill': ['total_bill_mean', 'total_bill_min', 'total_bill_max', 'total_bill_sum'],
#  'tip': ['tip_mean', 'tip_min', 'tip_max', 'tip_sum'],
#  'size': ['size_mean', 'size_min', 'size_max', 'size_sum']}




