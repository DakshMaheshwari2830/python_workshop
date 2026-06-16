def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(35))
print(sum_of_numbers(100))


def generate_groups(team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Daksh','ABC','XYZ','z','k0','hj')


def string_reverse(str1):
    
    rstr1=''
    index=len(str1)
    while index>0:
        rstr1+=str1[index-1]
        index=index-1
    return rstr1
print(string_reverse("Daksh Maheshwari"))