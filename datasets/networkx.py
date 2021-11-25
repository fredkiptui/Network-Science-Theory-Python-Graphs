import networkx as nx
from networkx.utils.tests.test_heaps import data

df = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)
df.nodes()
df.edges()

import matplotlib.pyplot as plt
% matplotlib inline

plt.figure(figsize=(12,8))
nx.draw_networkx(df, with_labels=True)

