from subprocess import check_output
import sys

get_result = check_output("wmic netlogin get name, fullname, lastlogon", shell=True, stderr=False)
#1print(get_result)
clean_result = str(get_result).lstrip("b'").rstrip("'").replace("\\r\\r\\n", "\n").replace('\n\n', '\n').split('\n')[2:-1]
for items in clean_result:
    print(items.lstrip().rstrip())
