import networkx as nx
import plotly.graph_objs as go

node_list = ["Thang","B","C","D","E","F","G","H","E"]

from_list = ['B', 'E', 'B', 'B', 'B', 'C', 'C', 'E', 'D', 'Thang', 'E', 'E', 'H', 'B', 'B', 'C', 'Thang', 'Thang', 'G', 'G']
to_list = ['F', 'D', 'D', 'D', 'D', 'F', 'H', 'C', 'F', 'E', 'B', 'B', 'B', 'E', 'H', 'E', 'B', 'E', 'E', 'Thang']

def draw_graph(node_list, from_list, to_list):
    G = nx.Graph()
    for i in range(len(node_list)):
        G.add_node(node_list[i])
        G.add_edges_from([(from_list[i], to_list[i])])


    pos = nx.spring_layout(G, k=0.5, iterations=100)
    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=5, color='#888'),
        hoverinfo='none',
        mode='lines')
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='pinkyl',
            reversescale=True,
            color=[],
            size=37,
            colorbar=dict(
                thickness=1,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=0)))
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color'] += tuple([len(adjacencies[1])])
        node_info = adjacencies[0]
        node_trace['text'] += tuple([node_info])

    title = "Network Graph Demonstration"
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                    title=title,
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=21, l=5, r=5, t=40),
                    annotations=[dict(
                        text="",
                        showarrow=False,
                        xref="paper", yref="paper")],
                    xaxis=dict(showgrid=False, zeroline=False,
                               showticklabels=False, mirror=True),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, mirror=True)))
    fig.show()