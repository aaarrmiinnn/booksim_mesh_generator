
# coding: utf-8

# In[1]:

import os


# In[2]:

#cwd = os.getcwd()
result_dir = os.getcwd()+"/results"
print result_dir
result_file = []
for item in (os.listdir(result_dir)):
    print item
    if item.endswith(".rslt"):
        result_file.append(item)


# In[3]:

result_file


# In[6]:


latency = []
for result in result_file:
    flag = 0
    with open("./results/"+result,'r') as f:
        for i,line in enumerate(f):
            if flag==0:
                if "====== Overall Traffic Statistics ======" in line:
                    print "Fount it on:"+ str(i)
                    start_line = i
                    flag = 1
            else:
                if "Network latency average" in line:
                    latency.append((("File Name: "+ result+","+line.split()[4])))
with open("./results/overall_results.txt", 'wr') as fp:
    for item in latency:
        fp.write(item+"\n")


# In[ ]:




# In[ ]:



