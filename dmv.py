#!/usr/bin/env python
# coding: utf-8

# # 1 dmv

# In[ ]:


import warnings 
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json
import seaborn as sns

csv = pd.read_csv("sales data.csv")
ed = pd.read_excel("sales data.xlsx")
jd=pd.read_json("sales data.json")
all_data = pd.concat([csv, ed, jd], ignore_index=True)
print("Data Combined Successfully")
print("Missing Values:\n", all_data.isnull().sum())

all_data.drop_duplicates(inplace=True)
print("Duplicates Removed Successfully")
all_data

all_data['Date'] = pd.to_datetime(all_data['Date'], errors='coerce')  #trans

csv.boxplot()
sns.pairplot(ed)
plt.show()

plt.figure(figsize=(20,10))
category_counts = all_data['Rating'].value_counts()
category_counts.plot(kind='bar')
plt.title('Product Category Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()


# # 2 dmv

# In[ ]:


df= pd.read_csv('weather.csv')
df


# In[ ]:


df.isnull().sum()


# In[ ]:


# Group by date and calculate average temperature
avg_temp = df.groupby('Date.Full')['Data.Temperature.Avg Temp'].mean().reset_index()

# Visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(avg_temp['Date.Full'], avg_temp['Data.Temperature.Avg Temp'], marker='o', color='blue')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°F)')
plt.xticks(rotation=45)
plt.grid()
plt.show()


# In[ ]:


# Group by date and calculate total precipitation
total_precipitation = df.groupby('Date.Full')['Data.Precipitation'].sum().reset_index()

# Visualization
plt.figure(figsize=(12, 6))
plt.bar(total_precipitation['Date.Full'], total_precipitation['Data.Precipitation'], color='skyblue')
plt.title('Total Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (inches)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[ ]:


# Group by city and calculate average wind speed
avg_wind_speed = df.groupby('Station.City')['Data.Wind.Speed'].mean().reset_index()

# Visualization
plt.figure(figsize=(20, 8))
plt.bar(avg_wind_speed['Station.City'], avg_wind_speed['Data.Wind.Speed'], color='orange')
plt.title('Average Wind Speed by City')
plt.xlabel('City')
plt.ylabel('Average Wind Speed (mph)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# # 3 dmv

# In[ ]:


import pandas as pd


# In[ ]:


df=pd.read_csv('telecom_churn.csv')
df


# In[ ]:


# Convert 'date_of_registration' to datetime
df['date_of_registration'] = pd.to_datetime(df['date_of_registration'], errors='coerce')

# Handle missing or invalid data in 'data_used'
df['data_used'] = df['data_used'].apply(lambda x: abs(x) if x < 0 else x)

# Check for any remaining missing values
print(df.isnull().sum())


# In[ ]:


df


# In[ ]:


# Calculate tenure (years as a customer)
df['tenure_years'] = (pd.to_datetime("2024-01-01") - df['date_of_registration']).dt.days // 365

# Binning 'estimated_salary' into income brackets
df['income_bracket'] = pd.cut(df['estimated_salary'], bins=[0, 50000, 100000, 150000, 200000], labels=['Low', 'Medium', 'High', 'Very High'])

# Convert categorical variables to numeric
df = pd.get_dummies(df, columns=['telecom_partner', 'gender', 'state', 'city', 'income_bracket'], drop_first=True)


# In[ ]:


df


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

# Churn distribution
sns.countplot(x='churn', data=df)
plt.title('Churn Distribution')
plt.show()

# Numerical feature analysis
numerical_features = ['age', 'num_dependents', 'estimated_salary', 'calls_made', 'sms_sent', 'data_used', 'tenure_years']
for feature in numerical_features:
    plt.figure()
    sns.boxplot(x='churn', y=feature, data=df)
    plt.title(f'{feature} vs. Churn')
    plt.show()

# Categorical feature analysis (e.g., telecom_partner)
sns.countplot(x='telecom_partner_Reliance Jio', hue='churn', data=df)
plt.title('Churn by Telecom Partner')
plt.show()


# # dmv 4

# In[ ]:


df=pd.read_csv('Real-Estate dataset.csv')
df


# In[ ]:


# Check for missing values
print(df.isnull().sum())

# Convert binary categorical columns to 0 and 1
binary_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for col in binary_columns:
    df[col] = df[col].apply(lambda x: 1 if x == 'yes' else 0)

# Convert categorical column 'furnishingstatus' to numerical encoding
df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)


# In[ ]:


# Add 'price_per_sqft' feature
df['price_per_sqft'] = df['price'] / df['area']

# Add 'total_rooms' feature
df['total_rooms'] = df['bedrooms'] + df['bathrooms']

# Create 'luxury_index' based on amenities
df['luxury_index'] = df[['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']].sum(axis=1)


# In[ ]:


df


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

# Correlation matrix
plt.figure(figsize=(18,12))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Scatter plot for 'area' vs 'price'
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='area', y='price')
plt.title("Area vs Price")
plt.show()

# Box plot for 'furnishingstatus' vs 'price'
plt.figure(figsize=(8,6))
sns.boxplot(x='furnishingstatus_semi-furnished', y='price', data=df)
plt.title("Furnishing Status vs Price")
plt.show()


# In[ ]:


from sklearn.preprocessing import StandardScaler

# List of numerical columns to scale
num_cols = ['price', 'area', 'price_per_sqft', 'total_rooms', 'luxury_index', 'bedrooms', 'bathrooms', 'stories', 'parking']

# Apply standard scaling
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])


# In[ ]:


df


# # 5 dmv

# In[ ]:


df=pd.read_csv('AQI Data Set.csv')
df


# In[ ]:


# Check for missing values
print(df.isnull().sum())

# Fill missing values (for this example, we'll fill with the mean of the columns)
df.fillna(df.mean(), inplace=True)

# Verify the changes
print(df.isnull().sum())
df=df.dropna()


# In[ ]:


# Convert 'Months' to datetime
df['Mounths'] = pd.to_datetime(df['Mounths'], format='%b-%y')

# Sort the DataFrame by 'Months'
df.sort_values('Mounths', inplace=True)

print(df)


# In[ ]:


import matplotlib.pyplot as plt

# Set the style for the plots
plt.style.use('seaborn-darkgrid')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot AQI trends
ax.plot(df['Mounths'], df['AQI'], marker='o', label='AQI', color='blue')

# Plot trends for different pollutants
ax.plot(df['Mounths'], df['PM10'], marker='o', label='PM10', color='orange')
ax.plot(df['Mounths'], df['SO2'], marker='o', label='SO2', color='green')
ax.plot(df['Mounths'], df['NOx'], marker='o', label='NOx', color='red')
ax.plot(df['Mounths'], df['PM2.5'], marker='o', label='PM2.5', color='purple')

# Add labels and title
ax.set_xlabel('Mounths', fontsize=14)
ax.set_ylabel('Concentration (µg/m³)', fontsize=14)
ax.set_title('Air Quality Index (AQI) Trends and Pollutants', fontsize=16)
ax.legend()
ax.grid()

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# # 6 dmv

# In[ ]:


df=pd.read_csv('retail_sales_data.csv')
df


# In[ ]:


# Calculate total sales
df['total_sales'] = df['quantity'] * df['price']

# Group by shopping mall and sum the sales
sales_by_region = df.groupby('shopping_mall')['total_sales'].sum().reset_index()

# Sort by total sales in descending order
sales_by_region = sales_by_region.sort_values(by='total_sales', ascending=False)

print(sales_by_region)


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(sales_by_region['shopping_mall'], sales_by_region['total_sales'], color='skyblue')
plt.title('Total Sales Performance by Shopping Mall')
plt.xlabel('Shopping Mall')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


# Calculate total sales by category
sales_by_category = df.groupby('category')['total_sales'].sum().reset_index()

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sales_by_category['category'], sales_by_category['total_sales'], color='lightgreen')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


# Calculate total sales by payment method
sales_by_payment_method = df.groupby('payment_method')['total_sales'].sum().reset_index()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sales_by_payment_method['total_sales'], labels=sales_by_payment_method['payment_method'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Payment Method')
plt.axis('equal')  # Equal aspect ratio
plt.show()


# In[ ]:


# Calculate total sales by gender and category
sales_by_gender_category = df.groupby(['gender', 'category'])['total_sales'].sum().unstack()

# Create a grouped bar chart
sales_by_gender_category.plot(kind='bar', figsize=(10, 6), color=['#ff9999', '#66b3ff'])
plt.title('Sales Performance by Gender and Category')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.legend(title='Product Category')
plt.show()


# In[ ]:



