# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases 
# by 2 percent per year and moreover 50 new inhabitants per year come to 
# live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
# It will need 3 entire years.
# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10

from math import floor
def nb_year(p0, percent, aug, p):
    i = 1
    mult = 1 + percent / 100.0
    prev = p0
    while (prev < p):
        ne = floor((prev * mult + aug))
        prev = ne
        i += 1
    return (i - 1)
    
def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        p0 += p0*percent/100 + aug
        i += 1
    return i
    
def nb_year(y,e,a,r,s=0):
    while y<r:y+=y*e*.01+a;s+=1
    return s
    
def nb_year(p0, percent, aug, p):
  y = 0
  while p0 < p: p0, y = p0 * (1 + percent / 100.0) + aug, y + 1
  return y
  
  
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
    
def nb_year(p0, percent, aug, p):
#     p0=初始人口，percent=每年增长速度，aug=每年移民数，p>=
    # my code
    final_people = 0
    num = 0
    while final_people < p:
        final_people = int(p0 + p0*(percent*0.01) + aug)
        num = num +1
        p0 = final_people
    return num
        
