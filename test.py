import datetime

a = '1-1.5万/月'
if '万/月' in a:
    a = a.replace('万/月', '').split('-')
print(a)


