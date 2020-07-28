from pm4py.objects.petri.petrinet import *
import relation as rl
import numpy as np
from trans_pathfinding import trans_path

def rp_mat_cal(N: PetriNet, M:Marking):
    # This function only calc transitions labeld not like 't1', 't2' and 't'+number form;
    trans_set = set()
    for t in N.transitions:
        t_name = t.name if t.label == None else t.label
        if 't' not in t_name:
            trans_set.add(t)

    # Get the number of transitions in WorkflowNet N
    n = len(trans_set)

    # Initialize RP-Matrix as 0s
    rp_mat = np.asmatrix(np.zeros((n,n)))

    # I Relation Array
    rel = list(rl.relation_dict.keys())

    N_trans = sorted(list(trans_set), key = lambda x: x.label)

    for i in range(n):
        for j in range(i,n):
            if j==i:
                # Diagonal element, i.e., Self-Relation
                self_relation = selfrelation_analysis(N_trans[j], N, M)
                if self_relation in rel:
                    rp_mat[j,j] = self_relation
            else:
                # Upper triangular element relation, BM is a symmetric matrix except one situation
                inter_relation = trans_relation_analysis(N_trans[i],N_trans[j], N, M)
                if inter_relation in rel:
                    if rl.relation_dict[inter_relation] not in ["right arrow", "inverse right arrow"]:
                        rp_mat[i,j] = rp_mat[j,i] = inter_relation
                    else:
                        if rl.relation_dict[inter_relation] == "right arrow":
                            rp_mat[i,j] = inter_relation
                            for key,value in rl.relation_dict.items():
                                if value == "inverse right arrow":
                                    rp_mat[j,i] = key
                        elif rl.relation_dict[inter_relation] == "inverse right arrow":
                            rp_mat[i,j] = inter_relation
                            for key,value in rl.relation_dict.items():
                                if value == "right arrow":
                                    rp_mat[j,i] = key
    return rp_mat
                        

# return relation key
def selfrelation_analysis(t:PetriNet.Transition,net: PetriNet, initial_marking: Marking):
    return trans_relation_analysis(t, t, net, initial_marking)
    

# return relation key
def trans_relation_analysis(t1:PetriNet.Transition, t2:PetriNet.Transition, net: PetriNet, initial_marking: Marking):
    t1_name = t1.name if t1.label == None else t1.label
    t2_name = t2.name if t2.label == None else t2.label
    satisified_relation = list()

    pattern = rl.relation_pattern(t1_name, t2_name)
    the_all_path = trans_path(t1, t2, net, initial_marking)

    if len(the_all_path) == 0:
        # reuturn plus relation key
        return 2
    else:
        ana_relation = dict()
        for key,value in rl.relation_dict.items():
            x2y = y2x = 0
            x2y_prime = y2x_prime = 0

            for path in the_all_path:
                x2y_prime, y2x_prime  = pattern.get_pattern(value, path)
                x2y += x2y_prime
                y2x += y2x_prime
            
            # print(value, x2y,y2x)
            
            if value == 'right arrow':
                if x2y >= 1 and y2x == 0:
                    satisified_relation.append(key)
            if value == 'plus':
                if y2x == 0 and x2y == 0:
                    satisified_relation.append(key)
            if value == 'parallel 1':
                if y2x >= 1 and x2y >= 1:
                    satisified_relation.append(key)
            if value == 'parallel 2':
                if y2x >= 1 and x2y >= 1:
                    satisified_relation.append(key)
            if value == 'parallel 3':
                if x2y ^ y2x:
                    satisified_relation.append(key)
            if value == 'parallel 4':
                if x2y ^ y2x:
                    satisified_relation.append(key)
            if value == 'parallel 5':
                if x2y > 1:
                    satisified_relation.append(key)
            if value == 'parallel 6':
                if x2y == 1:
                    satisified_relation.append(key)
            if value == 'inverse right arrow':
                if y2x >= 1 and x2y == 0:
                    satisified_relation.append(key)

        if len(satisified_relation) > 1:
            # print("Relation Overlay!")
            return satisified_relation
        elif len(satisified_relation) == 0:
            # print("Not Find Relation!")
            return None
        else:
            return satisified_relation[0]
