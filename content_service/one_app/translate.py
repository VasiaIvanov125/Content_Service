import pandas as pd
import numpy as np


def translate_csv(file='one_app/media/image_database.csv'):
    '''
    :param file:
    :return:
    '''

    Arr_csv = pd.read_csv(file, header=None, keep_default_na=False)
    Arr = Arr_csv.to_numpy()

    arr_image, arr_categories = np.split(Arr, [2], axis=1)

    delimiter = ','
    arr_str_categories = np.reshape(np.array([delimiter.join(categories) for categories in arr_categories]), (-1, 1))

    return np.hstack((arr_image, arr_str_categories))


def translate_text(Arr):
    '''
    :param file:
    :return:
    '''
    arr_image, arr_str_categories = np.split(Arr, [2], axis=1)

    arr_categories = []
    delimiter = ','
    for str_categories in arr_str_categories:
        categories = str_categories.split(sep=delimiter)
        arr_categories.append(categories)

    arr_categories = np.reshape(np.array(arr_categories), (-1, 1))

    return np.hstack((arr_image, arr_categories))