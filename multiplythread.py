import threading
import numpy as np



class Multiplythread(threading.Thread):
    def __init__(self, num, a, b, res_dict):
        threading.Thread.__init__(self)
        self.tnum = num
        self.A = a
        self.B = b
        self.res_dict =  res_dict

    def run(self):

        columns = []
        for x in range(self.B.shape[1]):
            tmp = []
            for i in range(self.B.shape[0]):
                tmp.append(self.B[i, x])
            columns.append(tmp)

        rows = []
        for x in range(self.A.shape[0]):
            tmp = []
            for i in range(self.A.shape[1]):
                tmp.append(self.A[x, i])
            rows.append(tmp)

        #[print("Thread_{} row:{}\n".format(self.tnum, x)) for x in rows]
        #[print( "Thread_{} column:{}\n".format(self.tnum,x) ) for x in columns ]

        result = np.zeros((0, self.A.shape[1]))
        tmp = np.zeros((1, 0))
        for row in self.A[:]:
            #print("Taki jest wiersz {}".format(row))
            for col in self.B.T:
                #print("result_size {}, tmp_size {}", result.shape, tmp.shape)
                tmp = np.concatenate((tmp, row * col.T), 1)
            result = np.concatenate((result, tmp), 0)
            tmp = np.zeros((1, 0))

        lock = threading.Lock()
        lock.acquire() # will block if lock is already held
        self.res_dict[self.tnum] = result
        lock.release()



"""
Single thread computing matrix multiplication. Asserts that inserted data are correct.
"""