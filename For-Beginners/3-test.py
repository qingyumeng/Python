1. 使用交互模式或者编写一个小程序解决下面的问题。
(a) 3 个人在餐厅吃饭，想分摊饭费。总共花费35.27 美元，他们还想留15%
的小费。每个人该怎么付钱？
 (b) 计算一个12.5m×16.7m 的矩形房间的面积和周长。
2. 写一个程序，把温度从华氏度转换为摄氏度。转换公式是C = 5 / 9* (F–32)。
（提示：当心整除问题！）
3. 你知道怎么计算坐车去某个地方需要花多长时间吗？相应的公式（用文字表
述）是“旅行时间等于距离除以速度”。编写一个程序，计算以80 km/h 的速
度行驶200 km 需要花多长时间，并显示答案。

import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "This is a secret number game"
print "number 1 to 99,can try 6 times"
while guess != secret and tries < 6:
    guess = input("input your number:")
    if guess < secret:
        print "it's low"
    elif guess > secret:
            print "it's too high"

    tries = tries + 1

if guess == secret:
    print "Got it"
else:
    print "No More time"
    print "the number is:",secret
