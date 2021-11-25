import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
data.head()

df = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)
df.nodes()
df.edges()

import networkx as nx
df = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)
df.nodes()

import matplotlib.pyplot as plt
% matplotlib inline

plt.figure(figsize=(12,8))
nx.draw_networkx(df, with_labels=True)


