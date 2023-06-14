# Tidy Data

Note: For a more in depth discussion of Tidy Data, you should read the [original paper by Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10/)!
Here are the important takeaways from the paper:

In data that is "tidy": 
- Each row reflects a single observation.
- Each column is reserved for a single variable. 

Most commonly in "untidy" data:
- Column headers are values, not variable names.
- Multiple variables are stored in one column.
- Variables are stored in both rows and columns.
- Multiple types of observational units are stored in the same table.
- A single observational unit is stored in multiple tables.

## Fixing Untidy Data so that it is Tidy

For this section I've generated some fake data that you can import into a Jupyter Notebook to play around with. 
To do this kind of work, you're going to become very familiar with the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html). Your best friends will be methods like: 
- [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)
- [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html)
- [explode](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html)
- [filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html)

Let's jump over to our Notebook to start playing. 
Importing data is pretty easy, you'll just need to run the following the import and view your first pandas DataFrame.

```python
import pandas as pd
df = pd.read_csv('common-stomach-problems-population-proportion.tsv', sep='\t')
df
```

The **DataFrame** is your basic unit of work in the Python world when you're working with data.
You may already notice some weirdness in the dataframe, we can edit the cell to try to clean it up already: 
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/72c9bf1f-c897-4a14-9789-b6e0cb57dc90)
You can get rid of that `Unnamed` column by adding the `index_col=0` argument to the `read_csv` method. Then reevaluate the cell to store the df and display it, and it'll look nicer. But it won't look Tidy.

The fact that the data loaded with an `Unnamed` column is actually a hint. What would a good name be? Each column should be for a single variable, maybe this variable would be called stomach_problem. Then, the values of Stomach Ulcers, Lactose Intolerance, etc actually make sense as variable-values pairs. But what about the other columns? Let's look at the next column to the right: `Age 18-25`. If the column name is `Age 18-25`, what does the first value of `0.23` mean? We have to look all the way to the filename of the data set to learn that 0.23 is the __proportion of the population__ with this disorder.


### Column Headers are Values, not Variable Names
