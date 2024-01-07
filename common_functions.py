df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])), 
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
# select a subset of df columns
df.filter(items=['one', 'three'])
