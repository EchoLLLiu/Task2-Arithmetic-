import unittest
import arithmetic
from fractions import Fraction

class ArithmeticTest(unittest.TestCase):
	def setup(self):
		pass

	# 测试Stack类中方法是否正确
	def testStack(self):
		s = arithmetic.Stack()
		lst = [1,2,3,4,5]
		for i in lst:
			s.push(i)
		self.assertEqual(s.pop(),5)
		s.push(6)
		self.assertEqual(s.pop(),6)
		self.assertEqual(s.peek(),4)
		self.assertEqual(s.isEmpty(),0)
		self.assertEqual(s.size(),4)
		print("test Stack() pass")

	#测试ran_num(x_num)函数是否生成了x_num个随机数，以及测试随机数的合法性
	def testran_num(self):
		n = 100
		flag = 0 
		num_list = arithmetic.ran_num(n)
		self.assertEqual(len(num_list),100)
		for num in num_list:
			if(isinstance(num, int)):
				if(num <= 100 and num >= 0):
					flag = 1
			else:
				if(num < 1 and num > 0):
					flag = 1
		self.assertEqual(flag,1)
		print("test ran_num(x_num) pass")

	#测试ran_oper(x_op)函数是否生成了x_op个运算符，以及测试每个运算符的合法性
	def testran_oper(self):
		n = 100
		count = 0
		op = ["+", "-", "*", "/"]	
		op_lst = arithmetic.ran_oper(n)
		self.assertEqual(len(op_lst),100)
		for o in op_lst:
			if(o in op):
				count = count + 1
		self.assertEqual(count,n)
		print("test ran_oper(x_op) pass")

	#测试combin_num_opera(x_op)函数中操作数与运算符是否交叉合并
	def testcombin_num_opera(self):
		n = 10
		op = ["+", "-", "*", "/"]
		arith_lst = arithmetic.combin_num_opera(n)
		count_num = 0
		flag_num= 1
		count_op = 0
		flag_op = 1
		length = len(arith_lst)
		for x in range(0,length):
			if(x % 2 == 0):
				count_num = count_num + 1
				if(isinstance(x,int) or x<1):
					flag_num = 1
				else:
					flag_num = 0
			else:
				count_op = count_op + 1
				if(arith_lst[x] in op):
					flag_op = 1
				else:
					flag_op = 0
		self.assertEqual(count_num,n+1)
		self.assertEqual(count_op,n)
		self.assertEqual(flag_num,1)
		self.assertEqual(flag_op,1)
		print("test combin_num_opera(op) pass")

	#测试operate(lst)函数，其计算结果是否正负整数和分数
	def testoperate(self):
		self.assertEqual(arithmetic.operate([1,"+",2,"+",3,"+",4]),10)
		self.assertEqual(arithmetic.operate([Fraction(1,2),"+",2,"*",3,"-",1]),Fraction(11,2))
		self.assertEqual(arithmetic.operate([2,"+",3,"-",4,"*",5]),-15)
		self.assertEqual(arithmetic.operate([1,"-",Fraction(2,3),"*",Fraction(4,5),"-",6]),Fraction(-83,15))
		print("test operate(lst) pass")

def main():
	test = unittest.TestSuite()
	test.addTest(ArithmeticTest("testStack"))
	test.addTest(ArithmeticTest("testran_num"))
	test.addTest(ArithmeticTest("testran_oper"))
	test.addTest(ArithmeticTest("testcombin_num_opera"))
	test.addTest(ArithmeticTest("testoperate"))

	runner = unittest.TextTestRunner()
	runner.run(test)

if __name__ == '__main__':
	main()
