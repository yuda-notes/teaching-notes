# Data Analysis with Pandas - Exercise

## Dataset
You'll be working with a dataset of 1,000 trending YouTube videos:
- **Dataset URL**: [trending-youtube-videos.csv](https://raw.githubusercontent.com/yuda-notes/teaching-notes/refs/heads/main/dataset/trending-youtube-videos.csv)
- **Columns**:
  - `video`: Video title
  - `video_views`: Number of views
  - `likes`: Number of likes
  - `dislikes`: Number of dislikes
  - `category`: Video category
  - `published`: Year published

## Tasks

### 1. Data Loading
- Load the dataset from the provided URL into a Pandas DataFrame

### 2. Data Exploration
- Display the first 5 rows of the dataset
- Show the dataset information (columns, data types, non-null counts)
- Display basic statistics for numerical columns

### 3. Data Manipulation
1. Extract the first 10 videos in the "Music" category
2. Remove all rows where category is "Gaming"
3. Filter the dataset to only include videos published before 2021
4. Create a new column called `label` that combines the `video` title and `category` in the format: "[video title] - [category]"

### 4. Data Aggregation
1. Calculate how many videos exist in each category
2. Determine which category has the most videos
3. Compute the average number of views grouped by publication year

### Bonus - Optional
- Save your final processed DataFrame to a new CSV file named `processed_trending_videos.csv`

---

**Note**: Perform all tasks in a Jupyter Notebook and show your results.
