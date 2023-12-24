import multiprocessing
def squre(x):
    return x*x

if __name__=="__main__":
    numbers=[2,4,5,6,8]

    with multiprocessing.Pool() as pool:
        result=pool.map(squre,numbers)
print(result)