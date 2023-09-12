
def common_elements(set_1, set_2):
    common = (i for i in set_1 if i in set_2)
    return common





set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))