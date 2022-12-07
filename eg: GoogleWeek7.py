import re
import sys
import csv
import operator

lines =[
    "Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)",
    "Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)",
        "Jan 31 01:49:29 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)",
        "Jan 31 02:30:04 ubuntu.local ticky: ERROR Timeout while retrieving information (oren)",
        "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)",
        "Jan 31 05:45:30 ubuntu.local ticky: INFO Created ticket [#7115] (noel)"]

per_user = {}
errors = {}


for line in lines:
    #match = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
    #code, error_msg, user = match.group(1), match.group(2), match.group(3)

    user_search = re.search(r"\((.*)\)$", line)
    user = user_search.group(1)

    error_msg_search = re.search(r":+ (INFO|ERROR) ([\w' ]*)[\[[#0-9]*\]?]? ", line)
    error_msg = error_msg_search.group(2)

    code_search = re.search(r"ticky: ([\w+]*):?", line)
    code = code_search.group(1)

    if error_msg not in errors.keys():
        errors[error_msg] = 1
    else:
        errors[error_msg] += 1

    if user not in per_user.keys():
        per_user[user] = {}
        per_user[user]["INFO"] = 0
        per_user[user]["ERROR"] = 0

    if code == "INFO":
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]["INFO"] = 0
        else:
            per_user[user]["INFO"] += 1

    elif code == "ERROR":
        if user  not in per_user.keys():
            per_user[user] = {}
            per_user[user]["INFO"] = 0
        else:
            per_user[user]["ERROR"] += 1

per_user_sorted = sorted(per_user.items())
errors_sorted = sorted(errors.items(), key=lambda x:x[1],reverse=True)


listerbig = []
for key, value in per_user_sorted:
    lister = []
    lister.append(str(key))
    lister.append(str(value["INFO"]))
    lister.append(str(value["ERROR"]))
    listerbig.append(lister)


print(listerbig)

print(errors_sorted)

with open("per_user_report.csv","w") as file:
    please = csv.writer(file)
    please.writerow(['Username', 'INFO', 'ERROR'])
    please.writerows(listerbig)

with open("error_message.csv","w") as file:
    please = csv.writer(file)
    please.writerow(['ERROR', "COUNT"])
    please.writerows(errors_sorted)
