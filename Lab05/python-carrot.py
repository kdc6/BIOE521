
# "^" - matches the beginning of a line or string

import re

string1 = "Hello World"
if re.search(r"^He", string1):
    print string1, "starts with the characters 'He'"