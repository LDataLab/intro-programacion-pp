import numpy as np

def resumen(valores):
    percentiles = [10,30,50,70,80,90,95,99]

    for p in percentiles:
        print('Percentil',p,':', np.percentile(valores,p))
    
    print('\nMedia:', valores.mean())
    print('\nMax:', valores.max())
    print('\nMin:', valores.min())