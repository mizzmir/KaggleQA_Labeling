import numpy as np
from scipy.stats import spearmanr

"""
    Spearman metrics for comparing results
"""

def spearman_metric(y_true, y_pred):
    y_true, y_pred = np.vstack(y_true), np.vstack(y_pred)
    corr = [
        spearmanr(pred_col, target_col).correlation
                      for pred_col, target_col in zip(y_pred.T, y_true.T)
    ]
    return np.nanmean(corr)

metrics = {"spearmanr" :spearman_metric}
