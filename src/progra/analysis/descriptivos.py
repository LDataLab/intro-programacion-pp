# Resumen
import numpy as np

def resumen(valores):
    percentiles = [10,30,50,70,80,90,95,99]
    for p in percentiles:
        print('Percentil',p,':', np.percentile(valores,p))
    
    print('\n Media:', valores.mean())
    print('\n Max:', valores.max())
    print('\n Min:', valores.min())
    
