from pm4py.objects.petri.petrinet import *
import numpy as np


def p_mat_cal(N1: PetriNet, N2: PetriNet, Corr_map: set):
    # This function only calc transitions labeld not like 't1', 't2' and 't'+number form;
    trans_set1 = set()
    for t in N1.transitions:
        t_name = t.name if t.label == None else t.label
        if 't' not in t_name:
            trans_set1.add(t)

    trans_set2 = set()
    for t in N2.transitions:
        t_name = t.name if t.label == None else t.label
        if 't' not in t_name:
            trans_set2.add(t)

    # Get the number of transaction in WorkflowNet N1, N2
    n1 = len(trans_set1)
    n2 = len(trans_set2)

    N1_trans = sorted(list(trans_set1), key=lambda x: x.label)
    N2_trans = sorted(list(trans_set2), key=lambda x: x.label)

    # Initialize P-Matrix as 0s
    p1_mat = np.asmatrix(np.zeros((n1, n2)))
    p2_mat = np.asmatrix(np.zeros((n2, n1)))

    for i in range(n1):
        for j in range(n2):
            c = trans_map(N1_trans[i], N2_trans[j], Corr_map)
            if c:
                p1_mat[i, j] = 1

    for k in range(n2):
        for l in range(n1):
            c2 = inver_trans_map(N2_trans[k], N1_trans[l], Corr_map)
            if c2:
                p2_mat[k, l] = 1

    return p1_mat, p2_mat


# Calculate the map of t1 in t2
def trans_map(t1: PetriNet.Transition, t2: PetriNet.Transition, corr_map):
    # return true of false
    t1_name = t1.name if t1.label == None else t1.label
    t2_name = t2.name if t2.label == None else t2.label

    y = False

    for key, value in corr_map.items():
        if (t1_name in key) and (t2_name in value):
            y = True
            break
    return y


# Calculate the map of t2 in t1
def inver_trans_map(t1: PetriNet.Transition, t2: PetriNet.Transition, corr_map):
    # return true of false
    t1_name = t1.name if t1.label == None else t1.label
    t2_name = t2.name if t2.label == None else t2.label

    y = False

    for key, value in corr_map.items():
        if (t2_name in key) and (t1_name in value):
            y = True
            break
    return y
