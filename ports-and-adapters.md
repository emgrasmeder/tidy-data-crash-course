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

## Mapping Ports and Adapters to the Code We Just Worked With
### Port Code
Your ports are the interface between the outside world and your app. They could be saving data to a database or pulling it from an external API, or the filesystem in our case. Port code tends to look like:

`some_df = pd.read_csv("some filename.tsv")`

and

`my_new_tidy_df.to_csv("some filename.csv")`
### Adapter Code
Adapter code doesn't rely on external systems, but the code doesn't conform to our internally ubiquitious language yet. The data doesn't feel like our well domain modeled code yet. The point of the adapter layer is to make the code tidy, to make the column names conform to our internal code conventions, to coerce data types into what we expect. Adapter layer code looks like:

`tidy_df = some_df.melt().rename(columns={"Old COLNAME": "new_column_name"})`

and

`pd.to_datetime(tidy_df)`

### Core Code
Core code is code that can make a lot of assumptions about the meaning of the code. Perhaps you can assume that any column name with the `_time` suffix will be a unix timestamp, or with a `_grams` suffix will be a float with 2 decimal places, or that columns dealing with money will be integers. This isn't an assumption you can make when you're dealing with external APIs, producers upstream, other teams, etc. 

But your adapters have insulated you from the chaos of the outside world, and now you can think about your data as you do about your business. Your columns are predictable, the data is tidy, and everything is interoperable with everything else. The core is the most important part of your business. You can write tests and refactor rapidly because everything is calm here. Core code often looks like:

`my_new_tidy_df = tidy_df.merge(some_other_tidy_df, how="outer", on=["column_in_both_dataframes"])`

and

`my_new_tidy_df.assign(tomorrow=my_new_tidy_df.date + pd.DateOffset(1))`

## Wrapping Up

You can literally just put your code in directories called ports, adapters, and core. Then you can tie it all together with a single `main` file that coordinates everything, or look at tools like Dagster, Airflow, Luigi, etc, but you probably don't need them for now. 

This was intended to be a super high level overview of how you'll organize your code and some of the common ways you'll work when phasing out spreadsheet based workflows. If you have questions, please raise an issue in the repository and I'll be happy to answer/adjust! I hope you feel like you know a bit more how to move forward!

[< Tidy Data](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/tidy-data.md) |

