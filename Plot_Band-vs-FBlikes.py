import matplotlib.pyplot as plt
import numpy as np
import math
import os, csv

script_dir = os.path.dirname(__file__) # abs path of script

fname2 = 'FBlikes'
abspath_fblikes = script_dir + '/' + fname2 + '.csv'

Band_data = []
with open(abspath_fblikes) as csv_data: # reading bands and debut years
    csvReader = csv.reader(csv_data)
    for row in csvReader:
        Band_data.append(row)

csv_data.close()

for i in range(len(Band_data)):    # sort bands as ascending years
    for j in range(len(Band_data)-1):
        if int(Band_data[j][1]) > int(Band_data[j+1][1]):
            Band_data[j], Band_data[j+1] = Band_data[j+1], Band_data[j]
            
bname=[]
bfl = []
bflstr = []
b10s=[]

for aa in Band_data:
    bname.append(aa[0])
    bfl.append(int(aa[2]))
    bflstr.append(str(round(int(aa[2]) / 1e6,1))+'M')
    b10s.append(str(math.floor(int(aa[1])/10.0)*10))
    
csfont = {'fontname':'STHeiti'}

# y labels
y = np.arange(len(bname))
plt.rcdefaults()
fig, ax = plt.subplots()
ax.set_yticks(y)
ax.set_yticklabels(bname, **csfont, fontsize='16')
ax.invert_yaxis()  


# x labels
xtic = []
xtex = []
for i in range(0, int(4e7+10), int(5e6)):
    xtic.append(i)
    xtex.append(str(int(i/ 1e6))+'M')  # x label in millions
ax.set_xlim((0, 4.5e7))
    

ax.set_xlabel('Facebook likes', fontsize='18')
ax.set_title('Bands with debut album before 2000 and still widely liked nowadays \n (More than 10 million Facebook likes)' , \
             fontsize='20', fontweight='bold')


fig.set_size_inches(18.5, 10.5, forward=True)
ax.xaxis.grid(linestyle='--')
plt.xticks(xtic, xtex, fontsize='14')

ax.barh(y, bfl, align='center',
        color='blue', ecolor='black' , alpha=0.5)


bhr = [[0, b10s[0]]]   # 1960s, 1970s, ...
for i in range(1, len(b10s)):
    if b10s[i] != b10s[i-1]:
        bhr.append([i, b10s[i]])
for i in range(len(bhr)):
    plt.axhline(y=bhr[i][0]-0.5, color='r', linestyle='-.')
    ax.text(4.25e7, bhr[i][0]+0.3, bhr[i][1]+'s', color='black',\
            fontweight='bold', alpha=0.5, fontsize='16', **csfont)

for i, v in enumerate(y):  # FB likes text
    ax.text(bfl[v]-2.2e6, i + .25, bflstr[v], color='black', \
            fontweight='bold', fontsize='14')

bottom = max(y)
ax.text(3.5e7, bottom+3, 'github.com/deniseycchang/Band-vs-FBlikes')

plt.subplots_adjust(left=0.15)

filename = script_dir + '/Band_FBlikes.png'
fig.savefig(filename)


plt.show()


## github.com/deniseycchang/Band-vs-FBlikes

        