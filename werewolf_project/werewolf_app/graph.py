from plotly.offline import plot
import plotly.graph_objs as go

def makeGraph(x_data, y_data):
    fig = go.Figure()
    scatter = go.Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=1, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')
    return plt_div
   