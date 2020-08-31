import csv
import pandas as pd

# import the csv contain the dictionary of corresponding states
csvfile = csv.reader(open("./dict_test/test_dict_state.csv"))
dict_state = dict(csvfile)

# dataframe for the test
df_test = pd.DataFrame(['qod'], columns= ['state'])

def state_data_cleaning(df, state_dict):
    """
    This function return the right state's name.

    p:
        df : the dataframe
        state_dict : the corresponding state based on sequences comparison
    """
    # edit dataframe columns state
    if df['state'] is None:
        return None
    else:
        return state_dict[df['state']]


def test_state_data_cleaning():
    assert df_test.apply(lambda x: state_data_cleaning(x, dict_state), axis= 1).values == 'qld'


