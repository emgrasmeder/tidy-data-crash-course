# Ports and Adapters / Hexagonal / Onion Architecture 

My recommendation for how to keep your code organized is to follow the Ports and Adapters pattern, which I'd map out quickly like this:

```
┌─────────────────────────────────────────────────────────────────┐
│port layer                                                       |
|         Code that knows about the outside world                 │
│         Causes side effects                                     │
│         Depends on state external to the app                    │
│         ┌──────────────────────────────────────────────┐        │
│         │adapter layer                                 │        │
│         │    Only exists to convert between port       |        |
|         |    and core                                  │        │
│         │        ┌────────────────────────────────┐    │        │
│         │        │ core                           │    │        │
│         │        │     Pure Functions             │    │        │
│         │        │     Domain Code                │    │        │
│         │        │     No Side Effects            │    │        │
│         │        └────────────────────────────────┘    │        │
│         └──────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

### Mapping Ports and Adapters to the Code We Just Worked With
#### Port Code
`some_df = pd.read_csv("some filename.tsv")`
#### Adapter Code
`tidy_df = some_df.melt().rename(columns={"old column name": "new column name"})`
#### Core Code
`my_new_df_which_is_still_tidy = tidy_df.merge(some_other_tidy_df, how="outer", on=["column_in_both_dataframes"])`
#### Port Code Again
`my_new_df_which_is_still_tidy.to_csv("some filename.csv")`
