from matplotlib import pyplot as plt
import matplotlib_venn as venn

S = {1,2,3}
T = {0,2,-1,5}
U = {10,2,12,4}

# strict subset means that it is the same definition as a subset except the two sets cannot be the same exact set
venn.venn3([S,T,U], set_labels=('S','T','U'))
plt.show()

