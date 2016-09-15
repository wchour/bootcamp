import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# a) Load the drone weight data in as a Pandas DataFrame.
weight = pd.read_csv('data/bee_weight.csv', comment='#', header=0)
sperm = pd.read_csv('data/bee_sperm.csv', comment='#', header=0)

# b) Plot ECDFs of the drone weight for control and also for those exposed to
# pesticide. Do you think there is a clear difference?
def ecdf(data):
    return np.sort(data),np.arange(1, len(data)+1)/len(data)

x_ctrl, y_ctrl = ecdf(weight.loc[(weight['Treatment'] == 'Control'),
    ['Weight']])
x_tx, y_tx = ecdf(weight.loc[(weight['Treatment'] == 'Pesticide'),
    ['Weight']])
plt.plot(x_ctrl, y_ctrl, marker='.', linestyle='none', color='blue', alpha=0.8)
plt.plot(x_tx, y_tx, marker='.', linestyle='none', color='green', alpha=0.8)


# c) Compute the mean drone weight for control and those exposed to pesticide.
# Compute 95% bootstrap confidence intervals on the mean.
wt_ctrl = weight.loc[(weight['Treatment'] == 'Control'),
    ['Weight']]
wt_tx = weight.loc[(weight['Treatment'] == 'Pesticide'),
    ['Weight']]
wt_ctrl_mean = np.mean(wt_ctrl)
wt_tx_mean = np.mean(wt_tx)

n_reps = 100000
reps_ctrl = np.empty(n_reps)
reps_tx = np.empty(n_reps)
for i in range(n_reps):
    bs_ctrl = np.random.choice(wt_ctrl['Weight'], size=len(wt_ctrl))
    bs_tx = np.random.choice(wt_tx['Weight'], size=len(wt_tx))
    reps_ctrl[i] = np.mean(bs_ctrl)
    reps_tx[i] = np.mean(bs_tx)
ci_ctrl = np.percentile(reps_ctrl, [2.5, 97.5])
ci_tx = np.percentile(reps_tx, [2.5, 97.5])
print(ci_ctrl)
print(ci_tx)
# Ctrl CI:[ 274.68529625  279.39445125]
# Tx CI: [ 275.04747917  281.53252083]

# d) Repeat parts (a)-(c) for drone sperm. Use the 'Quality' column as your
# measure. This is defined as the percent of sperm that are alive in a 500 µL
# sample.
s_ctrl_quality = sperm.loc[(sperm['Treatment'] == 'Control'),
    ['Quality']]
# s_ctrl_quality_bad = sperm.loc[(sperm['Treatment'] == 'Control'),
#     ['Quality']] == 0 | np.isnan(sperm.loc[(sperm['Treatment'] == 'Control'),
#         ['Quality']])
s_ctrl_q_good = sperm.loc[(sperm['Treatment'] == 'Control') & (sperm['Quality']>0),
    ['Quality']]
s_tx_q_good = sperm.loc[(sperm['Treatment'] == 'Pesticide') & (sperm['Quality']>0),
    ['Quality']]

x_ctrl, y_ctrl = ecdf(s_ctrl_q_good)
x_tx, y_tx = ecdf(s_tx_q_good)
plt.plot(x_ctrl, y_ctrl, marker='.', linestyle='none', color='blue', alpha=0.8)
plt.plot(x_tx, y_tx, marker='.', linestyle='none', color='green', alpha=0.8)

s_ctrl_mean = np.mean(s_ctrl_q_good)
s_tx_mean = np.mean(s_tx_q_good)

n_reps = 10000
reps_ctrl = np.empty(n_reps)
reps_tx = np.empty(n_reps)
for i in range(n_reps):
    bs_ctrl = np.random.choice(s_ctrl_q_good['Quality'], size=len(s_ctrl))
    bs_tx = np.random.choice(s_tx_q_good['Quality'], size=len(s_tx))
    reps_ctrl[i] = np.mean(bs_ctrl)
    reps_tx[i] = np.mean(bs_tx)
ci_ctrl = np.percentile(reps_ctrl, [2.5, 97.5])
ci_tx = np.percentile(reps_tx, [2.5, 97.5])
print(ci_ctrl)
print(ci_tx)
# Ctrl CI: [ 86.29236592  90.23593036]
# Tx CI: [ 76.93448682  83.06661203]
# e) As you have seen in your analysis in part (d), both the control and
# pesticide treatments have some outliers with very low sperm quality. This can
# tug heavily on the mean. So, get 95% bootstrap confidence intervals for the
# median sperm quality of the two treatments.
