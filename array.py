import numpy as np


transactions = np.array([
    [1200, 1500, 1300, 1600, 1700, 1800],   
    [1100, 1400, 1350, 1500, 1550, 1600],  
    [2000, 2200, 2100, 2300, 2400, 2500],  
    [1000, 950, 1100, 1200, 1150, 1300]    
])


total_per_branch = np.sum(transactions, axis=1)
print("Total transactions per branch:", total_per_branch)


highest_branch = np.argmax(total_per_branch) + 1
print("Branch with the highest total transactions: Branch", highest_branch)


average_monthly = np.mean(transactions)
print("Average monthly transaction volume across all branches:", average_monthly)


reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)


print("""
Reshaping changes how data is organized in memory but not the data itself.
Here, we combined 4x6 = 24 elements into a new 3x8 layout, useful for different analytical perspectives.
""")
