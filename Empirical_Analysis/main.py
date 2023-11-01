from Analysis import Analysis
from Sorting import bubble_sort, quick_sort
from Searching import linear_search, binary_search

# Analysis().analyse(
#     bubble_sort, 
#     csvSave=True
# )

# Analysis().analyse(
#     quick_sort,
#     lenArray=[100000, 300000, 700000, 1000000, 2000000, 3000000, 5000000],
#     csvSave=True
# )

Analysis().analyse(
    linear_search, 
    lenArray=[500000, 700000, 1000000, 2000000, 3000000, 4000000, 5000000, 7000000],
    csvSave=True
)

Analysis().analyse(
    binary_search, 
    lenArray=[500000, 700000, 1000000, 2000000, 3000000, 4000000, 5000000, 7000000],
    csvSave=True
)