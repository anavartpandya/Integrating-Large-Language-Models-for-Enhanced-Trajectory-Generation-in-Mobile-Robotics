import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt

r = 1
t = np.linspace(0,1,1000)
x = r*cos(2*np.pi*t)
y = r*sin(2*np.pi*t)

# Plot the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 1, 1)
plt.plot(x, y, label='Desired Traj')
plt.title('y vs. x')
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.show()

letter_used = ['a','b','c','d','e','f','g','h','i','j']
encode_dict = {}
decode_dict = {}
for i in range(10):
    encode_dict[i] = letter_used[i]
    decode_dict[letter_used[i]] = i

def Inverse_Kinematics(pxa,pxd):
    phi = np.arctan2(pxd[1]-pxa[1],pxd[0]-pxa[0])
    v = ((pxd[1] - pxa[1])**2 + (pxd[0] - pxa[0])**2)**0.5
    return [v,phi]

def Forward_Kinematics(pxa,v,phi_a):
    return [pxa[0]+v*cos(phi_a), pxa[1]+v*sin(phi_a)]

def convert(A,flag):
    A  = format(A, '.2f')
    A = A.replace(".","")
    if len(A) == 4:
        A = [int(A[0]),int(A[1]),int(A[2]),int(A[3])]
    elif len(A) == 3 and flag == True:
        A = [0,int(A[0]),int(A[1]),int(A[2])]
    else:
        A = [int(A[0]),int(A[1]),int(A[2])]
    return A

def encode(v,phi):
    sign = 0
    v = np.round(v,2)
    if phi<0:
        sign = 1
    phi = abs(phi)
    phi = np.round(phi,2)
    v = convert(v,True)
    phi = convert(phi,False)
    encoded_string = ""
    for i in range(4):
        encoded_string += encode_dict[v[i]]
    if sign == 0:
        encoded_string += "@"
    else:
        encoded_string += "$"
    for i in range(3):
        encoded_string += encode_dict[phi[i]]
    return encoded_string

    
[xa_,ya_] = [x[0],y[0]]
str_ = ""
V_ = [] 
PHI_ = []
for i in range(1,len(x)):
    v_,phi_ = Inverse_Kinematics([xa_,ya_],[x[i],y[i]])
    V_.append(v_)
    PHI_.append(phi_)

    str_ += encode(v_,phi_) + "#"
# print(str_)
print(PHI_)
with open('generated_traj.txt', 'w') as file:
    file.write(str_)