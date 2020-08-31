import pandas as pd

# import the dictionary
dict_postcode = {'nsw': [1000, 1999, 2000, 2599, 2619, 2899, 2921, 2999],
 'act': [200, 299, 2600, 2618, 2900, 2920],
 'vic': [3000, 3999, 8000, 8999],
 'qld': [4000, 4999, 9000, 9999],
 'sa': [5000, 5799, 5800, 5999],
 'wa': [6000, 6797, 6800, 6999],
 'tas': [7000, 7799, 7800, 7999],
 'nt': [800, 899, 900, 999]}

# dataframe for the test
df_test = pd.DataFrame(['2600'], columns= ['postcode'])


def match_postcode(df, post_dict):
    """
    This function return the state for given postcode.

    p:
        df : the dataframe
        post_dict : the corresponding state based on postcode
    """

    if df['postcode'] is None:
        return None
    else:
        for ps_state in post_dict.keys():
            groups = list(zip(*[iter(post_dict[ps_state])] * 2))
            if any(start <= int(df['postcode']) <= end for start, end in groups):
                return ps_state


def test_match_postcode():
    assert df_test.apply(lambda x: match_postcode(x, dict_postcode), axis= 1).values == 'act'


