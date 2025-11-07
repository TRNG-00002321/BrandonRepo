import pandas as pd

    # mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

    # pandas series
# a = [1, 7 , 2]
# myvar = pd.Series(a)
# print(myvar)
# #access it by index
# print(myvar[0])


    # create your own level
# a = [1,7,2]
# myvar = pd.Series(a, index=["x","y","z"]) #here instead of level 0-2, its x-z
# print(myvar)


    # in series, we can use key value pairs
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar=pd.Series(calories)
# print(myvar)

    # data frames
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50,40,45]
# }
# # load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df)


    # with the index argument you can name your own indexes
    #NAMED INDEXES
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50,40,45]
# }
#
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(df)

#                                    READING

    #read csv

# df = pd.read_csv('data.csv')
# print(df) #to_string() displays entire file
# new_df = df.dropna()
# print(new_df)


    #max row
#increase max row

    #read json
# df = pd.read_json('data.json')
# print(df.to_string())


#remove nulls
# df = pd.read_json('data.json')
# df.dropna(inplace = True)
# print(df.to_string())

#return new data frame with no empty cells
df = pd.read_json('data.json')
new_df = df.dropna()
print(new_df.to_string())

                                    # VIEWING

