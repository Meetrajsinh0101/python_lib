import numpy as np

# Task 2: 
followers = np.array([1200, 15000, 67000, 340000, 1250000])
print("Followers array:", followers)
print("Shape:", followers.shape)
print("Dimensions:", followers.ndim)
print("Data type:", followers.dtype)

print()

# Task 3: 
order_ids = np.arange(101, 111)
print("Order IDs:", order_ids)
print("Size:", order_ids.size)

print()

# Task 4: 
like_matrix = np.eye(3)
print("Like matrix:\n", like_matrix)



print()

# Task 5: 
scores_list = [45, 67, 120, 89, 54]
scores = np.array(scores_list)
print("Cricket scores array:", scores)
print("Bytes per score (itemsize):", scores.itemsize)
