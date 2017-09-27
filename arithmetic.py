# -*- coding=utf-8 -*-
from random import choice
from random import randint
from fractions import Fraction
import itertools
import pdb


#定义栈以及相关方法，便于：1将中缀式转化为后缀式，2后缀式结果的计算
class Stack: 
    def __init__(self): 
        self.items = [] 
    def isEmpty(self): 
         return self.size() == 0 
    def push(self, item): 
        self.items.append(item) 
    def pop(self): 
        return self.items.pop()  
    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 
    def size(self): 
        return len(self.items) 
	
#ran_num(x_num)方法生成x_num个随机数（参数x_num由全局变量传入，是运算符个数），返回随机数列表
def ran_num(x_num):
	#num_list列表保存随机生成的数值
	num_list = []	
	for i in range(0,x_num):	
		#设置flag标志，随机生成0或1，当flag为0时，生成一个随机整数；当flag为1时，生成一个随机分数
		flag = randint(0,1)
		if(flag == 0):
			num = randint(0,100)
			num_list.append(num)
		else:
			tmp1, tmp2= randint(1,10), randint(1,10)
			if(tmp1 > tmp2):
				frac = Fraction(tmp2, tmp1)
			else:
				frac = Fraction(tmp1, tmp2)
			num_list.append(frac)
	return num_list

#ran_oper(x_op)生成x_op个随机操作符(操作符个数由参数x_op控制),返回操作符列表
def ran_oper(x_op):
	#设置列表op保存四种操作符
	#通过取随机数(范围为0~3),来确定所取操作符在列表中的下标，以实现随机生成操作符
	op = ["+", "-", "*", "/"]	  
	op_list = []
	for i in range(0,x_op):
		tmp = choice(op)
		op_list.append(tmp)
	return op_list

#将随机数与随机运算符列表进行交叉合并
def combin_num_opera(x_op):
	num = ran_num(x_op + 1)
	oper = ran_oper(x_op)
	arith_list = list(itertools.chain.from_iterable(zip(num,oper)))
	length = len(num)
	arith_list.append(num[length-1])
	return arith_list

#对生成的四则运算式进行结果的计算
def operate(lst):
	#设置运算符优先级
	op_oprior = {"+":0, "-":0, "*":1, "/":1}
	op = ["+", "-", "*", "/"]
	#postfix_lst保存后缀表达式
	postfix_lst = []
	#利用栈实现中缀表达式与后缀表达式的转换
	#扫描合并列表中的每个元素，当为数值时直接存入postfix_lst中
	#当为运算符时，将其与栈顶运算符的优先级进行比较：
	#当该运算符优先级比栈顶大时，将其压入栈；否则将该运算符依次与栈内剩余运算符优先级进行比较，
	#若栈顶运算符优先级大于等于该运算符，则弹出并存入postfix_lst中，最后将该运算符压入栈中
	s = Stack()
	for tmp in lst:
		if(tmp not in op):
			postfix_lst.append(tmp)
		else:
			while(s.size() > 0  and op_oprior[tmp] <= op_oprior[s.peek()]):
				postfix_lst.append(s.pop())
			s.push(tmp)
	len = s.size()
	while(len > 0):
		postfix_lst.append(s.pop())
		len = len -1
#	print postfix_lst

	#利用栈计算后缀表达式的值
	#扫描postfix_lst，当元素为数值时压入栈，当碰到运算符时，弹出栈顶前两个数值并进行计算
	#再将计算结果压入栈
	resault = Stack()
	for item in postfix_lst:
		if(item not in op):
			resault.push(item)
		else:
			b = resault.pop()
			a = resault.pop()
			if(item == "+"):
				resault.push(a+b)
			if(item == "-"):
				resault.push(a-b)
			if(item == "*"):
				resault.push(a*b)	
			#在进行除法运算时注意判断两个数是否都为整数
			#若都为整数，需要将除法直接表示为Fraction(a,b)，否则计算结果将只取整数部分			
			if(item == "/"):
				if(b != 0):
					if(isinstance(a, int) and isinstance(b, int)):
						resault.push(Fraction(a,b))
					else:
						resault.push(a/b)
				else:
					le = len(lst)
					lst = arithmetic.combin_num_opera(le)
					operate(lst)
	return resault.peek()

#display_arith(lst)实现将随机数与随机操作符合并列表，转化成字符串形式,便于算式的输出显示
def display_arith(lst):
	#利用字典将python中的运算符与数学运算符进行对应
	op_dict = {"+":"+", "-":"-", "*":"×", "/":"÷"}  
	op = ["+", "-", "*", "/"]
	length = len(lst)
	for i in range(length):
		if(lst[i] in op):
			lst[i] = op_dict[lst[i]]
	#将列表中每个元素转化成字符再进行连接形成字符串
	return ''.join(str(v) for v in lst)
