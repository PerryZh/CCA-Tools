from pm4py.objects.transition_system.transition_system import *
from pm4py.objects.petri.petrinet import *
from pm4py.objects.petri.reachability_graph import construct_reachability_graph
from pm4py.objects.petri import semantics

# storing all the paths
all_path = []

def trans_path(t1:PetriNet.Transition, t2: PetriNet.Transition, net: PetriNet, initial_marking: Marking, iter=3):
    multi_path = set()
    while iter >= 1:
        multi_path = multi_path.union(trans_path_util(t1, t2, net, initial_marking))
        iter -= 1
    return multi_path


# def trans_path_utin(t1:PetriNet.Transition, t2: PetriNet.Transition, net: PetriNet, initial_marking: Marking, ini_transitions: PetriNet.Transition):
def trans_path_util(t1:PetriNet.Transition, t2: PetriNet.Transition, net: PetriNet, initial_marking: Marking):
    all_path.clear()
    reachab_graph = construct_reachability_graph(net, initial_marking)
    # find = False
    t1_name = t1.name if t1.label == None else t1.label
    t2_name = t2.name if t2.label == None else t2.label

    # Trigger transitions
    transitions = semantics.enabled_transitions(net, initial_marking)

    for tran1 in reachab_graph.transitions:
        if tran1.name == t1_name:
            for tran2 in reachab_graph.transitions:
                if tran2.name == t2_name:
                    for itran in reachab_graph.transitions:
                        for intran in transitions:
                            intran_name = intran.name if intran.label == None else intran.label
                            if itran.name == intran_name:
                                path_finding(itran, tran2, reachab_graph)
                                path_finding(itran, tran1, reachab_graph)
                else:
                    pass
        else:
            pass
    
    set_all_path = set(all_path)
    temp = list(set_all_path)
    for i in temp:
        if (t1_name not in i) or (t2_name not in i):
            set_all_path.remove(i)

    all_long_path = set()
    for path in set_all_path:
        pathIn = True
        for others in set_all_path - set([path]):
            if others.find(path) > -1:
                pathIn = False
        if pathIn:
            all_long_path.add(path)
            
    return all_long_path


def path_finding(t1:TransitionSystem.Transition, t2:TransitionSystem.Transition, graph: TransitionSystem):
    path = []
    visited = dict()
    for tran in graph.transitions:
        visited[tran] = False
    return path_finding_util(t1, t2, visited, path, graph)


def path_finding_util(t1:TransitionSystem.Transition, t2:TransitionSystem.Transition, visited:dict, path:list, graph: TransitionSystem):
    visited[t1] = True
    path.append(t1)
    find = False

    if t1 == t2:
        # print(path)
        # all_path.append(list(map(str,path)))
        if len(path) >= 2:
            all_path.append(str(path).strip('[]'))
            find = True
    else:
        state = t1.to_state
        if len(state.outgoing) > 0:
            for tran in state.outgoing:
                if visited[tran] == False:
                    find = path_finding_util(tran, t2, visited, path, graph)
    path.pop()
    visited[t1] = False
    return find



# reference
# [1] https://www.geeksforgeeks.org/find-paths-given-source-destination/