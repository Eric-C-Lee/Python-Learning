counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
filtered_counts = {key: value for key, value in counts.items() if value >= 200}
print(filtered_counts)
