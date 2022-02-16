import json
import pandas as pd
import numpy as np

# Arr_csv = pd.read_csv("../../../media/image_database.csv", header=None, keep_default_na=False)
# Arr = Arr_csv.to_numpy()
#
# arr_image, arr_categories = np.split(Arr, [2], axis=1)
#
# delimiter = ','
#
# arr_str_categories = [delimiter.join(categories) for categories in arr_categories]
#
# arr_str_categories = np.reshape(np.array([delimiter.join(categories) for categories in arr_categories]), (-1,1))
#
# arr_image_url, arr_amount = np.split(arr_image, 2, axis=1)
# M = np.hstack((arr_image, arr_str_categories))
# print(M)
# # SL = []
# # for i in M:
# #     slov = {"Image URL": '{}'.format(i[0]),
# #             "Amount of show": '{}'.format(i[1]),
# #             "Categories": '{}'.format(i[2])
# #             }
# #     SL.append(slov)
# fields = [{"Image URL": '{}'.format(i[0]), "Amount of show": '{}'.format(i[1]), "Categories": '{}'.format(i[2])} for i in M]
# spisok = [
#          {"model": "MODEL",
#           "pk": i+1,
#           "fields": fields[i]
#           } for i in range(len(fields)) ]
#
# with open('file_1.json', 'w') as file:
#         json.dump(spisok, file, indent=4)





# with open("file_1.json", "w") as file:
#      json.dump(dict(SL), file)

# arr_image, arr_str_categories = np.split(M, [2], axis=1)
# arr_categories = []
# delimiter = ','
# for str_categories in arr_str_categories:
#     categories = str_categories[0].split(sep=delimiter)
#     arr_categories.append(categories)
#
# M = np.hstack((arr_image, arr_categories))

