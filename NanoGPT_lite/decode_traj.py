import numpy as np
import matplotlib.pyplot as plt

with open('predicted_traj.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = text[:len(text)-1]


letter_used = ['a','b','c','d','e','f','g','h','i','j']
encode_dict = {}
decode_dict = {}
for i in range(10):
    encode_dict[i] = letter_used[i]
    decode_dict[letter_used[i]] = i

broken_text = []
V = []
PHI = []

for i in range(len(text)//9):
    broken_text.append(text[9*i:9*i+9])
count = 1
for i in broken_text:
    try:
        v = 10*decode_dict[i[1]] + decode_dict[i[2]] + 0.1*decode_dict[i[3]] + 0.01*decode_dict[i[4]]
        v = np.round(v,2)
        V.append(v)
    except:
        V.append(V[-1])
    try:
        phi = decode_dict[i[6]] + 0.1*decode_dict[i[7]] + 0.01*decode_dict[i[8]]
        phi = np.round(phi,2)
        if i[5] == "@":
            phi = phi
        elif i[5] == "$":
            phi = -phi
        PHI.append(phi)
    except:
        PHI.append(PHI[-1])
    count += 1

def Forward_Kinematics(pxa,v,phi_a):
    return [pxa[0]+v*np.cos(phi_a), pxa[1]+v*np.sin(phi_a)]
    

x = 0
y = 0
X = [x]
Y = [y]
for i in range(len(V)):
    x,y = Forward_Kinematics([x,y],V[i],PHI[i])
    X.append(x)
    Y.append(y)
t = np.linspace(0,1,len(X))

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(X, Y, label='Predicted xy Traj')
plt.title('y vs. x')
plt.axis('equal')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(t, X, label='Predicted x Traj')
plt.title('x vs. t')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(t, Y, label='Predicted y Traj')
plt.title('y vs. t')
plt.legend()

plt.tight_layout()
plt.show()

