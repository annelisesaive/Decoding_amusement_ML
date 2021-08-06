import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import MultiComparison
import scipy.stats as stats

def Anova_Improved(df, rating, group='Time', alpha=0.05, ylim=0, graph=True, order=None, color='gray'):
    
    bloc_list = []
    for tag in df[group].unique():
        bloc_list.append(list(df.loc[df[group] == tag][rating]))
    
    # Create a barplot
    if graph:
        sns.barplot(x=group, y=rating, data=df, color=color);
        plt.ylim(ylim)
        plt.show()

    # Anova
    k, p = stats.f_oneway(*bloc_list)
    print('k-value:',k)

    if p < alpha:
        print("p = {:g}*".format(p))
        print("There's a difference in at least one groups\n")
    else:
        print("p = {:g}".format(p))
        print("There's no difference in the groups\n")

    # Multiple Comparaison

    mc = MultiComparison(df[rating], df[group])
    mc_results = mc.tukeyhsd(alpha=alpha)
    print(mc_results)
    
    return


def regression(df, x, y, title='No title', alpha=0.05, graph=True):
    if graph:
        ax = sns.regplot(x=x, y=y, data=df, line_kws={"color":"black"}).set_title(title)
    print(x,'X',y)
    v, p = stats.kendalltau(df[x],df[y]) 
    if p <alpha:
        print('Relation significative')
        print(stats.kendalltau(df[x],df[y]),'*')
    else:
        print('Relation non significative')
        print(stats.kendalltau(df[x],df[y]))
        
    return v
        
        
def t_test(df, x, y, alpha=0.05):    
    t, p_value =stats.ttest_ind(x, y)
    
    if p <alpha:
        print('Difference significative')
        print(stats.ttest_ind(x, y),'*')
    
    else:
        print('Differnce non significative')
        print(stats.ttest_ind(x, y))
        
def spearman(df, x, y, title='No title', alpha=0.05):
    ax = sns.regplot(x=x, y=y, data=df, line_kws={"color":"black"}).set_title(title)
    print(x,'X',y)
    v, p = stats.spearmanr(df[x],df[y]) 
    if p <alpha:
        print('Relation significative')
        print(stats.spearmanr(df[x],df[y]),'*')
    else:
        print('Relation non significative')
        print(stats.spearmanr(df[x],df[y]))