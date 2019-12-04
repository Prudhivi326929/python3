def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

tempa = [4.2, 23.2, 6.9]
stu_grades = {"Marry":9.2, "Sim":8.8, "john":7.5}

print(mean(tempa))
print(mean(stu_grades))