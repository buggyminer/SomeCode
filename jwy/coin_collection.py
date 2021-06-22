import random
import time
import unittest

"""
1、根据参数初始化二维列表
2、根根据网格大小生成dp表
3、根据状态方程，逐行完成dp表
4、返回终点的dp表值
"""


# 初始化网格
def generate_table(n, m, p, v):
    table = [[0] * m for i in range(n)]
    # 更新随机数种子
    random.seed(time.process_time())
    count = 0
    while count < p:
        i = random.randint(0, n * m - 1)
        x = i // m
        y = i % m
        if(table[x][y]==0):
            count=count+1
            table[x][y] = random.randint(1, v)
    return table

# 使用dp解决问题
def dp(table):
    # 初始化dp列表
    n, m = len(table), len(table[0])
    dp = [[0] * (m + 1) for i in range(n + 1)]
# 编写撞状态方程
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + table[i][j]
# 返回dp表末尾的值
    return dp[n][m]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table = generate_table(10, 7, 40, 30)
    print(table)
    res = dp(table)
    print(res)


class coin_collection_test(unittest.TestCase):
    # 测试参数是否正确
    def test_generate_coin(self):
        n, m, p, v = 10, 7, 40, 30
        table = generate_table(n, m, p, v)
        self.assertEqual(len(table), n)
        self.assertEqual(len(table[0]), m)
        count = 0
        for row in table:
            for col in row:
                self.assertLessEqual(col, v)
                if (col != 0):
                    count = count + 1
        print(count)
        self.assertEqual(count, p)

    # 手工编写测试用例
    def test_dp_right(self):
        # table = generate_table(10, 7, 40, 30)
        test_table_list=[
            [
                [1,0,0],
                [0,1,0],
                [0,0,1],
            ],
            [
                [0, 2, 0],
                [0, 1, 5],
                [10, 0, 0],
            ],
            [
                [1, 2, 2],
                [3, 1, 2],
                [0, 2, 1],
            ],
        ]
        test_result_lsit=[
            3,10,8
        ]
        for table,res in zip(test_table_list,test_result_lsit):
            self.assertEqual(res,dp(table))
