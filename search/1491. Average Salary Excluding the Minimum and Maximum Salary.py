salary = [4000,3000,1000,2000]

if salary:
    salary.pop(salary.index(min(salary)))
    salary.pop(salary.index(max(salary)))

    return(sum(salary)/len(salary))