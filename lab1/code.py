def are_valid_groups(student_numbers, groups):
    for number in student_numbers:
        if number not in (member for group in groups for member in group):
            return False
    return True
