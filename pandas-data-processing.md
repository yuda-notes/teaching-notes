# Data Processing with Pandas

## Definition
- Data Processing is an activity that involves data manipulation and transformation to gain meaningful insights, facilitate analysis, and/or generate desired outputÏ
- Common task in Data Processing
  - Data Cleaning
  - Data Transformation
  - Data Integration
  - Data Aggregation
  - Filtering and Selection
  - Analysis
  - Data Visualization
  - And many more.
- Some common case for that involves data processing are:
  - Handle missing values
  - Handle duplicate values
  - Handle data inconcistencies 

## Handle Missing Values
<img src="https://github.com/user-attachments/assets/5e203835-2489-439f-8e6f-6864741b563d" width=500 />

- Characteristic of missing values
  - MCAR (Missing Completely At Random)
  - MAR (Missing At Random)
  - MNAR (Missing Not At Random)
 
### MCAR
- The missingness is completely unrelated to both observed and unobserved values in the dataset.
- In simpler terms, the absence of data occurs randomly, without any discernible pattern.
- A classic example of MCAR is when a survey participant unintentionally skips a question. The likelihood of data being missing is independent of any information present in the dataset.
### MAR
- The missingness can be explained by some observed features in the dataset.
- Although the data is missing systematically, it is still considered random because the missingness is not related to the unobserved values.
- For instance, in a tobacco study, younger participants might report their values less often (regardless of how much they smoke), leading to systematic missingness for age-related reasons.
### MNAR
- The missingness itself is related to the unobserved data. In this case, the missing data is not random and is associated with specific reasons or patterns.
- Referring to the tobacco study example, participants who smoke the most might intentionally withhold their smoking habits, leading to systematic missingness related to the missing data.

### Handling
<img src="https://github.com/user-attachments/assets/a3d61918-8719-43f5-9104-a4a8704ab733" width=500 />

- Delete rows/columns -> If the missing values are minimal and won't significantly impact the analysis, you can choose to delete rows or columns with missing values.
- Imputation -> When missing values are few and not too influential, imputing missing values using methods like mean, median, mode, or regression-based imputation can be suitable.
- Other specialized techniques -> Traditional imputation methods may not be suitable for MNAR data, and specialized techniques that consider the reasons for missingness are required.
```py
# check for missing values
df.isnull()

# drop missing values
df.dropnam()

# fill missing values
df.fillna(value)

# forward/backward fill
df.ffill()
# or
df.bfill()

# imputation using interpolation technique
df.interpolate
```

## Handle Duplicate Data 
- Duplicates refer to rows or records in a dataset that have identical values across all or most of their attributes.
- Duplicate data can occur due to various reasons, such as data entry errors, system glitches, or data integration processes.
```py
# check for duplicate values
df.duplicated()

# drop duplicate
df.drop_duplicates()
```

## Handle Data Inconsistencies
- To perform calculations or utilize the advance processing technique, you have to make sure that your data is in appropriate.
- Pandas data types are different with standard Python data types:
  - object -> same as 'str' in python
  - int64
  - float32
  - bool -> boolean
  - datetime
  - timedelta
```py
# convert data type of column
df.columnA = df.columnA.astype('int64')

# trim whitespace for each values in column
df.columnA = df.columnA.str.strip()

# set lowercase for each values in column
df.columnA = df.columnA.str.lower()
# uppercase
df.columnA = df.columnA.str.upper()

# remove or replace substring
df.columnA = df.columnA.str.replace('old_value', 'new_value')

# split string into list
df.columnA = df.columnA.str.split(' ') # split string by space (' ') character

# convert column to datetime
df.columnA = pd.to_datetime(df.columnA)

# extract datetime unit
df.year = df.columnA.dt.year # extract 'year' unit from datetime value

# formatting datetime to string
df.date_string = df.columnA.dt.strftime('%Y-%m-%d')

# extract time difference in each rows
df['time_diff'] = df['columnA'].diff()

# extract time intervals
df['time_interval'] = df['columnA'].diff().dt.total_seconds()

# convert timezone
df['columnA'] = df['columnA'].dt.tz_localize('UTC').dt.tz_convert('America/New_York') # convert from UTC to America/New York timezone
```
