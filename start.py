#_*_coding:utf-8_*_
import arithmetic
import sys,getopt
import decimal 
from random import randint

def main(argv):
	#命令行参数：当输入-h时显示帮助文档；当输入-n时，继续输入的数值即为题目个数
	number = 0
	try:
		options,args = getopt.getopt(sys.argv[1:],"hn:",["help","num="])
	except getopt.GetoptError:
		print ('start.py -n <the number of questions>  -h <help for this program>')
		sys.exit(2)
	for opt,arg in options:
		#当输入为-h时，打印提示信息
		if opt == '-h':
			print ('使用方法：start.py -n <the number of questions> or -h <help for this program>')
			sys.exit()
		#当输入为-n时，后续输入的数字即为题目个数
		elif opt in ("-n", "--num"):
			number = int(arg)
	
	print (u"本次共"+str(number)+u"题，满分100分\n")
	#count用来计数回答正确的题目个数
	count = 0
	for i in range(1,number+1):
	#op_num控制随机生成的运算符个数
		op_num = randint(1,10)
		x = arithmetic.combin_num_opera(op_num)
		try:
			ans = arithmetic.operate(x)
		except Exception as e:
			print("Error:",e)
	#	print ans
	#	pdb.set_trace()
		print (str(i)+": "+arithmetic.display_arith(x) + "= ",end="")
		#由于要考虑输入的可能是一个分数
		#因此直接以字符串类型输入，再将正确结果转化为字符串进行比较
		res = input()
		if(res == str(ans)):
			print (u"正确！"+"\n")
			count = count + 1
		else:
			print (u"不正确！正确答案是："+str(ans)+"\n")
	#最终成绩保留小数点后两位
	score = round(100 * float(count) / float(number),2)
	print (u"本次练习共答对"+str(count)+"题，"+u"总得分: " + str(score))

if __name__ == '__main__':
	main(sys.argv[1:])
