import numpy as np
import scipy.stats as stats

chat_id = 419801345

def solution(data: np.ndarray) -> bool:
    threshold = 500

    t_stat, p_value = stats.ttest_1samp(data, threshold)
    
    p_value_one_sided = p_value / 2
    
    reject_null = (p_value_one_sided < 0.02) and (np.mean(data) > threshold)
    
    return reject_null
