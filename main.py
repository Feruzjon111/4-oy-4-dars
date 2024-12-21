# 14

# def func(n, k):
#     count = 0
#     for i in n:
#         if i < k:
#             count += 1
#     return count
# n = list(map(int, input("Sonlar to'plamini kiriting (vergul bilan ajrating): ").split(',')))
# k = int(input("K sonini kiriting: "))
# natija = func(n, k)
# print(natija)


# 15

# def func(n, k):
#     s = 1
#     for i in n:
#         if i > k:
#             return i
#         s += 1
#     return 0
# n = list(map(int, input("Sonlar to'plamini kiriting (vergul bilan ajrating): ").split(',')))
# k = int(input("K sonini kiriting: "))
# natija = func(n, k)
# print(natija)


#16

# def func(n, k):
#     s = 0
#     for i in range(len(n)):
#         if n[i] > k:
#             s = i+1
#     return s
# n = list(map(int, input("Sonlar to'plamini kiriting (vergul bilan ajrating): ").split(',')))
# k = int(input("K sonini kiriting: "))
# natija = func(n, k)
# print(natija)


# 17

# def func(b, n):
#         print(f"B soni: {b}")
#         print(f"Sonlar to'plami: ")
#         for i in l:
#             print(i)
# b = float(input("B sonini kiriting: "))
# n = int(input("N sonini kiriting: "))
# l = []
# for j in range(n):
#     a = float(input(f"{j+1}-sonni kiriting: "))
#     l.append(a)
# func(b, n)


# 18

# def func(n):
#     l.sort()
#     i = 0
#     while i < len(l) - 1:
#         if l[i] == l[i + 1]:
#             l.remove(l[i])
#             l.remove(l[i])
#         else:
#             i += 1
#     print(f"Har xil qiymatli elementlar:")
#     for j in l:
#         print(j)
#
# n = int(input("N sonini kiriting: "))
# l = []
# for k in range(n):
#     a = float(input(f"{k + 1}-sonni kiriting: "))
#     l.append(a)
# func(n)


# 19

# def func(n):
#     lst = []
#     for i in range(1, len(l)):
#         if l[i] < l[i-1]:
#             lst.append(l[i])
#     print(f"Chap qo'shnisidan kichik sonlar:")
#     for j in lst:
#         print(j)
#     print(f"Chap qo'shnisidan kichiklari soni: {len(lst)}")
# n = int(input("N sonini kiriting: "))
# l = []
# for k in range(n):
#     a = float(input(f"{k + 1}-sonni kiriting: "))
#     l.append(a)
# func(n)







