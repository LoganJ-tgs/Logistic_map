# 0 < x < 1
x = .2

k = 40
# 0 < r < 4
import matplotlib.pyplot as plt
import numpy as np

# plot this
def calc(x, r, times = 100):
    if times == 0:
        return [x]
    listt = calc(x, r, times = times - 1)
    prex = listt [len(listt) - 1]
    p = r * prex * (1 - prex)
    listt.append(p)
    return listt

def cut(listt):
    prior = listt [len(listt) - 1]
    index = 2
    while prior != listt [len(listt) - index]:
        # check if within a certain range from last point
        prior = listt [len(listt) - index]
        index += 1
    return listt [-(index-1):]

def main():
    plt.figure(figsize=(8, 6))

    for r in np.linspace(2, 4, 2000):
        l = calc(x, r)
        l = l [-k:]
        plt.scatter(np.ones_like(l) * r, l, c="blue", s=0.1)


    plt.xlabel("R")
    plt.ylabel("X")
    plt.grid()
    plt.savefig("result.png")

if __name__ == '__main__':
    main()

