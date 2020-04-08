# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 1级台阶：1种跳法
# 2级台阶：2种跳法
# 3级台阶：3种跳法
# 4级台阶：5种跳法
# 类似于斐波那契数列
#  -*- coding:utf-8 -*-
class Solution:
	def jumpFloor(self, number):
		# write code here
		a = 1
		b = 1
		for i in range(number):
			a, b = b, a + b
		return a

	def recursionJumpFloor(self, number):
		if number == 1:
			return 1
		if number == 2:
			return 2
		return self.recursionJumpFloor(number - 1) + self.recursionJumpFloor(number - 2)

	def abonmalJumpFloor(self, number):
		if number == 1:
			return 1
		return 2 ** (number - 1)


flog = Solution()
count = flog.recursionJumpFloor(2)
count1 = flog.jumpFloor(4)
print(count1)
print(count)
