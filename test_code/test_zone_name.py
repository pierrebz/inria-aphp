import pandas as pd

# import the dictionary
dict_zone = {'02': 'nsw act', '03': 'vic tas', '07': 'qld', '08': 'sa nt wa'}

# dataframe for the test
df_test = pd.DataFrame(['02'], columns= ['area'])


def zone_name(df, phone_dict):
    """
    The function return the states fo each area zone

    p:
        - df : the dataframe
        - phone_dict : the corresponding states based on area code
    """

    if df['area'] in phone_dict.keys():
        return phone_dict[df['area']]
    else:
        return None


def test_zone_name():
    assert df_test.apply(lambda x: zone_name(x, dict_zone), axis= 1).values == 'nsw act'