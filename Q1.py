year=int(input())
def leap(yrs):
    leap=True
    noleap=False
    if(yrs%4 == 0 and (yrs%100 !=0 or yrs%400==0)):
        return leap
    else:
        return noleap
print(leap(year))