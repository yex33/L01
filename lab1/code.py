# xunzhou version
def are_valid_groups(student_numbers, groups):
    for number in student_numbers:
        if number not in (member for group in groups for member in group):
            return False
    return True

# kehao version
def are_valid_groups(snList, groupList):
    counter = 0
    for i in snList:
        for j in range(0, len(groupList)):
            for k in range(0, len(groupList[j])):
                if i == groupList[j][k]:
                    counter += 1
    if counter >= len(snList):
        return True
    else:
        return False
