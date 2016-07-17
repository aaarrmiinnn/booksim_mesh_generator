
# coding: utf-8

# In[5]:

import numpy as np
import sys
from scipy.spatial.distance import pdist, squareform


# In[12]:

#X_size = 8
#Y_size = 8
#custom_connections = [4,23,62,3]
#custom_connections_sources = custom_connections[0::2]
#custom_connections_destinations = custom_connections[1::2]
#name = 'crap'


# In[13]:

def mesh_creator(NX,NY):
    X, Y = np.meshgrid(range(1,NX+1), range(1,NY+1))
    X = np.asarray(X.T.ravel())
    Y = np.asarray(Y.T.ravel())
    concat_XY = np.reshape(np.concatenate((X,Y), axis=0), (2, X.size))
    adjacency_matrix = squareform(pdist(concat_XY.T,'cityblock')==1)
    
    return adjacency_matrix


# In[ ]:




# In[14]:

try:
    X_size = int(sys.argv[1])
    Y_size = int(sys.argv[2])
    name = sys.argv[3]
    custom_connections = sys.argv[4:]
    if (len(custom_connections)%2==1):
        print("You entered Odd number of custome connections! Shame on you.")
        sys.exit(1)
    custom_connections_sources = custom_connections[0::2]
    custom_connections_destinations = custom_connections[1::2]
except ValueError as e:
    print("You didn't enter a number! Shame on you.")
    sys.exit(1)
print("All done!")
print (custom_connections_sources)
print (custom_connections_destinations)


# In[15]:
delayy = 3
adj_matrix = mesh_creator(X_size,Y_size)
node_count = adj_matrix.shape[0]


# In[16]:

with open('%s.nwk' % name, 'wb') as f:
    for i in range(1,node_count+1):
        adjacent_routers = np.where(adj_matrix[i-1,])
        adjacent_router_list = (np.asarray(adjacent_routers)).tolist()
        f.write('router %i node %i '%(i-1,i-1))
        if str(i-1) in custom_connections_sources:
            print i-1
            temp = custom_connections_destinations[(custom_connections_sources.index(str(int(i)-1)))]
            #print ("found %i and %i"%i,temp)
            f.write('router %s %s '%(temp,delayy))
            
        for j in adjacent_router_list[0]:
                    f.write('router %i '%j)
            
        f.write('\n')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



