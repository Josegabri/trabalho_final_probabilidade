import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt 
from scipy.stats import ttest_ind,stats,wilcoxon,ttest_rel

dados_brutos= pd.read_excel('PROVA.xls', 'dados_brutos')
dados_ambiente_1= pd.read_excel('PROVA.xls', 'ambiente_1')
dados_ambiente_2= pd.read_excel('PROVA.xls', 'ambiente_2')
dados_individuos_1=[1161,1267,1177,926,920,907]
dados_individuos_2=[242,273,242,313,363,315]

# ** Criando os gráficos ** 

# histograma_all= sn.histplot (data=dados_brutos, binwidth=20)
# histograma_all.figure.set_size_inches(12, 8)

# linha_all= sn.lineplot(data=dados_brutos)
# linha_all.figure.set_size_inches(12, 8)

# boxplot_all = sn.boxplot(data=dados_brutos)
# boxplot_all.figure.set_size_inches(15, 8)

# histograma_ambiente_1= sn.histplot (data=dados_ambiente_1)
# histograma_ambiente_1.figure.set_size_inches(12, 8)

# histograma_ambiente_2= sn.histplot (data=dados_ambiente_2)
# histograma_ambiente_2.figure.set_size_inches(12, 8)

# linha_ambiente_1= sn.lineplot(data=dados_ambiente_1)
# linha_ambiente_1.figure.set_size_inches(12, 8)

# linha_ambiente_2= sn.lineplot(data=dados_ambiente_2)
# linha_ambiente_2.figure.set_size_inches(20, 10)

# correlacao_dados_brutos= dados_brutos.corr()
# tabela_correlacao= sn.heatmap(correlacao_dados_brutos, annot=True)

# ** Salvando imagem dos gráficos ** 

# sn.FacetGrid.savefig(histograma_all, 'Histograma_all_dados')
# sn.FacetGrid.savefig(linha_all, 'grafico_linha_all')
# sn.FacetGrid.savefig(boxplot_all, 'boxplot_all')
# sn.FacetGrid.savefig(histograma_ambiente_1,'histograma_ambiente_1')
# sn.FacetGrid.savefig(histograma_ambiente_2,'histograma_ambiente_2')
# sn.FacetGrid.savefig(linha_ambiente_1,'grafico_linha_ambiente_1')
# sn.FacetGrid.savefig(linha_ambiente_2,'grafico_linha_ambiente_2_1')
# sn.FacetGrid.savefig(tabela_correlacao,'tabela_correlação_dados_brutos')

# ** Calculando teste de hipótese ** ]

print (ttest_rel(dados_individuos_1,dados_individuos_2))
