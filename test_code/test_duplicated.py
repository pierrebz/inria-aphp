import pandas as pd
from collections import Counter

# density by state
wgt = {'nsw': 0.33780252244063175,
       'vic': 0.24497216225428928,
       'qld': 0.19054652880354506,
       'wa': 0.09294398363822293,
       'sa': 0.07874105215316442,
       'tas': 0.027496875355073287,
       'act': 0.01829337575275537,
       'nt': 0.009203499602317918}

# dataframe for the test
df_test = pd.DataFrame([[411955, 'madeleine', 'nsw', 'nsw', 'nsw', 'nsw'],
                        [411955, 'william', 'nsw', 'vic', None, 'nsw']], columns=['patient_id',
                                                                                  'given_name',
                                                                                  'state_cln',
                                                                                  'postcode_cln',
                                                                                  'area_cln',
                                                                                  'suburb_cln'])

def detect_duplicates(df):
    """
    This function detect duplicated patient

    p:
        - wgt: density by state
    """

    # list of duplacate index
    idx_drop = []

    # list of unique patient_id
    unique = df.patient_id.unique()

    # list of patient_ids having more than 1 occurence
    dpt_patient_id = []
    for id_pat in unique:
        if len(df[df.patient_id == id_pat]) > 1:
            dpt_patient_id.append(id_pat)

    # for each patient id duplicated
    for row in dpt_patient_id:
        check_right = df[df.patient_id == row]

        # dictionnary for idx et state max.
        dict_max_idx = {}
        dict_max_state = {}

        for row in range(len(check_right)):
            # list of states for each row
            list_state = ' '.join([i for i
                                   in check_right.iloc[row]['state_cln':
                                                            'suburb_cln'].values.tolist() if i]).split(' ')

            # occurance for each state in the list
            count = dict(Counter(list_state))

            # add weight to count.
            for cnt in count.keys():
                count[cnt] = count[cnt] * wgt[cnt]

            # find index of max ans the state.
            dict_max_idx[check_right.index[row]] = max(count, key=count.get)
            dict_max_state[check_right.index[row]] = max(count.values())

        # add the index of row to drop
        idx_drop.append(min(dict_max_state, key=dict_max_state.get))

    # drop duplicated rows
    df.drop(idx_drop, inplace=True)

    return df


def test_detect_duplicates():
    assert detect_duplicates(df_test).given_name.values == 'madeleine'