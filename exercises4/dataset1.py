import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
input: ndarray
output: ndarray
"""
def lesson1(x):
    return np.sin(np.pi * x * 0.8) * 10

"""
input: 
output: pandas.Dataframe
"""
def lesson2():
    np.random.seed(0)
    x_2 = np.array([])
    for _ in range(20):
        rand_num = np.random.uniform(-1.0, 1.0)
        x_2 = np.append(x_2, rand_num)
    y_2 = lesson1(x_2)
    df_x_2 = pd.DataFrame(x_2,columns=["観測点"])
    df_y_2 = pd.DataFrame(y_2, columns=["真値"])
    df = pd.concat([df_x_2, df_y_2], axis=1)
    # グラフ描画
    x = np.arange(-1, 1 , 0.1)
    y = lesson1(x)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x, y,label="sin")
    plt.plot(x_2,y_2,'.', label="ex1.2",markersize=15)
    plt.legend()
    plt.savefig("lesson2.png")
    plt.show()
    return df

"""
input:
output: pandas.Dataframe
"""
def lesson3():
    noizu = np.random.normal(loc=0.0, scale=2.0, size=20)
    noizu = noizu/2
    df = lesson2()
    true_nums = df["真値"]
    watch_point = df["観測点"]
    nd_true_nums = true_nums.values
    noizu_plus_true_nums = nd_true_nums + noizu
    df_noizu = pd.DataFrame(noizu_plus_true_nums, columns=["観測値"])
    df = pd.concat([df, df_noizu], axis=1)
    x = np.arange(-1, 1 , 0.1)
    y = lesson1(x)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x, y,label="sin")
    plt.plot(watch_point,true_nums,'.', label="ex1.2",markersize=15)
    plt.plot(watch_point,noizu_plus_true_nums,'.', label="ex1.3",markersize=15)
    plt.legend()
    plt.savefig("lesson3.png")
    plt.show()
    return df

"""
input: df, file_name
output:
"""
def lesson4(df, tsv_name):
    df.to_csv(f"{tsv_name}.tsv", sep='\t', index=False)

"""
input: file_name
output: pandas.Dataframe
"""
def lesson5(tsv_name):
    df = pd.read_table(f"{tsv_name}.tsv")
    return df