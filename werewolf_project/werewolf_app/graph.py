from plotly.offline import plot
import plotly.graph_objs as go

def makeGraph(x_data, y_data): # profile page graph
    fig = go.Figure()
    scatter = go.Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=1, marker_color='green')
    fig.add_trace(scatter)
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            showticklabels=False,
            gridcolor='lightgray',
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
        ), showlegend=False, margin=dict(
            l=0,
            t=0,
            b=0,
            r=0,
            pad=0,
        ), width=500, height=295, plot_bgcolor='white', paper_bgcolor='white',
    )
    plt_div = plot(fig, output_type='div')
    return plt_div
   
def doubleGraph(x_data, y_dataW, y_dataV): # end of game graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_dataW, name="Werewolves Alive", line_color="red"))
    fig.add_trace(go.Scatter(x=x_data, y=y_dataV, name="Villagers Alive", line_color="blue"))
    fig.update_layout(title_text="Roles Alive Per Turn")
    plt_div = plot(fig, output_type="div")
    return plt_div

def indexGraph(x_data, y_dataW, y_dataV): # main index graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_dataW, name="Werewolf Winrate", line_color="red"))
    fig.add_trace(go.Scatter(x=x_data, y=y_dataV, name="Villager Winrate", line_color="blue"))
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            showticklabels=False,
            gridcolor='lightgray',
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
        ), showlegend=False, margin=dict(
            l=0,
            t=0,
            b=0,
            r=0,
            pad=0,
        ), width=358, height=295, plot_bgcolor='white', paper_bgcolor='white',
    )
    plt_div = plot(fig, output_type="div")
    return plt_div