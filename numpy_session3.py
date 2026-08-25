import numpy as np

# Task 1: 
friend1_steps = np.array([7000, 8500, 9200, 6000, 10000, 7500, 8800])
friend2_steps = np.array([6500, 9000, 8700, 7200, 9500, 8000, 9100])

print("Friend 1 steps:", friend1_steps)
print("Friend 2 steps:", friend2_steps)
print("Addition:", friend1_steps + friend2_steps)
print("Subtraction:", friend1_steps - friend2_steps)
print("Multiplication:", friend1_steps * friend2_steps)
print("Division:", friend1_steps / friend2_steps)

print()

# Task 2: 
user_preferences = np.array([
    [0.8, 0.2, 0.5],
    [0.3, 0.9, 0.1],
    [0.6, 0.4, 0.7]
])

song_popularity = np.array([
    [0.7, 0.3, 0.4],
    [0.5, 0.8, 0.2],
    [0.6, 0.1, 0.9]
])

dot_result = user_preferences.dot(song_popularity)
matmul_result = np.matmul(user_preferences, song_popularity)

print("User preferences matrix:\n", user_preferences)
print("Song popularity matrix:\n", song_popularity)
print("Recommendation matrix using dot():\n", dot_result)
print("Recommendation matrix using matmul():\n", matmul_result)

print()

# Task 3: 
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

rotated_image = image.T
print("Original image:\n", image)
print("Transposed (rotated) image:\n", rotated_image)
print("Mean:", np.mean(image))
print("Median:", np.median(image))
print("Standard deviation:", np.std(image))
print("Variance:", np.var(image))

print()

# Task 4: 
correlation_grid = np.array([
    [1.0, 0.5, 0.3],
    [0.5, 1.0, 0.4],
    [0.3, 0.4, 2.0]   
])

inverse_matrix = np.linalg.inv(correlation_grid)
determinant = np.linalg.det(correlation_grid)
eigenvalues, eigenvectors = np.linalg.eig(correlation_grid)

print("Correlation grid:\n", correlation_grid)
print("Inverse matrix:\n", inverse_matrix)
print("Determinant:", determinant)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

print()

# Task 5: 
orders = np.array([
    [120, 135, 150, 140, 160, 155],   
    [110, 125, 130, 145, 150, 160]    
])

reshaped_orders = orders.reshape(3, 4)
flattened_orders = reshaped_orders.flatten()
split_parts = np.split(flattened_orders, 2)
stacked_orders = np.vstack((split_parts[0], split_parts[1]))

print("Original orders (2,6):\n", orders)
print("Reshaped (3,4):\n", reshaped_orders)
print("Flattened:", flattened_orders)
print("Split into two parts:", split_parts)
print("Stacked vertically:\n", stacked_orders)
