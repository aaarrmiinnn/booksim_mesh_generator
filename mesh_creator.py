
# coding: utf-8

# In[1]:

import numpy as np
import sys
from scipy.spatial.distance import pdist, squareform


# In[2]:

def mesh_creator(NX,NY):
    X, Y = np.meshgrid(range(1,NX+1), range(1,NY+1))
    X = np.asarray(X.T.ravel())
    Y = np.asarray(Y.T.ravel())
    concat_XY = np.reshape(np.concatenate((X,Y), axis=0), (2, X.size))
    adjacency_matrix = squareform(pdist(concat_XY.T,'cityblock')==1)
    
    return adjacency_matrix


# In[3]:

try:
    X_size = int(sys.argv[1])
    Y_size = int(sys.argv[2])
    name = sys.argv[3]
except ValueError as e:
    print("You didn't enter a number! Shame on you.")
    sys.exit(1)
print("All done!")


# In[4]:




# In[5]:

adj_matrix = mesh_creator(X_size,Y_size)
node_count = adj_matrix.shape[0]


# In[7]:

with open('%s.nwk' % name, 'wb') as f:
    
    for i in range(1,node_count+1):
        adjacent_routers = np.where(adj_matrix[i-1,])
        adjacent_router_list = (np.asarray(adjacent_routers)).tolist()
        f.write('router %i node %i '%(i-1,i-1))
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



