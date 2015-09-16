import sys
from math import log

class udpr:
    def __init__(self,seed,k,m):
        self.seed,self.k,self.m=seed,k,m
    def generate_udpr(self):
        self.seed=(self.seed*self.k)%self.m
        return (self.seed/self.m)

class edpr:
    def __init__(self,lam,seed,k,m):
        self.lam,self.rand=lam,udpr(seed,k,m)
    def generate_expr(self):
        return (log(self.rand.generate_udpr())/-self.lam)

class experiment:
    def __init__(self,seed,k,m,q):
        self.rand=udpr(seed,k,m)
	self.q=q
    def run(self,times):
        mean,var=0,0
        for i in range(0,times):
	    timesdone,seen,done=0,-1,0
	    while(not done):
	        x=self.rand.generate_udpr()
                timesdone += 1
                if(x < self.q):
                    if(seen==1):
                        done=1
                    else:
                        seen=1
                else:
                    if(seen==0):
                        done=1
                    else:
                        seen=0
            mean += timesdone
            var += timesdone*timesdone
        mean=mean/(times*1.0)
        print "'\nCoin Toss mean is:",mean
	print "Coin Toss variance is:",(var/(times*1.0) - mean*mean)
	print "Coin Toss mean theoretically is:", ((-self.q* self.q +  self.q + 2)/( self.q* self.q*1.0 -  self.q +1))
	print "Coin Toss Variance theoretically  is:", (5* self.q*(1- self.q)-2* self.q*self.q*(1- self.q)*(1- self.q))/((1- self.q*(1- self.q))*(1- self.q*(1- self.q)))

if __name__ == "__main__":
    if (len(sys.argv) != 6):
        print "arguments not proper"
        sys.exit(0)
    seed,k,m,mean,var,interval,lam,q=float(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),0,0,[0]*10,int(sys.argv[4]),float(sys.argv[5])
    random=udpr(seed,k,m)
    for i in range(0,10000):
        val= random.generate_udpr()
        interval[int(10*val)] +=  1	
        mean = mean+val 
        var = var + val*val
    mean=mean/10000
    print "'\nFor Uniformly Distributed Pseudo Radom numbers using Multiplicative congruential method"
    print "Mean value is:",mean
    print "Variance value is:",(var/10000 - mean*mean)
    print "Interval as follows"
    for i in range(0,10):
        print "[0.",i,"- 0.",i+1,"]:",interval[i]
    randome=edpr(lam,seed,k,m)
    mean,var=0,0
    for i in range(0,10000):
        val= randome.generate_expr()
        mean += val
	var=var + val*val
    mean=mean/10000
    print "'\nFor Exponentially Distributed Pseudo Radom numbers"
    print "Mean value by simulation:",mean
    print "Variance Value by simulation:",(var/10000 - mean*mean)
    print "Theoretical value of Mean:",(1/(lam*1.0))
    print "Theoretical value of variance:",(1/(lam*lam*1.0))
    toss=experiment(seed,k,m,q)
    toss.run(1000)

