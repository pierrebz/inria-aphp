import pandas as pd

# import the dictionary
dict_suburb = {'aarons pass': ['nsw'],
 'abba river': ['wa'],
 'abbey': ['wa'],
 'abbeyard': ['vic'],
 'abbeywood': ['qld'],
 'abbotsbury': ['nsw'],
 'abbotsford': ['nsw', 'vic', 'qld'],
 'abbotsham': ['tas'],
 'abels bay': ['tas'],
 'abercorn': ['qld'],
 'abercrombie': ['nsw'],
 'abercrombie river': ['nsw'],
 'aberdare': ['nsw'],
 'aberdeen': ['nsw', 'tas'],
 'aberfeldie': ['vic'],
 'aberfeldy': ['vic'],
 'aberfoyle': ['nsw'],
 'aberfoyle park': ['sa']}

# dataframe for the test
df_test = pd.DataFrame(['abercorn'], columns= ['suburb'])


def match_suburb(df, suburb_dict):
    """
    This function return the states fo each suburb

    p:
        - df : the dataframe
        - suburb_dict : the corresponding states based on suburb name
    """
    if df['suburb'] is None:
        return None
    elif df['suburb'] in suburb_dict.keys():
        return ' '.join(suburb_dict[df['suburb']])
    else:
        return None


def test_match_suburb():
    assert df_test.apply(lambda x: match_suburb(x, dict_suburb), axis= 1).values == 'qld'