import collections


def are_vaild_groups(stu_list, groups_list):
    # stu_list = [1, 2, 3, 4]
    # groups_list = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

    for group in groups_list:
        for i in group:
            if len(i) == len(stu_list):
                if collections.Counter(i) == collections.Counter(stu_list):
                    return True
            return False
