import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
b = np.array([[1, 2, 3]*3]).reshape((-1, 3))
print("a:", a)
print("b:", b)

c = a * b
print("a*b:", c)
c = c.sum(axis=1)  # 分子
print("分子:", c)

d = np.sqrt((a*a).sum(axis=1))
print((a*a).sum(axis=1))
print(d)
e = np.sqrt((b*b).sum(axis=1))
print(e)

print(c/(d*e))

cosine = ((a*b).sum(axis=1)) / (np.sqrt((a*a).sum(axis=1)) * np.sqrt((b*b).sum(axis=1)))
print(cosine)

def cal_cosine(vec1, vec2):
    return (vec1*vec2).sum()/(np.sqrt((vec1*vec1).sum())*np.sqrt((vec2*vec2).sum()))
