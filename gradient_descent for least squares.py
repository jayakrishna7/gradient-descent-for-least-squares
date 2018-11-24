import sys
import random

##read data file
f1 = sys.argv[1]
file= open(f1)

data = []
i = 0
l = f1.readline()

while(l != '') : #read
    a = l.split()
    b = len(a)
    l2 = []
    for j in range(0, b, 1):
        l2.append(float(a[j]))
        if j == (b-1) :
            l2.append(float(1))
        #data.append(l2)

    data.append(l2)
    l = f1.readline()

rows = len(data)
cols = len(data[0])

f1.close()
#--------------------------------------------------------------
##read label data
f2 = sys.argv[2]
file=open(f2)

trainlabels = {}
n = []
n.append(0)
n.append(0)

l = f2.readline()
while(l != '') : #read

    a = l.split()
    if int(a[0]) == 0:
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f2.readline()
    n[int(a[0])] += 1

##print(trainlabels)
#print(trainlabels)

##initialize w
w = []

for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01
#    w[j] = 1

##define function dot_product
def dp(list1, list2):
    dp = 0
    refw = list1
    refx = list2
    for j in range (cols):
        dp += refw[j] * refx[j]
    return dp


##gradient descent iteration
eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        error += ( -trainlabels.get(i) + dp(w,data[i]) )**2

#initialize flag and iteration parameters
flag = 0
k=0

while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)

    for i in range(rows):
        if(trainlabels.get(i) != None):
            d_p = dp(w, data[i])
            for j in range (cols):
#compute gradient
                delf[j] += (-trainlabels.get(i) + d_p) * data[i][j]
bestobj = 1000000000000
for k in range(0, len(eta_list), 1):

    eta = eta_list[k]

    ##update w
    ##insert code here for w = w + eta*dellf

    ##get new error
    error = 0
    for i in range(0, rows, 1):
        if (trainlabels.get(i) != None):
    ##update error
    ##insert code to update the loss (which we call error here)

    obj = error

    ##update bestobj and best_eta
    ##insert code here

    ##remove the eta for the next
    ##insert code here for w = w - eta*dellf

eta = best_eta

##update
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    curr_error = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            curr_error += ( -trainlabels.get(i) + dp(w,data[i]) )**2
    print(error,k)
    if error - curr_error < 0.001:
        flag = 1
    error = curr_error

### print error
## calculate differences in error:

#print("count",k)
#print("w =",w)

normw = 0
for j in range((cols-1)):
    normw += w[j]**2
    print(w[j])

normw = (normw)**0.5
print("||w||=", normw)

d_origin = w[(len(w)-1)] / normw


for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p = dp(w, data[i])
        if(d_p > 0):
            print("1",i)
        else:
            print("0",i)




