import numpy as np

def inlocuireNAN(X):
    mean = np.nanmean(X, axis=0)  # calculam mediile pentru coloanele ce au valori NAN
    pos = np.where(np.isnan(X))
    X[pos] = mean[pos[1]]
    return X

def ncomp_estim(alpha,pondere=None,limita=None):
    nrcomp_k =  len(np.where(alpha>1)[0])
    if pondere is None:
        pondere = np.cumsum(alpha/sum(alpha))
    if limita is not None:
        v = np.where(pondere>=limita)[0]
        if len(v)!=0:
            nrcomp_p = v[0] + 1
        else:
            nrcomp_p = np.NaN
    else:
        nrcomp_p = np.NaN
    m = len(alpha)
    eps = alpha[:(m-1)] - alpha[1:]
    sigma = eps[:(m-2)] - eps[1:]
    negative = sigma<0
    if any(negative):
        nrcomp_c = np.where(negative)[0][0] + 2
    else:
        nrcomp_c = np.NaN
    return [nrcomp_k,nrcomp_p,nrcomp_c]
