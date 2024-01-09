# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import geopandas

MOBILITY_BY_YEAR_PATH = os.path.join("data", "mobility_by_year")


def betweenness_centralities():
    """
    Loop all of the biggest municipalities and calculate the betweenness centralities every five years
    for each municipality and plot them.

    """

    ten_largest = [
        "Helsinki",
        "Espoo",
        "Vantaa",
        "Turku",
        "Tampere",
        "Lahti",
        "Oulu",
        "Kuopio",
        "Pori",
        "Jyväskylä",
    ]
    all_bc = []
    years2 = ["1990", "1995", "2000", "2005", "2010", "2015", "2020"]

    for node in ten_largest:
        temp = []

        for year in years2:
            network, percent, df2 = data_to_network(year)

            bcs = nx.betweenness_centrality(
                network, weight="Total"
            )  # Weights are reciprocals of total values
            bc = [value for (key, value) in bcs.items() if key == node]
            temp.append(bc)

        print(node)
        all_bc.append(temp)

    fig1 = plt.figure(1)

    for i in range(10):
        plt.plot(years2, all_bc[i], label=ten_largest[i], marker=".")

        plt.legend(loc="upper right")
        plt.title("Betweenness Centralities")


def degree_dist(network):
    """
    Calculate and plot degree distribution
    """

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


def netto_network(network, df, percent):
    edges = network.edges()

    for city1, city2 in edges:
        sub_df = df[["Arrival", "Departure"]].isin([str(city1), str(city2)]).all(axis=1)

        df2 = df[sub_df]
        indexes = list(df2.index)

        if len(indexes) == 2:
            net = df2["Total"][indexes[0]] - df2["Total"][indexes[1]]
            if net > 0:
                df["netto"][indexes[0]] = net
                df["netto"][indexes[1]] = 0
            else:
                df["netto"][indexes[1]] = abs(net)
                df["netto"][indexes[0]] = 0

        else:
            df["netto"][indexes[0]] = df["Total"][indexes[0]]

    df_sorted2 = df.sort_values(by=["netto"], ascending=False)
    df_sorted2 = df_sorted2.reset_index()

    amount = len(df_sorted2) * percent
    amount = round(amount, 0)

    del df_sorted2["index"]
    df_strongest2 = df_sorted2.iloc[0 : int(amount), :]

    net_network = nx.from_pandas_edgelist(
        df_strongest2,
        source="Departure",
        target="Arrival",
        edge_attr="netto",
        create_using=nx.DiGraph(),
    )

    return net_network


def data_to_network(year, directed, edge_attr, percent, viz_bc):
    """
    Reads data to dataframe format.
    - Removes all the edges with total migration of zero.
    - Adds a column called 'log', which haves natural logarithm values of column 'Total'.
    - Changes column names to more suitable ones.

    """

    data = pd.read_csv(
        "/Users/elsaollikainen/Desktop/hands_on_network_analysis/hands-on-network-analysis/data/mobility_by_year/"
        + year
        + ".csv",
        delimiter=",",
        encoding="latin-1",
    )

    # if year == '2020':     # 2020 the file structure is different than the other files, it has two rows less
    # N = 0
    # else:
    # N = 2

    data = pd.read_csv(
        os.path.join(MOBILITY_BY_YEAR_PATH, year) + ".csv",
        delimiter=",",
        encoding="latin-1",
    )

    data = data.rename(
        columns={
            "Area of arrival": "Arrival",
            "Area of departure": "Departure",
            "Total " + year + " Intermunicipal migration": "Total",
            "Males " + year + " Intermunicipal migration": "Males",
            "Females " + year + " Intermunicipal migration": "Females",
        }
    )

    data = data.drop(data[data.Total == 0].index)  # Remove links with weight zero

    data = data.replace({"Arrival - ": "", "Departure - ": ""}, regex=True)

    data["log"] = np.log(data["Total"])
    data["netto"] = 0

    if viz_bc:
        data["Total"] = (
            1 / data["Total"]
        )  # take reciprocals for betweenness centrality, UNCOMMENT IF BC NOT NEEDED

    df_sorted = data.sort_values(by=[edge_attr], ascending=False)
    df_sorted = df_sorted.reset_index()

    percent = percent
    amount = len(df_sorted) * percent
    amount = round(amount, 0)

    del df_sorted["index"]
    df_strongest = df_sorted.iloc[0 : int(amount), :]

    if directed:
        network = nx.from_pandas_edgelist(
            df_strongest,
            source="Departure",
            target="Arrival",
            edge_attr=edge_attr,
            create_using=nx.DiGraph(),
        )

    else:
        network = nx.from_pandas_edgelist(
            df_strongest, source="Departure", target="Arrival", edge_attr=edge_attr
        )

    return network, data


def visualize_network(
    network, year, directed, viz_bc, df, edge_attr, netto, percent, node_colors=None
):
    fig = plt.figure(1, figsize=(10, 10))
    cmap = plt.get_cmap("Blues")
    vmin = -0.01
    vmax = 0.1

    edges = network.edges()

    if netto:
        weights = [network[u][v]["netto"] for u, v in edges]
        weights2 = [w * 0.002 for w in weights]
    else:
        weights = [network[u][v][edge_attr] for u, v in edges]

        if edge_attr == "Total":
            weights2 = [w * 0.001 for w in weights]
        elif edge_attr == "log":
            weights2 = [w * 0.1 for w in weights]

    if viz_bc:
        network_all = nx.from_pandas_edgelist(
            df,
            source="Departure",
            target="Arrival",
            edge_attr="log",
            create_using=nx.DiGraph(),
        )

        betweenness1 = nx.betweenness_centrality(network_all, weight="Total")

        nodes = network.nodes()
        betweenness = []

        for node in nodes:
            bc = [value for (key, value) in betweenness1.items() if key == node]
            betweenness.append(bc[0])

        if directed:
            nx.draw_kamada_kawai(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=25,
                node_size=100,
                with_labels=True,
                width=weights2,
                node_color=betweenness,
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        else:
            nx.draw(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=20,
                node_size=100,
                with_labels=True,
                width=weights2,
                node_color=betweenness,
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )

        fig.suptitle(year + "   " + edge_attr + "   " + str(percent) + "%")
        norm = mpl.colors.Normalize(vmin=0.0, vmax=vmax)
        scm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
        cbar = plt.colorbar(scm)
        cbar.ax.set_ylabel("# of contacts", rotation=270)

    elif node_colors is not None:
        if directed:
            nx.draw_kamada_kawai(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=25,
                node_size=100,
                with_labels=True,
                width=weights2,
                node_color=node_colors["proportion"],
                # vmin=vmin,
                # vmax=vmax,
                cmap=cmap,
            )
        else:
            nx.draw(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=20,
                node_size=100,
                with_labels=True,
                width=weights2,
                node_color=node_colors["proportion"],
                # vmin=vmin,
                # vmax=vmax,
                cmap=cmap,
            )

        # sm._A = []
        norm = mpl.colors.Normalize(
            vmin=min(node_colors["proportion"]), vmax=max(node_colors["proportion"])
        )
        scm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
        cbar = plt.colorbar(scm, fraction=0.036, pad=0.04)
        cbar.set_label(
            f"Proportion of demographic {node_colors['demographic_name']}",
            rotation=270,
            fontsize=10,
            labelpad=20,
        )
        fig.suptitle(year + "   " + edge_attr + "   " + str(percent) + "%")
    else:
        if directed:
            nx.draw_kamada_kawai(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=25,
                node_size=100,
                with_labels=True,
                width=weights2,
            )
        else:
            nx.draw(
                network,
                arrows=True,
                arrowstyle="->",
                arrowsize=20,
                node_size=100,
                with_labels=True,
                width=weights2,
            )

        fig.suptitle(year + "   " + edge_attr + "   " + str(percent) + "%")

    plt.show()


def main():
    """DEFINE THESE PARAMETERS TO MAKE DIFFERENT NETWORKS"""

    year = "2020"  # Select the year to visualize
    directed = False  # Select if the network is directed or not
    edge_attr = (
        "Total"  # Select if using 'Total' or 'log' which is logarithm of Total values
    )
    viz_bc = False  # Select if you want to visualize node colors based on their betweenness centralities
    """JOS viz_bc True, edge_attr = 'log', muuten ei toimi ! """

    percent = 0.01  # How many percent of the links are evaluated
    max_st = True  # Maximum spanning tree
    """ Maximum spanning tree can only be used with undirected networks!!"""

    netto = False  # Use net migration as edge weights
    """ JOS netto = true, edge_attr='Total' !!"""

    network, df = data_to_network(year, directed, edge_attr, percent, viz_bc)

    if max_st:
        network = nx.algorithms.tree.mst.maximum_spanning_tree(
            network, weight=edge_attr
        )

    if netto:
        network = netto_network(network, df, percent)

    visualize_network(network, year, directed, viz_bc, df, edge_attr, netto, percent)


def visualize_map(network, year, totnet):
    data = geopandas.read_file("./finland_map/finland/kunta4500k_2022Polygon.shp")

    for i in range(0, len(data)):
        data.loc[i, "centroid_lon"] = data.geometry.centroid.x.iloc[i]
        data.loc[i, "centroid_lat"] = data.geometry.centroid.y.iloc[i]

    print(data.head())

    pos = {}

    for i in range(0, len(data)):
        node_info = data.loc[
            [i], ["nimi", "namn", "centroid_lon", "centroid_lat"]
        ].values.tolist()
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
    print([network[u][v] for u, v in edges])

    weights = [network[u][v][str(totnet)] for u, v in edges]
    weights2 = [w * 0.001 for w in weights]

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # ax = data["geometry"].boundary.plot(figsize=(20, 16))
    ax = data["geometry"].plot(
        edgecolor="#FFCC99", facecolor="#FFB266", figsize=(20, 16)
    )
    nx.draw(
        network,
        pos=pos,
        arrows=True,
        arrowstyle="->",
        node_size=10,
        with_labels=False,
        width=weights2 * 5000,
    )

    plt.show()

    ax.set_title(year)


def get_node_colors_from_demographics(demographics, column, nodes):
    """Gets list of node colors (variable proportions) from demographics dataframe."""
    subset = demographics["Municipality"].isin(nodes)
    demographics_in_net = demographics[subset]
    demographics_in_net = demographics_in_net.set_index("Municipality")
    demographics_in_net = demographics_in_net.loc[nodes]
    node_colors = demographics_in_net[column]
    node_colors_dict = {"demographic_name": column, "proportion": node_colors}

    return node_colors_dict


# %%


def main():
    """DEFINE THESE PARAMETERS TO MAKE DIFFERENT NETWORKS"""

    year = "2000"  # Select the year to visualize
    directed = False  # Select if the network is directed or not
    edge_attr = (
        "Total"  # Select if using 'Total' or 'log' which is logarithm of Total values
    )
    viz_bc = False  # Select if you want to visualize node colors based on their betweenness centralities
    """JOS viz_bc True, edge_attr = 'log', muuten ei toimi ! """

    percent = 0.005  # How many percent of the links are evaluated
    max_st = True  # Maximum spanning tree
    """ Maximum spanning tree can only be used with undirected networks!!"""

    netto = False  # Use net migration as edge weights
    """ JOS netto = true, edge_attr='Total' !!"""

    network, df = data_to_network(year, directed, edge_attr, percent, viz_bc)

    demographic_to_color_by = (
        "0-30y"  # Name of demographic data column demographics.csv
    )
    # demographic_to_color_by = "log-Median income 2020"
    # demographic_to_color_by = "Percentage of males 2020"
    node_colors_dict = None
    if demographic_to_color_by is not None:
        demographics = pd.read_csv("data/demographics.csv")
        demographics["log-Median income 2020"] = np.log(
            demographics["Median income 2020"]
        )
        node_colors_dict = get_node_colors_from_demographics(
            demographics, demographic_to_color_by, list(network.nodes())
        )

    if max_st:
        network = nx.algorithms.tree.mst.maximum_spanning_tree(
            network, weight=edge_attr
        )

    if netto:
        network = netto_network(network, df, percent)

    visualize_network(
        network,
        year,
        directed,
        viz_bc,
        df,
        edge_attr,
        netto,
        percent,
        node_colors=node_colors_dict,
    )

    if netto == True:
        visualize_map(network, year, "netto")
    else:
        if edge_attr == "Total":
            visualize_map(network, year, "Total")
        else:
            visualize_map(network, year, "log")

    print(network.nodes())


main()


# %%

# %%
