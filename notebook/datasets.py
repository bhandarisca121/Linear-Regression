import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 100

# Generate features with one decimal point
square_feet = np.round(np.random.uniform(1000, 5000, n_samples), 1)
bedrooms = np.random.randint(1, 6, n_samples)
age = np.round(np.random.uniform(0, 50, n_samples), 1)

# Generate target (price) with one decimal point
price = np.round((200 * square_feet + 50000 * bedrooms - 1000 * age + 
                 np.random.normal(0, 50000, n_samples)), 1)

# Create DataFrame
house_data = pd.DataFrame({
    'square_feet': square_feet,
    'bedrooms': bedrooms,
    'house_age': age,
    'price': price
})

# Save to CSV
house_data.to_csv('house_prices.csv', index=False)

# Save to CSV
house_data.to_csv('house_prices.csv', index=False)
