
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
