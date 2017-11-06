# python3

import numpy as np

def dis_point_line(p, l):
    A = np.array( p )
    B = np.array( l )
    # The distance from point A and line B
    # line B has limited length with two fixed end-points
    a = B[0]
    b = B[1]
    ba = a-b
    bA = A-b
    d = np.linalg.norm(np.cross(ba,bA))/np.linalg.norm(ba)
    if (np.dot(ba, bA) > 0) & (np.dot( (b-a), bA ) > 0):
        return np.min( [np.linalg.norm(A-B[0]), np.linalg.norm(A-B[1]), d] )
    else:
        return np.min( [np.linalg.norm(A-B[0]), np.linalg.norm(A-B[1])] )
    
# demo:
# dis_point_line(l=[[2,3,4],[3,4,5]], p=[1,2,3])



def dis_point_curve(p, c):
    
    A = np.array( p )
    B = np.array( c )
    # the closest distance between point A and curve B
    # curve B is described by 10 points.
    
    # NOTICE: when the curve is too winding, there might be some problems.
    # because we only consider the two points within B which are most close to point A
    
    C = []
    
    i_min = np.argmin( np.linalg.norm( B-A, axis = 1 ) )    
    C.append( B[i_min] )
    # B = np.delete(B,i_min,axis=0) # will make error
    B2 = np.delete(B,i_min,axis=0)
    
    i_min = np.argmin( np.linalg.norm( B2-A, axis = 1 ) )    
    C.append( B2[i_min] )
        
    return dis_point_line(p=A, l=np.array( C ))

# demo:
# A = [1,2,3]
# B = np.random.rand( 10,3 )*10
# dis_point_curve(p=A, c=B)