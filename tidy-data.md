# Tidy Data

If your organization has a bunch of Excel or Google Spreadsheets strung together with fragile macros and you want to build the foundational skills necessary to modernize your stack, this is for you. 

Your data is most likely Messy. As Hadley Wickham says in his [pivotal paper](https://www.jstatsoft.org/article/view/v059i10/), "Tidy datasets are all alike but every messy dataset is messy in its own way." I don't know right now what your messy data will be like, and most likely all of your spreadsheets will be messy in a unique and challenging way. You have to learn to Tidy your data before you can do anything with it. Here's the important takeaways about Tidy Data, but you'll have to keep looking these things up and working to understand them time and again:

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

For this section I've generated some fake data that you can import into a Jupyter Notebook to play around with. You can either clone this repository or just copy+paste the raw relevant files, just make sure you copy all the important whitespace when you do that.
In general, to do this kind of work, you're going to become very familiar with the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html). Your best friends will be methods like: 
- [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)
- [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html)
- [explode](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html)
- [filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html)
- [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

Let's jump over to our Notebook to start playing. 
### Importing Data
Importing data is pretty easy, you'll just need to run the following the import and view your first pandas DataFrame. Let's load the fake data table representing the proportion of the general population who has a given stomach problem, divided up by age:

```python
import pandas as pd
stomach_problems = pd.read_csv('common-stomach-problems-population-proportion.tsv', sep='\t')
stomach_problems
```
executing a cell with just a variable like `stomach_problems` at the end will result in the dataframe being displayed inline on the notebook.

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

(1) and (2) are simple enough, but to do (3) I'll introduce a new method: `replace`.

After a quick internet search, I find that I can chain the `replace` method with options to update a single column using a regular expression, and so my final query for tidying up this table looks like this:
```python
new_df = df\
    .melt(id_vars=["Age","Height"], ignore_index=False)\
    .reset_index()\
    .rename(columns={"variable":"quarter", "value":"weight_kg", "index":"name"})\
    .replace({"quarter": {"Weight-Q": ""}}, regex=True)
```
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/93687a48-c790-4a9c-b9b7-ee32efc29e3a)

From here, I can finally have a single cohesive conversation between my datasets with a little mapping and joining. 
For instance, we have a table that contains people and their ages, and another table with ages and the likelihood of a stomach issues within the general population. I can create a new column for, `age_bracket` in the table for the people, and we'll have a column in common between the two. 
The somewhat arbitrarily created age brackets were: 18-25, 26-32, 33-40, 40-52, 53-65, 66-80, and 80-100. I need to write a function which will add a column to my patient's info dataframe that corresponds to their age bracket.

The apply function is generally one to avoid, but with this size data set it's really not worth worrying about for now. Assigning people their age brackets can be accomplished with something like this:
```python
def determine_age_range(age):
    age = int(age)
    if 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 32:
        return "26-32"
    elif 33 <= age <= 40:
        return "33-40"
    elif 41 <= age <= 52:
        return "41-52"
    elif 53 <= age <= 65:
        return "53-65"
    elif 66 <= age <= 80:
        return "66-80"
    elif 80 <= age <= 100:
        return "80-100"
    
weights["age_range"] = weights.filter(items=["Age"], axis=1).apply(lambda x: determine_age_range(x), axis=1)
```

and this enables us to use the merge method to merge our datasets and start to do analysis:
```python
pd.DataFrame.merge(weights, common_stomach_problems, on=["age_range"], how="outer").dropna()
```

![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/ee96d662-aa4c-4556-88e9-ec4553924365)

From here, we could see at a glance that Gil Atkins has a 10% chance of having Stomach Ulcers given their [fake] prevalence in the general population. By tidying our data like this, it becomes almost mechanical to then incorporate data that would give us better estimates of likelihoods for various diseases/disorders, for example if we also had statistics about those issues as they intersect race, socioeconomic status, diet, and so on. Although the size of the data increases, the interoperability is hugely beneficial. And anyway, the Data Science team will problly want their data de-normalized for their machine learning algorithms.

One of the nice things about the tidy format is that I can utilize vectorized operations in the Pandas library and [speed up execution time dramatically](https://plainenglish.io/blog/pandas-how-you-can-speed-up-50x-using-vectorized-operations), when compared to using iteration.
Let's say I want to find people who have a lot of variance in their weight throughout the year. In its original format, I'd probably need to write code that looks like:
```python
for row in df:
    var = compute_variance(row, relevant_column_names=["Weight-Q1", "Weight-Q2", "Weight-Q3", "Weight-Q4"])
    ...
```
and with our tidy data I can instead:


