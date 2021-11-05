from django.shortcuts import render
from django.http import HttpResponse

from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np
# Create your views here.


def index(request):
    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                             mode='markers',
                             name='markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                             mode='lines+markers',
                             name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                             mode='lines',
                             name='lines'))

    # Setting layout of the figure.
    fig.update_layout(title='Styled Scatter',
                      yaxis_zeroline=False, xaxis_zeroline=False)

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': fig},
                    output_type='div')

    return render(request, 'graph/demo_plot.html',
                  context={'plot_div': plot_div})