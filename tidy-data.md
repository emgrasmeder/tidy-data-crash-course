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
Importing data is pretty easy, you'll just need to run the following the import and view your first pandas DataFrame. Let's load the fake data table representing the proportion of the general population who has a given stomach problem, divided up by age:

```python
import pandas as pd
df = pd.read_csv('common-stomach-problems-population-proportion.tsv', sep='\t')
df
```

The **DataFrame** is your basic unit of work in the Python world when you're working with data.
You may already notice some weirdness in the dataframe, we can edit the cell to try to clean it up already: 
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/72c9bf1f-c897-4a14-9789-b6e0cb57dc90)
You can get rid of that `Unnamed` column by adding the `index_col=0` argument to the `read_csv` method. Then reevaluate the cell to store the df and display it, and it'll look nicer. But it won't look Tidy.

The fact that the data loaded with an `Unnamed` column is actually a hint. What would a good name be? Each column should be for a single variable, maybe this variable would be called stomach_problem. Then, the values of Stomach Ulcers, Lactose Intolerance, etc actually make sense as variable-values pairs. But what about the other columns? Let's look at the next column to the right: `Age 18-25`. If the column name is `Age 18-25`, what does the first value of `0.23` mean? We have to look all the way to the filename of the data set to learn that 0.23 is the __proportion of the population__ with this disorder. It shouldn't be so hidden!

The fact that you can't discern what a value in the table means just by looking at the column header is another dead giveaway that your data isn't tidy. What we want is to have a column each for:
- Stomach Problem
- Age Range
- Proportion of Population

I've found it helpful to first map out an example of my input data and what my output data would look like. (These can later be turned into test cases!) At the very least, knowing what the desired dataframe's column names will be will help a lot to wrap your mind around carving out the next steps.

With a little playing wround, I've come up with this: 

```python 
melted_df = df
    .melt(ignore_index=False)
    .reset_index()
    .rename(columns={"index":"stomach_ailment", "variable":"age_range", "value": "population_proportion"})
```

Melt is exactly the method you want here. After reading the documentation for [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html), I played around with the method and a few possible combinations of arguments but eventually I just tried `df.melt()` to see what would happen without any arguments, that got me pretty far by itself. Give it a shot!

You should now have a tidy dataframe! It will be a lot bigger than the table you started out with, but that's the price of being explicit. And as according to the Zen of Python, explicit is better than implicit. 

![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/6cf14554-c29e-458b-afd2-f73fe6d28653)


### Column Headers are Values, not Variable Names
Let's take a look at another fake data file in this repository. This one contains 4 measurements of weights for a given patient over a years time, it's called `'patient-weights-over-1-year.tsv'`

Once again, you can load it into your dataframe in pandas with
```python
df = pd.read_csv('patient-weights-over-1-year.tsv', sep='\t', index_col=0)
```
and look at it by evaluating a cell with 
```python
df
```
as the last line of the cell. 


Aside from this table containing information unrelated to the name of the file (age and height), what's wrong with this table? Well, once again: When a table is tidy, each column represents a single variable. In our table, we have the columns `Weight-Q1`, `Weight-Q2`, `Weight-Q3`, and `Weight-Q4`, which confuse the concept of a variable name and a variable's value. Instead, we should have two columns: weight and quarter. Columns indicating Q1, Q2, Q3, and Q4 by their names are storing Values where they should be just Names. 
Our target dataframe will have the following column names:
Name, Age, Height, Weight, Quarter. How do we make that happen?

We're going to want to melt again! But this time there's some data we want to hang onto that's already pretty Tidy. 
```python
df
    .melt(id_vars=["Age","Height"], ignore_index=False)`
```
We use the melt method again, this time providing Age and Height as "id_vars", and we'll end up with this: 
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/1c1b5dc9-28d7-4652-9645-4184ff02e3a8)
Just with doing a melt, we're already pretty far along! But we still need to: 
1. Reset the index column and give that new column the name `name`
1. Change the column names for `variable` and `value` to `quarter` and `weight_kg`
1. Change values like `Weight-Q1` and `Weight-Q2` to `1` and and `2`

(1) and (2) are simple enough, but to do (3) I'll introduce a new method: `replace`
After a quick internet search, I find that I can chain the `replace` method with options to update a single column using a regular expression, and so my final query for tidying up this table looks like this:
```python
new_df = df
    .melt(id_vars=["Age","Height"], ignore_index=False)
    .reset_index()
    .rename(columns={"variable":"quarter", "value":"weight_kg", "index":"name"})
    .replace({"quarter": {"Weight-Q": ""}}, regex=True)
```
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/93687a48-c790-4a9c-b9b7-ee32efc29e3a)



