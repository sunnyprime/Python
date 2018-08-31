# import re
#
# patterns = ['term1','term2']
#
# text = 'This is a string with term1,not not the other!'
#
# for pattern in patterns:
#     print("I'm searching for: "+pattern)
#
#     if re.search(pattern,text):
#         print("MATCH!")
#     else:
#         print("NO MATCH")

# ===============================

# import re
#
# split_term = '@'
#
# email = 'user@gmail.com'
#
# print(re.split(split_term,email))

# ===================================
#
# import re
#
# print(re.findall('match','test phrase match in middle'))
# ======================================================

import re

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sdddd'

test_patterns =['sd*']

multi_re_find(test_patterns,test_phrase)
