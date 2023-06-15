# Tidy Data

If your organization has a bunch of Excel or Google Spreadsheets strung together with fragile macros and you want to build the foundational skills necessary to modernize your stack, this is for you. 

Your data is most likely Messy. As Hadley Wickham says in his [pivotal paper](https://www.jstatsoft.org/article/view/v059i10/), "Tidy datasets are all alike but every messy dataset is messy in its own way." I don't know right now what your messy data will be like, and most likely all of your spreadsheets will be messy in a unique and challenging way. You have to learn to Tidy your data before you can do anything with it. Here are the important takeaways about Tidy Data:

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

### Exploring and Manipulating 
The **DataFrame** is your basic unit of work in the Python world when you're working with data. If the data frame is entirely new to you, maybe check out [this baby guide on some basic pandas operations to see how people usually interact with dataframes](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/dataframes.md). What comes below is a bit more advanced, but I'm confident you can learn the basic syntax of Pandas while learning the high level data tidying skills for your own data in the days to come.

You may already notice some weirdness in the dataframe, we can edit the cell to try to clean it up already: 
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/72c9bf1f-c897-4a14-9789-b6e0cb57dc90)
You can get rid of that `Unnamed: 0` column by adding the `index_col=0` argument to the `read_csv` method. Then reevaluate the cells that (i) store the df and (ii) display it, and it'll re-render the dataframe to look nicer. 

But it still won't be Tidy.

The fact that the data loaded with an `Unnamed` column is actually a hint. What would a good name be? Each column should be for a single variable, maybe this variable would be called `stomach_problem`. Then, the values of Stomach Ulcers, Lactose Intolerance, etc actually make sense as variable-values pairs. 

But what about the other columns? Let's look at the next column to the right: `Age 18-25`. If the column name is `Age 18-25`, what does the first value of `0.23` mean? We have to look all the way to the filename of the data set to learn that 0.23 is the __proportion of the population__ with this disorder. In fact, it shouldn't be so hidden!

The fact that you can't discern what a value in the table means just by looking at the column header is another dead giveaway that your data isn't tidy. Take a step back and look at the table. What information, in general, is stored in the table. Try to think about __a single row containing a single observation__. What would the "observation" be?

Answer: We have a column each for:
- Stomach Problem
- Age Range
- Proportion of Population

The "observation", if you read across the tidied up row, should read like: "a given stomach problem at a given age affects a certain proportion of the population". 

I've found it helpful to first map out an example of my input data (the picture above) and what my output data would look like. (These can later be turned into test cases!) At the very least, knowing what the desired dataframe's column names will be will help a lot to wrap your mind around carving out the next steps.

So whereas the first data point in our old, untidy dataframe reads: 
```
, age 18-25
stomach ulcers, 0.23 
```
instead, we want something like:
```
stomach_problem, age_range, proportion_of_population
"stomach ulcer", 18-25, 0.23
```
see how that fits together?

#### Tidying the Stomach Problems Table

The magic word for tidying this type of messy data is ✨ **melt** ✨ .

Melt is exactly the method you want here. It's usually a good first place to look when you have some messy data. After reading the documentation for [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html), I played around with the method and a few possible combinations of arguments, but eventually I just tried `df.melt()` to see what would happen without any arguments, that got me pretty far by itself. Give it a shot!


Then, with a little more playing wround, I've come up with this: 

```python 
tidy_stomach_problems_df = pd.read_csv('common-stomach-problems-population-proportion.tsv', sep='\t', index_col=0)\
    .melt(ignore_index=False)\
    .reset_index()\
    .rename(columns={"index":"stomach_ailment", "variable":"age_range", "value": "population_proportion"})\
    .replace({"age_range": {"Age ": ""}}, regex=True)
```

You should now have a tidy dataframe! It will be a lot bigger than the table you started out with, but that's the price of being explicit. And as according to the Zen of Python, explicit is better than implicit. 

![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/f167de0e-e87d-4a0c-a910-fcc2c28b4ba2)



### Column Headers Containing Values
Let's take a look at another fake data file in this repository. This one contains 4 measurements of weights for a given patient over a years time, it's called `'patient-weights-over-1-year.tsv'`

Once again, you can load it into your dataframe in pandas with
```python
weights_df = pd.read_csv('patient-weights-over-1-year.tsv', sep='\t', index_col=0)
```
and look at it by evaluating a cell with 
```python
weight_df
```
as the last line of the cell. 


Aside from this table containing information unrelated to the name of the file (age and height), what's wrong with this table? Well, once again: __When a table is tidy, each column represents a single variable.__ In our table, we have the columns `Weight-Q1`, `Weight-Q2`, `Weight-Q3`, and `Weight-Q4`, which confuse the concept of a variable name and a variable's value. Instead, we should have two columns: weight and quarter. Columns indicating Q1, Q2, Q3, and Q4 by their names are storing Values where they should be just Names. 
Our target dataframe will have the following column names:
- Name
- Age
- Height
- Weight
- Quarter
  
Or to put it more visually:
Our current table looks like: 
```
name, age, height, weight-q1, weight-q2, weight-q3, weight-q4
some name, 21,170, 100, 104, 95, 101
```
and what we want instead is:
```
name, age, height, weight, quarter
some name, 21, 170, 100, 1
```

(Wouldn't this make a nice test case?)
So how do we make that happen?

We're going to want to melt again! But this time there's some data (age and height) we want to hang onto that's already pretty Tidy. 
```python
weight_df\
    .melt(id_vars=["Age","Height"], ignore_index=False)`
```
We use the melt method again, this time providing Age and Height as "id_vars", and we'll end up with this: 
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/1c1b5dc9-28d7-4652-9645-4184ff02e3a8)
Just with doing a melt, we're already pretty far along! But we still need to: 
1. Reset the index column and give that new column the name `name`
1. Change the column names for `variable` and `value` to `quarter` and `weight_kg`
1. Change values like `Weight-Q1` and `Weight-Q2` to `1` and `2`

(1) and (2) are simple enough, and to do (3) I'll mention about the method: `replace`.

`replace` is nice because it can work on as many colums as you want, and column by column operations are what's desirable. This let's us think about our dataframe using Domain Modeling. We can actually start to think of **column names as domain object names**. But in order to get this column to be our well-behaved domain model, we need to change it from a string like "Weight-Q1" to an integer like `1`. A `quarter` is a decent domain object, right? Everyone will know it should be an integer between 1 and 4. We can use the replace method to change all the values in the `quarter` column which match the regular expression "Weight-Q" with the empty string "". So my final query for tidying up this table looks like this:
```python
weight_df = weight_df\
    .melt(id_vars=["Age","Height"], ignore_index=False)\
    .reset_index()\
    .rename(columns={"variable":"quarter", "value":"weight_kg", "index":"name"})\
    .replace({"quarter": {"Weight-Q": ""}}, regex=True)
```
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/93687a48-c790-4a9c-b9b7-ee32efc29e3a)

From here, I'm close to being able to bridge the gap between my tables. All that's left is a little mapping and merging. 

For instance, we have a table that contains people and their ages, and another table with ages and the likelihood of a stomach issues within the general population. I can create a new column for, `age_bracket` in the table for the people, and we'll have a column in common between the two. 
The somewhat arbitrarily created age brackets were: 18-25, 26-32, 33-40, 40-52, 53-65, 66-80, and 80-100. I need to write a function which will help add a column to my patient's info dataframe that corresponds to their age bracket.

For reasons of speed, the apply function is generally one to avoid, but with this size data set it's really not worth worrying about for now. Assigning people their age brackets can be accomplished with something like this:
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
    
weight_df = weight_df.assign(age_range=weights_df.filter(items=["Age"], axis=1).apply(lambda x: determine_age_range(x), axis=1))
weight_df
```

so now we have a tidy `weights_df` which is also enriched with an `age_range` column. This overlap enables us to merge (think SQL `Join`) with any tidy data containing the same column.
I.e.
```python
pd.DataFrame.merge(weight_df, tidy_stomach_problems_df, on=["age_range"], how="outer").dropna()
```

![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/ee96d662-aa4c-4556-88e9-ec4553924365)


From here, we could see at a glance that Gil Atkins has a 10% chance of having Stomach Ulcers given their [fake] prevalence in the general population. That's how an "Observation" works in Tidy data. 

### Conclusion

By tidying our data like this, it becomes almost mechanical to incorporate new data.

If we get more data about our patients, for example race, socioeconomic status, diet, and so on, as long as that data contains a `name` column with names that match the data above, we can add it in with our `merge` function. As long as all the tables are Tidy, they can be combined across any common columns.

Although Tidying increases the size of the data, the interoperability, ability to reason, and even execution speed (because of [vectorized/columnar data operations](https://plainenglish.io/blog/pandas-how-you-can-speed-up-50x-using-vectorized-operations)) will greatly outweight the disk space that you're using up. And besides that, the Data Science team will very likely want their data de-normalized for their machine learning algorithms.

Now that you have a high level understanding of Tidying your data, the last thing you need to know is how to organize your code. Let's talk about that very quickly:

[< Jupyter Notebooks](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/jupyter-notebook.md) | [Organizing your code >](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/ports-and-adapters.md)
