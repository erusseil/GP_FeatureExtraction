import numpy as np


def step(x1):
    return np.where(x1 > 0, x1, 0)


def protected_exponent(x1):
    with np.errstate(over='ignore'):
        return np.where(np.abs(x1) < 10, np.exp(x1), np.exp(10))


def bazin(x,p1,p2,p3,p4,p5):
    with np.errstate(over='ignore'):
        
        p3 =  np.where(p3 != 0, p3, 1)
        p4 =  np.where(p4 != 0, p4, 1)
        
        exp1 = -(x-p2)/p3
        num = np.where(exp1 < 50, np.exp(exp1), np.exp(50))
        
        exp2 = (x-p2)/p4
        den = 1 + np.where(exp2 < 50, np.exp(exp2), np.exp(50))
        
        return p1*num/den + p5


def ego(x,p1,p2,p3,p4,p5,p6,shift):
    
    # De la forme A / x + B*C*D
    x = x+shift+0.14
    
    protex = np.where(abs(x) > 0.001, x, (np.sign(x)+0.00001)*0.001)
    double_expo = 2*x*protected_exponent(protected_exponent(x))
    
    den_A = p3 +protected_exponent(p4*x)
    protec_den_A = np.where(abs(den_A) > 0.001, den_A, (np.sign(den_A)+0.0001)*0.001)
    A = p1 + p2/protec_den_A
    
    B = double_expo - p5
    
    C = double_expo - p6/protex
    
    full_den = x + A*B*C
    protec_full_den = np.where(abs(full_den) > 0.001, full_den, (np.sign(full_den)+0.0001)*0.001)
    
    return step(x)/protec_full_den



def ego_err(params, time, flux):
    diffs = np.abs(flux - ego(diffs))
    

    
def bazin_err(params, time, flux):
    diffs = np.abs(flux - bazin(time,*params))
    return 100. * np.average(diffs)