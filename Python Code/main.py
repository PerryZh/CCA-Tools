from pm4py.objects.petri.reachability_graph import construct_reachability_graph
from pm4py.visualization.transition_system import visualizer as ts_visualizer
from pm4py.visualization.petrinet import visualizer as pn_visualizer
from pm4py.objects.petri import semantics
from pm4py.objects.petri.petrinet import PetriNet, Marking
from pm4py.objects.petri import utils
from trans_pathfinding import trans_path
import relation as rl
import rp_mat_calc as rp
import p_mat_calc as pmap
import corresponding as corr
import sim_computing as sim

# Net 1
net1 = PetriNet("petri_net1")
# creating places
p11 = PetriNet.Place("p1")
p12 = PetriNet.Place("p2")
p13 = PetriNet.Place("p3")
p14 = PetriNet.Place("p4")
# add the places to the Petri Net
net1.places.add(p11)
net1.places.add(p12)
net1.places.add(p13)
net1.places.add(p14)
# Create transitions
t1_a1 = PetriNet.Transition("A1", "A1")
t1_b1 = PetriNet.Transition("B1", "B1")
t1_c1 = PetriNet.Transition("C1", "C1")
# Add the transitions to the Petri Net
net1.transitions.add(t1_a1)
net1.transitions.add(t1_b1)
net1.transitions.add(t1_c1)
# Add arcs
utils.add_arc_from_to(p11, t1_a1, net1)
utils.add_arc_from_to(t1_a1, p12, net1)
utils.add_arc_from_to(p12, t1_b1, net1)
utils.add_arc_from_to(t1_b1, p13, net1)
utils.add_arc_from_to(p13, t1_c1, net1)
utils.add_arc_from_to(t1_c1, p14, net1)
# Adding tokens
initial_marking1 = Marking()
initial_marking1[p11] = 1

# Net 2
net2 = PetriNet("petri_net2")
# creating places
p21 = PetriNet.Place("p1")
p22 = PetriNet.Place("p2")
p23 = PetriNet.Place("p3")
p24 = PetriNet.Place("p4")
# add the places to the Petri Net
net2.places.add(p21)
net2.places.add(p22)
net2.places.add(p23)
net2.places.add(p24)
# Create transitions
t2_ab1 = PetriNet.Transition("AB1", "AB1")
t2_ab2 = PetriNet.Transition("AB2", "AB2")
t2_c1 = PetriNet.Transition("C1", "C1")
# Add the transitions to the Petri Net
net2.transitions.add(t2_ab1)
net2.transitions.add(t2_ab2)
net2.transitions.add(t2_c1)
# Add arcs
utils.add_arc_from_to(p21, t2_ab1, net2)
utils.add_arc_from_to(t2_ab1, p22, net2)
utils.add_arc_from_to(p22, t2_ab2, net2)
utils.add_arc_from_to(t2_ab2, p23, net2)
utils.add_arc_from_to(p23, t2_c1, net2)
utils.add_arc_from_to(t2_c1, p24, net2)
# Adding tokens
initial_marking2 = Marking()
initial_marking2[p21] = 1

# Net 3
net3 = PetriNet("petri_net3")
# creating places
p31 = PetriNet.Place("p1")
p32 = PetriNet.Place("p2")
p33 = PetriNet.Place("p3")
p34 = PetriNet.Place("p4")
p35 = PetriNet.Place("p5")
p36 = PetriNet.Place("p6")
p37 = PetriNet.Place("p7")
p38 = PetriNet.Place("p8")
p39 = PetriNet.Place("p9")
# add the places to the Petri Net
net3.places.add(p31)
net3.places.add(p32)
net3.places.add(p33)
net3.places.add(p34)
net3.places.add(p35)
net3.places.add(p36)
net3.places.add(p37)
net3.places.add(p38)
net3.places.add(p39)
# Create transitions
t3_a1 = PetriNet.Transition("A1", "A1")
t3_b1 = PetriNet.Transition("B1", "B1")
t3_b2 = PetriNet.Transition("B2", "B2")
t3_c1 = PetriNet.Transition("C1", "C1")
t3_1 = PetriNet.Transition("t1", "t1")
t3_2 = PetriNet.Transition("t2", "t2")
t3_3 = PetriNet.Transition("t3", "t3")
# Add the transitions to the Petri Net
net3.transitions.add(t3_a1)
net3.transitions.add(t3_b1)
net3.transitions.add(t3_b2)
net3.transitions.add(t3_c1)
net3.transitions.add(t3_1)
net3.transitions.add(t3_2)
net3.transitions.add(t3_3)
# Add arcs
utils.add_arc_from_to(p31, t3_a1, net3)
utils.add_arc_from_to(t3_a1, p32, net3)
utils.add_arc_from_to(t3_a1, p33, net3)
utils.add_arc_from_to(t3_a1, p34, net3)
utils.add_arc_from_to(p32, t3_1, net3)
utils.add_arc_from_to(t3_1, p34, net3)
utils.add_arc_from_to(p34, t3_b1, net3)
utils.add_arc_from_to(t3_b1, p36, net3)
utils.add_arc_from_to(p36, t3_c1, net3)
utils.add_arc_from_to(p36, t3_3, net3)
utils.add_arc_from_to(p33, t3_2, net3)
utils.add_arc_from_to(t3_2, p35, net3)
utils.add_arc_from_to(p35, t3_b2, net3)
utils.add_arc_from_to(t3_b2, p37, net3)
utils.add_arc_from_to(p37, t3_c1, net3)
utils.add_arc_from_to(t3_c1, p38, net3)
utils.add_arc_from_to(p38, t3_3, net3)
utils.add_arc_from_to(t3_3, p39, net3)
# Adding tokens
initial_marking3 = Marking()
initial_marking3[p31] = 1

# Net 4
net4 = PetriNet("petri_net4")
# creating places
p41 = PetriNet.Place("p1")
p42 = PetriNet.Place("p2")
p43 = PetriNet.Place("p3")
p44 = PetriNet.Place("p4")
p45 = PetriNet.Place("p5")
p46 = PetriNet.Place("p6")
p47 = PetriNet.Place("p7")
p48 = PetriNet.Place("p8")
p49 = PetriNet.Place("p9")
# add the places to the Petri Net
net4.places.add(p41)
net4.places.add(p42)
net4.places.add(p43)
net4.places.add(p44)
net4.places.add(p45)
net4.places.add(p46)
net4.places.add(p47)
net4.places.add(p48)
net4.places.add(p49)
# Create transitions
t4_a2 = PetriNet.Transition("A2", "A2")
t4_bc1 = PetriNet.Transition("BC1", "BC1")
t4_bc2 = PetriNet.Transition("BC2", "BC2")
t4_1 = PetriNet.Transition("t1", "t1")
t4_2 = PetriNet.Transition("t2", "t2")
t4_3 = PetriNet.Transition("t3", "t3")
# Add the transitions to the Petri Net
net4.transitions.add(t4_a2)
net4.transitions.add(t4_bc1)
net4.transitions.add(t4_bc2)
net4.transitions.add(t4_1)
net4.transitions.add(t4_2)
net4.transitions.add(t4_3)
# Add arcs
utils.add_arc_from_to(p41, t4_a2, net4)
utils.add_arc_from_to(t4_a2, p42, net4)
utils.add_arc_from_to(t4_a2, p43, net4)
utils.add_arc_from_to(p42, t4_1, net4)
utils.add_arc_from_to(p43, t4_2, net4)
utils.add_arc_from_to(t4_1, p44, net4)
utils.add_arc_from_to(t4_1, p45, net4)
utils.add_arc_from_to(t4_2, p45, net4)
utils.add_arc_from_to(t4_2, p46, net4)
utils.add_arc_from_to(p44, t4_bc2, net4)
utils.add_arc_from_to(p45, t4_bc1, net4)
utils.add_arc_from_to(p46, t4_bc2, net4)
utils.add_arc_from_to(t4_bc1, p47, net4)
utils.add_arc_from_to(p47, t4_bc2, net4)
utils.add_arc_from_to(t4_bc2, p48, net4)
utils.add_arc_from_to(p48, t4_3, net4)
utils.add_arc_from_to(t4_3, p49, net4)
# Adding tokens
initial_marking4 = Marking()
initial_marking4[p41] = 1

# # # Show Petri Net
gviz = pn_visualizer.apply(net2, initial_marking2)
pn_visualizer.view(gviz)

# Show Reachability Graph
# reachab_graph = construct_reachability_graph(net4, initial_marking4)
# viz = ts_visualizer.apply(reachab_graph, parameters={"show_labels": True, "show_names": True})
# ts_visualizer.view(viz)


# print(trans_path(t4_bc1, t4_bc2, net4, initial_marking4,1))
# print(rp.trans_relation_analysis(t_a, t3, net, initial_marking))˜
# print(rp.trans_relation_analysis(t3_b1, t3_b1, net3, initial_marking3))

# a = rp.rp_mat_cal(net3, initial_marking3)
# b = rp.rp_mat_cal(net4, initial_marking4)
# print(a)
# print(b)

# c, d =pmap.p_mat_cal(net3,net4,corr.corresponding_map34)
# print(c)
# print(d)

# print(sim.sim_cal(a,b,c,d))


a = rp.rp_mat_cal(net1, initial_marking1)
b = rp.rp_mat_cal(net2, initial_marking2)
print(a)
print(b)

c, d =pmap.p_mat_cal(net1,net2,corr.corresponding_map12)
print(c)
print(d)

print('similarity =' + str(sim.sim_cal(a,b,c,d)))