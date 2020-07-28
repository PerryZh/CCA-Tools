import numpy as np

def sim_cal(rp_mat1, rp_mat2, p_mat1, p_mat2):
    #Get the size of matrix for each Workflow Net
    n1 = rp_mat1.shape[0]
    n2 = rp_mat2.shape[0]

    # Compute intermediate matrix for each Workflow Net
    inter_mat1 = np.dot(rp_mat1,p_mat1)
    inter_mat2 = np.dot(rp_mat2,p_mat2)

    if n1 != n2:
        # inter_mat1 has the same size of inter_mat2' transposition
        inter_mat2 = inter_mat2.transpose()
    
    diff_count = 0
    for i in range(n1):
        for j in range(n2):
            if inter_mat1[i,j] != inter_mat2[i,j]:
                diff_count += 2

    return 1 - diff_count/(rp_mat1.size + rp_mat2.size)
