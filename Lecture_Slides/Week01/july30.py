import random
from time import time

def random_instance(n):
    """ creates random instance of size n """

    return [ random.randint(-10,10) for i in range(n) ] 


def find_optimal_window(A):
    """ Given daily fluctuation, find optimal investment window """

    def evaluate(A,a,b):
        """ returns A[a]+...+A[b] """

        return sum(A[a:b+1])

    n = len(A)
    i_answer = j_answer = 0
    for i in range(0,n):
        for j in range(i,n):
            if evaluate(A,i,j) > evaluate(A,i_answer, j_answer):
                i_answer = i
                j_answer = j

    return (i_answer, j_answer)


def find_optimal_window_faster(A):
    """ Given daily fluctuation, find optimal investment window """

    def evaluate(B,a,b):
        """ returns A[a]+...+A[b] """

        return B[a] - B[b+1]

    n = len(A)

    B = []
    for i in range(0,n):
        B.append( sum(A[i:]) )
    B.append(0)
    
    i_answer = j_answer = 0
    for i in range(0,n):
        for j in range(i,n):
            if evaluate(B,i,j) > evaluate(B,i_answer, j_answer):
                i_answer = i
                j_answer = j

    return (i_answer, j_answer)



def find_optimal_window_superfast(A):
    """ Finds optimal window of investment given daily stock price fluctions """

    n = len(A)

    B = []
    aux = sum(A)
    for i in range(0, n):
        B.append(aux)
        aux = aux - A[i]
    B.append(0)

    OPT = [ 0 ]
    for j in range(1,n):
        if B[j] > B[OPT[j-1]]:
            OPT.append(j)
        else:
            OPT.append(OPT[j-1])
    
    return max( zip(OPT,range(n)), key=lambda x: B[x[0]]-B[x[1]+1] )




















def capped_function_timer(instances, function, time_bound = 1):
    """ returns function on instances, but stops once it takes more than time_bound """

    answer = []
    for x in instances:
        start = time()
        function(x)
        elapsed = time() - start
        answer.append(elapsed)        
        if elapsed > time_bound:
            break

    return answer
    



def plot_consecutive_ratios(sizes, runtimes, plotcolor='blue'):

    ratios = []
    for i in range(1,len(runtimes)):
        ratios.append(runtimes[i] / runtimes[i-1])

    x = sizes[1:len(runtimes)]
    y = ratios 
    scatter(x,y,color=plotcolor)
    xscale('log')
    xlabel('size of instance')
    ylabel('ratio of runtimes')


def plot_runtimes(sizes, runtimes):

    x = sizes[0:len(runtimes)]
    y = runtimes
    scatter(x,y)
    xscale('log')
    xlabel('size of instance')
    ylabel('ratio of runtimes')
