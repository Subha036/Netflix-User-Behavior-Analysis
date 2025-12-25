import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("netflix_data.csv")

# Top genres by watch hours
genre_watch = data.groupby('genre')['watch_hours'].sum()

# Watch hours per user
user_watch = data.groupby('user_id')['watch_hours'].sum()

# Average rating by genre
genre_rating = data.groupby('genre')['rating'].mean()

# Bar chart: Top genres
plt.figure(figsize=(7,5))
genre_watch.plot(kind='bar', title='Watch Hours by Genre')
plt.ylabel("Watch Hours")
plt.show()

# Line chart: Watch hours per user
plt.figure(figsize=(7,5))
user_watch.plot(kind='line', marker='o', title='User Watch Hours')
plt.xlabel("User ID")
plt.ylabel("Watch Hours")
plt.show()

# Bar chart: Ratings by genre
plt.figure(figsize=(7,5))
genre_rating.plot(kind='bar', title='Average Rating by Genre')
plt.ylabel("Rating")
plt.show()

print("Top Genres by Watch Hours:\n", genre_watch)
print("\nUser Watch Hours:\n", user_watch)
print("\nAverage Rating by Genre:\n", genre_rating)
