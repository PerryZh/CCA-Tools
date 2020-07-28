from pm4py.objects.petri.reachability_graph import construct_reachability_graph
from pm4py.visualization.transition_system import visualizer as ts_visualizer
from pm4py.objects.petri import semantics
from pm4py.objects.petri.petrinet import PetriNet, Marking
from trans_pathfinding import trans_path
import rp_mat_calc as rp
import relation as rl

net = PetriNet("new_petri_net")

# creating places
p1 = PetriNet.Place("p1")
p2 = PetriNet.Place("p2")
p3 = PetriNet.Place("p3")

# add the places to the Petri Net
net.places.add(p1)
net.places.add(p2)
net.places.add(p3)

# Create transitions
t_a = PetriNet.Transition("A", "A")
t_b = PetriNet.Transition("B", "B")
t3 = PetriNet.Transition("name3", "t3")
t4 = PetriNet.Transition("name4", "t4")

# Add the transitions to the Petri Net
net.transitions.add(t_a)
net.transitions.add(t_b)
net.transitions.add(t3)
net.transitions.add(t4)

# Add arcs
from pm4py.objects.petri import utils
utils.add_arc_from_to(p1, t_a, net)
utils.add_arc_from_to(p1, t3, net)
utils.add_arc_from_to(t_a, p2, net)
utils.add_arc_from_to(p2, t4, net)
utils.add_arc_from_to(p2, t_b, net)
utils.add_arc_from_to(t_b, p3, net)
utils.add_arc_from_to(t3, p3, net)
utils.add_arc_from_to(t4, p3, net)

# Adding tokens
initial_marking = Marking()
initial_marking[p1] = 1

# Get triggern transitions
# ini_transitions = semantics.enabled_transitions(net, initial_marking)

# Show Petri Net
from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking)
pn_visualizer.view(gviz)

# Show Reachability Graph
reachab_graph = construct_reachability_graph(net, initial_marking)
viz = ts_visualizer.apply(reachab_graph, parameters={"show_labels": True, "show_names": True})
ts_visualizer.view(viz)


print(trans_path(t_a, t_b, net, initial_marking))
print(rp.trans_relation_analysis(t_a, t_b, net, initial_marking))