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

I've generated a couple fake data sets to play around with
### Column Headers are Values, not Variable Names
