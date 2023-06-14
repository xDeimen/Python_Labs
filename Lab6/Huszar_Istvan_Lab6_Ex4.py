"""
EXERCITIUL 4:Aflatiminimulfunctiei: F = 100(y − x2)2+ (1 − x)2FolositialgoritmulPowell siGolden Section Search pentrurezolvareaproblemei
"""

from scipy.optimize import golden, fmin_powell

def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

x0 = [0, 0]  # punctul de start
res_powell = fmin_powell(f, x0)
res_golden = golden(f)