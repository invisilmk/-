# import time as t
# start_time = t.time()
# for a in range(0,1001):
#     for b in range(0,1001-a):
#         for c in range(0,1001-a-b):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print(f'a{a},b{b},c{c}')
# end_time = t.time()
# print(f'{end_time-start_time}')
t=1000*1000*1000*2
t=n*n*n*2
t(n)=n^3*2
t(n)=n^3*10
t(n)=n^3
import time as t
start_time = t.time()
for a in range(0,1001):
    for b in range(0,1001-a):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print(f'a{a},b{b},c{c}')
end_time = t.time()
print(f'{end_time-start_time}')