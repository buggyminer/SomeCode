import random
import time
import unittest


def generate_table(n, m, p, v):
    table = [[0] * m for i in range(n)]
    random.seed(time.process_time())
    count = 0
    while count < p:
        i = random.randint(0, n * m - 1)
        x = i // m
        y = i % m
        # print("x is ", x, "y is", y)
        if(table[x][y]==0):
            count=count+1
            table[x][y] = random.randint(1, v)
    return table


def dp(table):
    n, m = len(table), len(table[0])
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + table[i][j]

    return dp[n][m]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table = generate_table(10, 7, 40, 30)
    print(table)
    res = dp(table)
    print(res)


class coin_collection_test(unittest.TestCase):
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
