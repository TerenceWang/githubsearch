import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def recall(nums, target):
	res = []
	count = 0
	for num in nums:
		if num>=target:
			count = count + 1
		res.append(count)
	return res

def prec(nums, target):
	res = []
	count = 0

	for i in range(len(nums)):
		if nums[i]>=target:
			count = count + 1
		res.append(count*1.0/(i+1))
	return res


#class Exception
f1 = [3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
t1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#class NoUsernameException
f2 = [3, 0, 2, 0, 0, 0, 0, 0, 0, 0]
t2 = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function search
f3 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t3 = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function public static void search
f4 = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
t4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function sort(Comparable[] )
f5 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t5 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

#function query
f6 = [1, 1, 0, 2, 0, 0, 0, 0, 0, 0]
t6 = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]

#usage "throws IOException"
f7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t7 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#function push
f8 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
t8 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#function public boolean isEmpty()
f9 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
t9 = [2, 0, 0, 0, 0, 0, 0, 0, 3, 0]

#function public static void main(String[] args)
f10 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t10 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]




c22 = [3,2,2,1,1,1,1,1,1,1]
c23 = [2,1,0,1,0,0,1,0,0,2]
c24 = [3,3,3,3,3,2,3,3,3,3]
c25 = [3,2,1,2,2,3,2,3,3,0]
c26 = [3,3,3,3,3,3,3,3,3,3]
c27 = [3,1,0,0,0,0,1,1,0,0]
c28 = [3,2,1,1,2,2,0,0,0,0]
c29 = [0,0,0,0,1,0,1,1,2,0]
c30 = [3,3,3,3,3,3,3,3,3,2]
c31 = [3, 3, 0, 3, 1, 3, 3, 3, 0, 0]  
c32 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c33 = [3, 0, 2, 2, 2, 2, 2, 2, 2, 2]
c36 = [0, 0, 0, 3, 0, 0, 0, 3, 0, 0]
c37 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c38 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c39 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
c40 = [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
c41 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]


f27 = [3,0,3,1,0,1,1,0,1,3]
f28 = [2,2,1,2,0,1,3,0,1,0]
f29 = [2,0,2,0,0,0,0,0,0,0]
f34 = [3, 3, 3, 3, 0, 0, 0, 3, 0, 0]
f35 = [3, 3, 3, 3, 0, 0, 0, 3, 0, 0]
f36 = [3, 3, 3, 3, 0, 0, 0, 3, 3, 3]
f38 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
f39 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
f40 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
f41 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]




t22 = [3,0,0,1,2,0,1,0,1,1]
t23 = [1,0,0,1,0,0,1,1,0,0]
t24 = [3,3,3,3,3,3,1,1,1,0]
t25 = [1,2,3,0,2,0,0,0,2,0]
t26 = [3,3,3,3,3,3,3,3,3,3]
t27 = [1,1,3,1,1,0,0,0,0,0]
t28 = [0,0,1,1,2,1,0,0,0,0]
t29 = [2,2,2,2,0,2,2,2,2,1]
t30 = [3,3,3,3,3,3,3,3,3,3]
t31 = [3, 2, 0, 0, 0, 0, 3, 0, 0, 0] 
t32 = [3, 3, 3, 3, 3, 3, 0, 3, 0, 3]
t33 = [0, 0 ,0, 3, 0, 3, 0, 3, 0, 0]
t34 = [3, 0, 0, 3, 3, 3, 0, 3, 0, 3]
t35 = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t36 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t37 = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t38 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t39 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
t40 = [3, 3, 0, 0, 0, 0, 0, 0, 0, 0]
t41 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 0]



t11 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t12 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
f12 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
t13 = [1, 1, 1, 1, 3, 0, 0, 0, 1, 0]
f13 = [3, 2, 0, 2, 3, 3, 2, 2, 2, 3]
t14 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
f14 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
t15 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f15 = [1, 0, 0, 2, 1, 1, 0, 0, 0, 0]
t16 = [0, 0, 0, 0, 3, 1, 2, 1, 1, 0]
f16 = [1, 3, 1, 0, 1, 2, 1, 1, 3, 1]
t17 = [1, 2, 1, 2, 2, 2, 2, 2, 3, 2]
f17 = [1, 1, 1, 0, 0, 0, 2, 0, 0, 0]
t18 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f18 = [2, 1, 1, 1, 0, 0, 0, 0, 1, 0]
t19 = [2, 1, 1, 1, 0, 1, 0, 1, 1, 1]
f19 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t20 = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1]
f20 = [1, 1, 0, 0, 1, 1, 1, 0, 0 ,1]
t21 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f21 = [0, 0, 0, 0, 1, 2, 1, 0, 0 ,1]
c = [
	c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,
	c32,c33,c36,c37,c38,c39,c40,c41]
t = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,
	t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,
	t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,
	t32,t33,t34,t35,t36,t37,t38,t39,t40,t41]

	
f = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,
f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,
f27,f28,f29,f34,f35,f36,f38,f39,f40,f41]



x = [i for i in range(0,10)]

cpre = [0 for i in range(0,10)]
tpre = cpre
fpre = cpre

crecall = cpre
frecall = cpre
trecall = cpre

target = 2

for i in range(len(c)):
	cpre = np.add(cpre,prec(c[i],target))
	crecall = np.add(crecall,recall(c[i],target))

for i in range(len(f)):
	fpre = np.add(fpre,prec(f[i],1))
	frecall = np.add(frecall,recall(f[i],target))	

for i in range(len(t)):
	tpre = np.add(tpre,prec(t[i],1))
	trecall = np.add(trecall,recall(t[i],target))


totalcount = 10.0

togetherpre = np.add(cpre,fpre)
togetherpre = togetherpre/(len(c)+len(f))


cpre = cpre/len(c)
tpre = tpre/len(t)
fpre = fpre/len(f)

togetherrecall = np.add(crecall,frecall)

crecall = crecall/(totalcount*len(c))
trecall = trecall/(totalcount*len(t))
frecall = frecall/(totalcount*len(f))

togetherrecall = togetherrecall/(totalcount*(len(c)+len(f)))

def drawplot(number,A1,B1,A2,B2,str1, str2):
	ff = plt.figure(number)
	ax1 = plt.subplot(211)
	ax2 = plt.subplot(212)

	plt.sca(ax1)
	plt.plot(x,A1,label=str1)
	plt.plot(x,B1,label=str2)
	plt.legend(loc='best')
	plt.ylabel('Precision')

	plt.sca(ax2)
	plt.plot(x,A2,label=str1)
	plt.plot(x,B2,label=str2)
	plt.legend(loc='best')
	plt.xlabel('Items')
	plt.ylabel('Recall')
	return ff

ff = drawplot(1,tpre,togetherpre,trecall,togetherrecall,"full","class+function")
ff.savefig("full_together.pdf", bbox_inches='tight')


ff = drawplot(2,cpre,fpre,crecall,frecall,"class","function")
ff.savefig("class_function.pdf", bbox_inches='tight')

# pp = PdfPages('class_function.pdf')
# plt.savefig(pp, format='pdf')

# plt.figure(1)
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)

# plt.sca(ax1)
# plt.plot(x,tpre,label="full")
# plt.plot(x,togetherpre,label="class+function")
# plt.legend(loc='best')


# plt.sca(ax2)
# plt.plot(x,trecall,label="full")
# plt.plot(x,togetherrecall,label="class+function")
# plt.legend(loc='best')

# plt.figure(2)
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)

# plt.sca(ax1)
# plt.plot(x,tpre,label="full")
# plt.plot(x,cpre,label="class")
# plt.legend(loc='best')


# plt.sca(ax2)
# plt.plot(x,trecall,label="full")
# plt.plot(x,crecall,label="class")
# plt.legend(loc='best')


# plt.figure(3)
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)

# plt.sca(ax1)
# plt.plot(x,tpre,label="full")
# plt.plot(x,fpre,label="function")
# plt.legend(loc='best')

# plt.sca(ax1)
# plt.plot(x,trecall,label="full")
# plt.plot(x,frecall,label="function")
# plt.legend(loc='best')
