# import multiprocessing
#
#
# def squre(x):
#     return x * x
#
#
# if __name__ == "__main__":
#     numbers = [2, 4, 5, 6, 8]
#
#     with multiprocessing.Pool() as pool:
#         result = pool.map(squre, numbers)
#     print(result)
#
#
# # import asyncio
# # import nest_asyncio
# # async def greet(name):
# # 	await asyncio.sleep(1)
# # 	print(name)
# # async def main():
# # 	await asyncio.gather(greet("Geeks"), greet("For"), greet("Geeks"))
# # # If in a Jupyter notebook or IPython environment:
#
# # nest_asyncio.apply()
# # if __name__ == "__main__":
# # 	asyncio.create_task(main())
#
#
# def tasks(n):
#     value = 0
#
#     while value < n:
#         yield value
#         value += 1
#
#
# for i in tasks(4):
#     print(i)
#
# from datetime import date
#
#
# class Abd():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromdob(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def Isadult(age):
#         return age > 18
#
#
# p = Abd("aravind", 30)
# p2 = p.fromdob("arun", 1996)
# print(p2.name, p2.age)
# p4 = p.Isadult(19)
# print(p4)
#
# # inputs=input("enter the string")
#
# # words=inputs.split(' ')
#
# # p={}
#
# # for i in words:
# #     count=words.count(i)
# #     p.update({i:count})
# # print(p)
#
#
# lis = [10, 12, 32, 43, 10, 32, 26, 24, 12]
# c = []
# for i in range(len(lis)):
#     for j in range(i + 1, len(lis)):
#
#         if lis[i] == lis[j]:
#             c.append(lis[i])
# for i in lis:
#     if i in c:
#         lis.remove(i)
# print("duplicates", c)
# print("after remove", lis)
#
#
# def cal(s):
#     return "".join(["{" if j.lower().count(j) == 1 else "}" for j in s])
#
#
# print(cal("aBc"))
#
# str1 = "isincisinefsdfsdinedfsdaginedhrtsyrine"
# str2 = "ine"
# len1 = len(str1)
# len2 = len(str2)
# print(len1, len2)
# count = 0
#
# for i in range(len1 - len2 + 1):
#     j = 0
#     for k in range(i, i + len2):
#         if str1[k] != str2[j]:
#             break
#         j += 1
#     if j == len2:
#         count += 1
# print(count)
#
# data = [1, 2, 3, [4, [5, 6, 7, [8, 9]]]]
#
#
# def mm(cc):
#     for each in cc:
#         if isinstance(each, list):
#             mm(each)
#         else:
#             print(each)
#
#
# print(mm(data))


class First:
    def pvalue(self, name, age):
        self.name=name
        self.age=age
        print(name, age)


f = First()
f.pvalue("arun", 27)