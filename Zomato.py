# Importing necessary libraries
import matplotlib.pyplot as plt  # For plotting
import pandas as pd  # For data manipulation
import seaborn as sns  # For data visualization

# Load the dataset with the correct path handling
dataframe = pd.read_csv(r'Zomato data .csv')
print(dataframe.head())  # Display the first 5 rows of the dataframe

# Function to handle and convert the 'rate' column
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    try:
        return float(value)
    except ValueError:
        return None

# Apply the function to the 'rate' column
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())  # Display the first 5 rows of the dataframe after conversion

# Display dataframe information
dataframe.info()

# Plotting the count of restaurant types
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.title("Count of Restaurant Types")
plt.show()  # Show the plot

# Grouping the data by restaurant type and summing the votes
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})

# Plotting the sum of votes by restaurant type
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)
plt.title("Votes by Restaurant Type")
plt.show()  # Show the plot

# Finding the restaurant(s) with the maximum votes
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

# Plotting the count of online order availability
sns.countplot(x=dataframe['online_order'])
plt.title("Online Order Availability")
plt.show()  # Show the plot

# Plotting the distribution of ratings
plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()  # Show the plot

# Plotting the count of approximate cost for two people
couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.title("Approximate Cost for Two People")
plt.xlabel("Cost")
plt.ylabel("Count")
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.show()  # Show the plot

# Plotting a boxplot of ratings based on online order availability
plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe)
plt.title("Boxplot of Ratings by Online Order Availability")
plt.show()  # Show the plot

# Creating a pivot table and plotting a heatmap
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap of Online Orders by Restaurant Type")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()  # Show the plot
