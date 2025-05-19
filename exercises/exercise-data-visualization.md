# Data Visualization - Exercise

## Dataset

## Instruction

- Create visualizations based on this dataset.
- Dataset link: https://github.com/yuda-notes/teaching-notes/raw/refs/heads/main/dataset/cleaned-youtube-videos.csv

Sample Preview:

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>video</th>
      <th>video_views</th>
      <th>likes</th>
      <th>dislikes</th>
      <th>category</th>
      <th>published</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lil Nas X - Old Town Road (Official Movie) ft....</td>
      <td>54071677</td>
      <td>3497955</td>
      <td>78799</td>
      <td>Music</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>JP Saxe - If the World Was Ending (Official Vi...</td>
      <td>76834495</td>
      <td>804353</td>
      <td>21195</td>
      <td>Music</td>
      <td>2019</td>
    </tr>
    <tr>
      <td>Power Star Pawan Kalyan Special Surprise To Se...</td>
      <td>96686</td>
      <td>1007</td>
      <td>82</td>
      <td>Entertainment</td>
      <td>2018</td>
    </tr>
    <tr>
      <td>Totti with a funny penalty</td>
      <td>8353318</td>
      <td>5613</td>
      <td>1082</td>
      <td>Sports</td>
      <td>2007</td>
    </tr>
    <tr>
      <td>Polo G, Stunna 4 Vegas &amp; NLE Choppa feat. Mike...</td>
      <td>7396199</td>
      <td>320910</td>
      <td>6485</td>
      <td>Music</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
</div>

## 1. Category Distribution

Create a bar chart showing the number of videos in each category. This helps understand which category appears most frequently in trending content.

## 2. Likes vs. Views Comparison

Create a scatter plot to show the relationship between the number of likes and views. Each dot represents a video. What kind of trend or correlation can you observe?

## 3. Average Views per Category

Group the videos by category and calculate the average number of views per category. Create a horizontal bar chart to show the result.

## 4. Trend Over Time

Create a line chart showing how many trending videos were published each year. Use the published column to extract the year.

## Bonus

Create a heatmap that compares likes and dislikes by category using color intensity.

**Notes**

- Work on **Notebook** or **Colab**
- You can choose `matplotlib`, `seaborn`, or `plotly`
- Report to the instructor if finished!
