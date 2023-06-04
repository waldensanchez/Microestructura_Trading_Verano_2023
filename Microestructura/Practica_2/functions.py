
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
def f_compare_ts(ts_list_o, ts_list_d):
    dictionary = {'first_o':ts_list_o[0], 'last_o' : ts_list_o[-1],'qty_o' : len(ts_list_o),
                  'first_d':ts_list_d[0], 'last_d' : ts_list_d[-1],'qty_d' : len(ts_list_d),
                  'exact_match':len(set(ts_list_o) & set(ts_list_d))} 
    return dictionary