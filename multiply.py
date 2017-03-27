import multiplythread
import numpy as np

result_dict = {}
thread_amount = 3
tmp_a = open("./data/A.txt", "r").read().split("\n", 2)[2].replace("   ", ",").replace("\n", ";")
tmp_b = open("./data/B.txt", "r").read().split("\n", 2)[2].replace("   ", ",").replace("\n", ";")

matrix_a = np.matrix(tmp_a)
matrix_b = np.matrix(tmp_b)
#print("Main! \nA= {}\n B={}".format(matrix_a,matrix_b))
#print("Wynik=\n{}".format(matrix_a*matrix_b))

#print(matrix_a.shape)
#print(matrix_b.shape)

if matrix_a.shape[1] != matrix_b.shape[0]:
    print("Bad matrices size!")
    quit()

result_matrix = np.zeros((0, matrix_b.shape[1]))

thread_tab = []
step = int(matrix_a.shape[0] / thread_amount)
rest = int(matrix_a.shape[0] % thread_amount)
start = 0

for i in range(thread_amount):
    if i < rest:
        #print("Thread start:{} end:{}".format(start, start+step+1))
        thread_tab.append(
            multiplythread.Multiplythread(
                i, matrix_a[start: start+step+1], matrix_b , result_dict))
        start += 1
    else:
        #print("Thread start:{} end:{}".format(start, start + step ))
        thread_tab.append(
            multiplythread.Multiplythread(
               i, matrix_a[start:start+step:], matrix_b, result_dict))
    start += step

for th in thread_tab:
    th.start()

while len(result_dict.keys()) < thread_amount:
    #print(result_dict.keys())
    pass

for i in range(thread_amount):
    result_matrix = np.concatenate((result_matrix, result_dict[i]), 0)

print("Wynik2=\n{}".format(result_matrix))