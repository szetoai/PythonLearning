import pandas as pd

# creating dataframes based on list and dict
profiles = [
    ["Kelly", "White Bread", 28],
    ["Lauren", "Burrito", 19],
    ["Joseph", "Porridge", 103]
]
favorites = [
    {"name":"Kelly","fruit":"kiwi","vegetable":"one big leaf","sport":"running"},
    {"name":"Lauren","fruit":"lime","vegetable":"tomato","sport":"weight lifting"},
    {"name":"Joseph","fruit":"prunes","vegetable":"spinach","sport":"pilates"}
]
list_df = pd.DataFrame(profiles, columns=["Names","Favorite Food", "Age"], index=[1,2,3])
dict_df = pd.DataFrame(favorites, index=[1,2,3])
print(f"{list_df}\n{dict_df}")

# modifying dataframes
home_states = ["MA", "NY", "AZ"]
list_df["Home States"] = home_states
print(list_df)
# editing column values
age_min = []
for x in list_df["Age"]:
    age_min.append(x/2 + 7)
    print("hi")
list_df["Min Age Range"] = age_min
list_df["Min Age Range"] = round(list_df["Min Age Range"], 1)
print(list_df)
# changing data types
print(list_df["Min Age Range"].dtype)
list_df["Min Age Range"] = list_df["Min Age Range"].astype(int)
print(list_df)
# indexing
print(list_df[list_df["Min Age Range"] > 18])