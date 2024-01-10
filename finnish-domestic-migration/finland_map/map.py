# %%
import geopandas
import matplotlib.pyplot as plt

import networkx as nx
import pandas as pd
import numpy as np

import os

print(os.getcwd())


def visualize_network(network):
    data = geopandas.read_file("finland/kunta4500k_2022Polygon.shp")

    for i in range(0, len(data)):
        data.loc[i, "centroid_lon"] = data.geometry.centroid.x.iloc[i]
        data.loc[i, "centroid_lat"] = data.geometry.centroid.y.iloc[i]

    print(data.head())

    pos = {}

    for i in range(0, len(data)):
        node_info = data.loc[[i], ["nimi", "namn", "centroid_lon", "centroid_lat"]].values.tolist()
        name, namn, lon, lat = (
            node_info[0][0],
            node_info[0][1],
            node_info[0][2],
            node_info[0][3],
        )

        if name in network.nodes:
            network.nodes[name]["pos"] = [lon, lat]
            pos[name] = [lon, lat]

        elif namn in network.nodes:
            network.nodes[namn]["pos"] = [lon, lat]
            pos[namn] = [lon, lat]

    edges = network.edges()
    weights = [network[u][v]["Total"] for u, v in edges]
    weights2 = [w * 0.001 for w in weights]

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax = data["geometry"].boundary.plot(figsize=(20, 16))
    nx.draw(
        network,
        pos=pos,
        arrows=True,
        arrowstyle="->",
        node_size=100,
        with_labels=True,
        width=weights2,
    )

    plt.show()

    ax.set_title("2020")


# %% Data to dataframe

data = pd.read_csv("../data/mobility_by_year/2020.csv", delimiter=",")

data = data.rename(
    columns={
        "Area of arrival": "Arrival",
        "Area of departure": "Departure",
        "Total 2020 Intermunicipal migration": "Total",
        "Males 2020 Intermunicipal migration": "Males",
        "Females 2020 Intermunicipal migration": "Females",
    }
)

print("DATA:", data.head())


data = data.drop(data[data.Total == 0].index)

data = data.replace({"Arrival - ": "", "Departure - ": ""}, regex=True)

data
# %% Forming and visualizing the network


network = nx.from_pandas_edgelist(data, source="Departure", target="Arrival", edge_attr="Total")

print("Number of nodes:", network.number_of_nodes())
print("Number of edges:", network.number_of_edges())


visualize_network(network)


# %% Visualizing 1% of the links with highest values

df_sorted = data.sort_values(by=["Total"], ascending=False)
df_sorted = df_sorted.reset_index()

amount = len(data) * 0.01
amount = round(amount, 0)

del df_sorted["index"]
# fmt: off
df_strongest = df_sorted.iloc[0: int(amount), :]
# fmt: on

network_strongest = nx.from_pandas_edgelist(
    df_strongest, source="Departure", target="Arrival", edge_attr="Total"
)

max_st = nx.algorithms.tree.mst.maximum_spanning_tree(network_strongest)


visualize_network(network_strongest)


# %% Plotting degree distribution

degrees = []
for node in network.nodes():
    degree = network.degree(node)
    degrees.append(degree)


distribution = np.bincount(degrees)
distribution = distribution / float(len(degrees))

min_range = 0
max_range = max(degrees) + 1
x_values = list(range(min_range, max_range))


fig = plt.figure(2)
ax = fig.add_subplot(111)
offset = 0.5
ax.bar(np.array(x_values) - offset, distribution, width=0.5)
ax.set_xlabel("Degree")
ax.set_ylabel("P(k)")
plt.show()

# %%
