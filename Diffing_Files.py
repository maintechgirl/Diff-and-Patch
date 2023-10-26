### Diffing Files

# cat rearrange1.py

#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])


# cat rearrange2.py

#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])


# diff rearrange1.py rearrange2.py

"""
6c6
<     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
---
>     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
"""

"""
diff - When we call the diff commande we get only the lines are different between 2 files.
<    - The less than symbol tells us that the first line was removed from the first file,
>    - and the greater than symbol tells us that the second line was added to the second file.

"""

# diff validations1.py validations2.py

"""
5c5,6
<     assert (type(username) === str), "username must be a string"
---
>     if type(username) !=str:
>         raise TypeError("username must be a string")
11a13,15
>         return False
>     # Username cant begin with a number
>     if username[0].isnumeric():
"""

"""
We can see that diff splits the changes in two separate sections.
5c5,6    - The section that starts with 5c5,6 shows a line in the first file that was replaced by two different lines in the second file.
The number at the beginning of this section indicates the line number in the first and second files.
c        - The c in between the numbers means that a line was changed.
11a13,15 - The section that starts with 11a13,15 shows three lines that are new in the second file. 
"""

# diff -u validations1.py validations2.py

"""
--- validations1.py     2020-01-05 07:03:46.999900910 -0800
+++ validations2.py     2020-01-05 07:03:46.999900910 -0800
@@ -2,7 +2,8 @@

def validate_user(username, minlen):
-   assert (type(username) == str), "username must be a string"
+   if type(username) != str:
+       raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must bbe at least 1")

@@ -10,5 +11,8 @@
        return False
    if not username.isalnum():
        return False
+    # Username cant begin with a number
+   if username[0].isnumeric():
+       return False
    return True
"""

"""
-u       - It shows the change lines together with some context, using the minus sign to mark lines that were removed,
and the plus sign to mark lines that were added.

We can see that the new file actually has a completely new if block that's part ofa chain of conditionals that looks very similar,
and that's why with the diff output that we saw before, it was a little confusing which lines had been added. 
"""



"""
wdiff     - highlights the words that have changed in a file instead of working line by line like diff does.
meld, KDiff3, or vimdiff  -  graphical tools that display files side by side and highlight the differences by using color"""