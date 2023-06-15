The most basic way people interact with dataframes, I'd guess, is like this:

# make a dataframe
`df = pd.DataFrame({"first column":[1,2,3,4,5],"second column":[11,22,33,44,55]})`
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/904ceb07-c1cf-4324-bc65-af13a0a07fd4)

# select some data in the dataframe
`df["first column"]`
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/51ec0946-53f7-4274-af85-d4ea19888435)

# add some data together
`df["first column"] + df["second column"]`
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/4f80e8fa-d649-4425-b6c2-0c8d73abc484)

# assign data to a new column
`df["some new column"] = df["first column"] + df["second column"] + 999`
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/51a2ab0a-9fe5-49c4-bbb9-60fe8af779d2)

Anything beyond that, I generally advise people to do an image search for "pandas cheat sheet" and look it over every so often. Most functionality that you'd want with a pandas dataframe is baked into the object, you just have to know how to look for it. 

![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/4d1c92f3-0431-4dc5-9215-179dc20e0e92)


If you want to see some more in depth examples of how DataFrames get used in production, I would point you to the [Continuous Delivery for Machine Learning workshop that I created while at ThoughtWorks](https://github.com/ThoughtWorksInc/cd4ml-workshop/tree/master/jupyter_notebooks), which walks you thought the process of feature engineering and exploratory data analysis making heavy use of dataframes.
