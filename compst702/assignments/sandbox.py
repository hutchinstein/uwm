import re

myre = "[^a-z1-5]"
if re.search(myre, "abc1234"):
    print("True")
else:
    print("False")