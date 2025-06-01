# a ='abaca'
# nsk = []

# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         nsk.append(a[i:j])

# print(nsk)

# def weird():
#     t = int(input())
#     for i in range(t):
#         w,x,y,z = map(int, input().split())
#         if w == (x+y) or w == (z+y) or w == (x+z) or w == (x+y+z):
#             print('YES')
#         elif w< min(x,y,z):
#             print('NO')
#         elif w == x or w == y or w == z:
#             print('YES')
#         else:
#             print('NO')

# if __name__ == '__main__':
#     weird()


# t = int(input())


# for i in range(t):
#     try:
    
#         empty_tobs = 0
#         for i in range(t):
#             empty_tobs = 0
#             bottles = list(input().split())
#             for items in bottles:
#                 if items == '0':
#                     empty_tobs += 1
#                 else:
#                     pass
                    

#     except Exception as e:
#         print(f'LOL, ran into some problem: {e}')
#     finally:
#         if empty_tobs >= 2:
#             print("Water filling time")
#         else:
#             print('Not now')

# t = int(input())

# for i in range(t):
#     a,b,c = map(int, input().split())
#     if (a+b+c) >= 2:
#         print('Not now')
#     elif (a+b+c) < 2:
#         print('Water filing time')
#     else:
#         pass

# t = int(input())
# for i in range(t):
#     weapons_rack = list(map(int, input().split()))
#     lucky_soldiers = 0
#     unlucky_soldiers = 0
#     for weapons in weapons_rack:
#         if (weapons%2 == 0):
#             lucky_soldiers += 1
#         elif (weapons%2 != 0):
#             unlucky_soldiers += 1
#         else:
#             pass
        
#     if lucky_soldiers > unlucky_soldiers:
#         print('READY FOR BATTLE')
#     else:
#         print('NOT READY')

# t = int(input())
# for i in range(t):
#     weapons_rack = list(map(int, input().split()))
#     lucky = 0
#     unlucky = 0
#     for weapon_no in range(len(weapons_rack)-1):
#         if weapons_rack[weapon_no] % 2 == 0:
#             lucky += 1
#         elif weapons_rack[weapon_no+1] % 2 == 0:
#             unlucky += 1
#         else:
#             pass

#     if lucky > unlucky:
#         print('READY FOR BATTLE')
#     else:
#         print('NOT READY')

# t = int(input())
# for i in range(t):
#     n,x = map(int, input().split())
#     process = False
#     diff = (n-x)
#     if diff > 0:
#         process = True
#         while process:
#             if diff % 4 == 0:
#                 print(diff//4)
#                 process = False
#                 break
#             elif diff % 4 != 0 and diff < 4:
#                 print(1)
#                 process = False
#                 break
#             else:
#                 packets = (diff//4)+1
    #             print(packets)
    #             process = False
    #             break
    # else:
    #     pass
            
# t = int(input())
# for i in range(t):
#     n, x = map(int, input().split())
#     if n > x:
#         if (n-x) > 4 and (n-x)%4 == 0:
#             print((n-x)//4) 
#         elif (n-x) > 4 and (n-x)%4 != 0:
#             print(((n-x)//4)+1)
#         else:
#             print(1)
#     elif n == x:
#         print(0)
#     else:
#         print(0)

# t = int(input())
# for i in range(t):
#     seat = int(input())
#     if seat in range(1,51):
#         print('LEFT')
#     else:
#         print('RIGHT')

