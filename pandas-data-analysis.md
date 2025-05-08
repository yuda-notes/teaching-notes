# Data Analysis with Pandas

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*hHVINI5TGJB6jPKN.jpg)

## Definition
- Pandas is a library that provides data manipulation and analysis with specific data structure.
- There are 2 data structures in Pandas
  - DataFrame -> same like `table` in SQL, which consist of rows and columns
  - Series -> just a single column in DataFrame
 
![image](https://github.com/user-attachments/assets/91df71da-bf6f-4d7a-bb13-8f72e92358b6)

## Setup
```bash
conda install pandas
# or
pip install pandas
```

## Loading Data
- Pandas can load data from any sources, such as
  - CSV
  - Excel
  - JSON
  - SQL
  - and many [more](https://pandas.pydata.org/docs/reference/io.html)
- To load data in pandas
  ```py
  # import package
  import pandas as pd

  # load from CSV
  pd.read_csv("file_name.csv")

  # load from Excel
  pd.read_excel("file_name.xlsx")

  # load from links
  pd.read_csv("https://www.example.com/file_name.csv")
  ```

### Create DataFrame ([reference](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/))
- Create empty DataFrame
  ```py
  df = pd.DataFrame()
  ```
- Create DataFrame from Dictionary
  ```py
  # initialize dictionary
  data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
          'Age': [20, 21, 19, 18]}
  
  # Create DataFrame
  df = pd.DataFrame(data)
  ```
- Create DataFrame from List
  ```py
  # initialize list of lists
  data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
  # Create the pandas DataFrame
  df = pd.DataFrame(data, columns=['Name', 'Age'])
  ```
- Create DataFrame from List of Dictionary
  ```py
  # Initialize data to lists.
  data = [{'a': 1, 'b': 2, 'c': 3},
          {'a': 10, 'b': 20, 'c': 30}]
  
  # Creates DataFrame.
  df = pd.DataFrame(data)
  ```
- Create DataFrame from Dictionary of Series
  ```py
  # Initialize data to Dicts of series.
  d = {'one': pd.Series([10, 20, 30, 40],
                        index=['a', 'b', 'c', 'd']),
       'two': pd.Series([10, 20, 30, 40],
                        index=['a', 'b', 'c', 'd'])}
  
  # creates Dataframe.
  df = pd.DataFrame(d)
  ```
- And many more.

## Data Exploration
- Here are some snippets of code to do Data Exploration with Pandas
  ```py
  # import package
  import pandas as pd

  # load data
  df = pd.read_csv("file_name.csv")
  
  # get first N rows from DataFrame, by default is the first 5 rows
  df.head()

  # get last N rows from DataFrame, by default is the last 5 rows
  df.tail()

  # more examples
  df.head(10) # first 10 rows
  df.tail(3) # last 3 rows

  # get DataFrame dimension, in the form of tuple
  df.shape # ouput: (num_of_rows, num_of_columns)

  # get DataFrame columns
  df.columns

  # get DataFrame index
  df.index

  # get data types in each column of the DataFrame
  df.dtypes
  
  # get DataFrame summary
  df.info()

  # get descriptive statistic numbers for all numerical columns in DataFrame
  df.describe()

  # get number of unique values in each column of the DataFrame
  df.nunique()

  # get frequency count of unique values in each column of the DataFrame
  df.value_counts()

  # to check for missing values
  df.isnull()
  ```
## Data Manipulation
### Sorting ([reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html))
- By default, pandas will sort in ascending order.
  ```py
  # sort values by column name
  df.sort_values(by=["column1"])

  # sort values by multiple columns
  df.sort_values(by=["column1", "column2"])

  # to adjust ascending or descending, change the `ascending` parameter
  df.sort_values(by=["column1", ascending=False)
  ```
### Slicing/Accessing Columns and Rows ([reference](https://www.geeksforgeeks.org/slicing-indexing-manipulating-and-cleaning-pandas-dataframe/))
- Slice Colunns
  ```py
  # get single column
  df['column1']
  # or
  df.column1

  # get multiple columns
  df[['column1', 'column2']]
  ```
- Slice Rows
  - To slice rows in DataFrame we need to know whether its integer-based or label-based index
    - Integer-based indexing ([reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html))
      ```py
      # get single row by index
      df.iloc[1] # get row from index 1

      # get multiple rows (range of rows)
      df.iloc[4:51] # get row from index 4 to 50
      ```
    - Label-based indexing ([reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html))
      ```py
      # get single row
      df.loc['indexA'] # get row from 'indexA'

      # get multiple rows
      df.loc['indexB':'indexZ'] # get row from 'indexB' to 'indexZ'

      # get row by conditional expression
      df.loc[df.columnA > 100] # get all rows that have 'columnA' value more than 100
      ```
### Query/Filtering ([reference](https://builtin.com/data-science/pandas-filter))
- There are many ways to query data from Pandas, here are some snippets of it.
  ```py
  # get all data that have 'columnX' value equals to 'Hello'
  df[df['columnX'] == 'Hello']

  # query with multiple conditions (use `&` for AND, `|` for OR)
  df[ (df['columnX'] == 'Foo') & (df['columnY'] == 'Bar') ]

  # using `.query()` method
  df.query("columnX == 'Hello' and columnY == 'World'")

  # using `.isin()` method
  df[ df['columnX'].isin(['value1','value2','value3']) ]

  # get all data where 'columnX' contains specific string 'a'
  df[ df['columnX'].str.contains("a") ]
  ```
### Add Column and Row
- Column
  ```py
  # add new column with specified values
  df['new_column'] = list_of_value
  # or
  df.new_column = list_of_value

  # add new column with values from existing column
  df.new_column = df.columnX + 5 
  ```
- Row
  > `.append()` method is deprecated in latest pandas version.
  ```py
  # initialize dictionary for the new row
  data = {
      "Model":["Linear Regression"], 
      "R2":   [0.042], 
      "MSE":  [3.14],  
  }
      
  # we need a new DataFrame with the new contents
  df_new_rows = pd.DataFrame(data)
  
  # we can use `.concat()` method
  df = pd.concat([df, df_new_rows])
  ```
  - There are many other ways to add new row [here](https://www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/)
 
### Remove Column and Row
- Column
  ```py
  # using `.drop()` method, by default this will not change the existing DataFrame
  df.drop(columns=['columnA'])

  # to also change the existing DataFrame, set the `inplace` parameter to `True`
  df.drop(columns=['columnA'], inplace=True)
  # or
  df = df.drop(columns=['columnA']) # replace the variable

  # other ways to delete column, using `del` keyword
  del df['columnA']
  ```
- Row
  ```py
  # same like column, we can also use `.drop()` method for rows
  df.drop(index=[0, 1]) # remove rows in index 0 and 1

  # other ways to delete row, using query/filtering
  df = df[ ~(df.columnA == 'Hello')] # get all data which have 'columnA' value are NOT 'Hello'
  ```

## Data Aggregation and Grouping ([reference](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html))
- For list of aggregation methods, see [here](https://sparkbyexamples.com/pandas/pandas-aggregate-functions-with-examples/)
  ```py
  # using `.agg()` method
  df.agg({'columnA': 'sum', 'columnB':'mean'}) # perform sum in 'columnA' and mean in 'columnB'

  # group by specific columns and create sum of values in each group
  df.groupby(by=["columnA"]).sum()
  ```




  
