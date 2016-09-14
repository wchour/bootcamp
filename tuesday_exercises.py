import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# The following is specific Jupyter notebooks
# %matplotlib inline
# %config InlineBackend.figure_formats = {'png', 'retina'}

wt = np.loadtxt('data/wt_lac.csv', skiprows=3, comments='#', delimiter=',')
q18m = np.loadtxt('data/q18m_lac.csv', skiprows=3, comments='#', delimiter=',')
q18a = np.loadtxt('data/q18a_lac.csv', skiprows=3, comments='#', delimiter=',')



def plot_iptg():
    plt.plot(wt[:,0],wt[:,1], marker='.',
             linestyle='none', markersize=20, alpha=0.8)
    plt.plot(q18m[:,0],q18m[:,1], marker='.',
             linestyle='none', markersize=20, alpha=0.8)
    plt.plot(q18a[:,0],q18a[:,1], marker='.',
             linestyle='none', markersize=20, alpha=0.8)
    plt.legend(('wild type', 'Q18M', 'Q18A'), loc='lower right')
    plt.margins(0.02)
    plt.title('Fold Change Repression of Lac Gene')
    plt.xlabel('[IPTG] (mM)')
    plt.ylabel('fold change')
    plt.show()

# plot experimental data (fold change expression vs. [IPTG])
def plot_iptglogx():
    plt.semilogx(wt[:,0],wt[:,1], marker='.',
             linestyle='none', markersize=10, alpha=0.8)
    plt.semilogx(q18m[:,0],q18m[:,1], marker='.',
             linestyle='none', markersize=10, alpha=0.8)
    plt.semilogx(q18a[:,0],q18a[:,1], marker='.',
             linestyle='none', markersize=10, alpha=0.8)
    plt.legend(('wild type', 'Q18M', 'Q18A'), loc='lower right')
    plt.margins(0.02)
    plt.title('Fold Change Repression of Lac Gene')
    plt.xlabel('[IPTG] (mM)')
    plt.ylabel('fold change')
    # plt.show()

# calculate theoretical fold change value
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    conc = c
    rk = RK
    num = rk * (1 + (conc/KdA))**2
    denom = (1 + (conc/KdA))**2 + (Kswitch * (1 + (conc/KdI))**2)
    change = (1 + (num/denom))**(-1)
    return change

# plot theoretical fold change value along designated logspace
def smooth():
    data = np.logspace(-6,2,1000)
    constants = [('wt', 141.5), ('q18m', 1332), ('q18a', 16.56)]
    number = len(constants)
    for i in range(number):
        plt.semilogx(data, fold_change(data, constants[i-1][1], KdA=0.017,
                     KdI=0.002, Kswitch=5.8), marker='.',
                     linestyle='none', markersize=10, alpha=0.8)
        plt.legend(('wild type', 'Q18M', 'Q18A'), loc='lower right')
        plt.margins(0.02)
        plt.title('Theoretical Fold Change Repression of Lac Gene')
        plt.xlabel('[IPTG] (mM)')
        plt.ylabel('fold change')
    plt.show()

# calculate bohr parameter
def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    conc = c
    term1 = -1 * np.log(RK)
    num = (1 + (conc/KdA))**2
    denom = (1 + (conc/KdA))**2 + (Kswitch * (1 + (conc/KdI))**2)
    term2 = -1 * np.log(num/denom)

    return (term1 + term2)

# calculate the fold change value based on bohr parameter
def fold_change_bohr(bohr_parameter):
    denom = 1 + np.exp(-bohr_parameter)
    return (1/denom)

# p
def plot_bohr():
    x = np.linspace(-6,6,1000)
    fold_change = fold_change_bohr(x)
    plt.plot(x, fold_change, marker='.',
                             markersize=4, alpha=0.8, color='gray')
    plt.margins(0.02)
    plt.title('Bohr Parameter')


def plot_all():
    # Plot experimental data
    # plot_iptglogx()
    plot_bohr()
    constants = [('wt', 141.5), ('q18m', 1332), ('q18a', 16.56)]
    number = len(constants)
    # for i in range(number)

    x = bohr_parameter(wt[:,0], constants[0][1], KdA=0.017, KdI=0.002, Kswitch=5.8)
    y = wt[:,1]
    plt.plot(x, y, marker='.', linestyle='none', markersize=10, alpha=0.8)

    x1 = bohr_parameter(q18m[:,0], constants[1][1], KdA=0.017, KdI=0.002, Kswitch=5.8)
    y1 = q18m[:,1]
    plt.plot(x1, y1, marker='.', linestyle='none', markersize=10, alpha=0.8)

    x2 = bohr_parameter(q18a[:,0], constants[2][1], KdA=0.017, KdI=0.002, Kswitch=5.8)
    y2 = q18a[:,1]
    
    plt.plot(x2, y2, marker='.', linestyle='none', markersize=10, alpha=0.8)
    plt.legend(('theoretical', 'wt', 'q18m', 'q18a'), loc='lower right')
    plt.margins(0.02)
    plt.title('Experimental Fold Change vs. Bohr Parameter')
    plt.xlabel('Bohr Parameter')
    plt.ylabel('Fold Change')
