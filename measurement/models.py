from django.db import models
from django.db.models import PROTECT

from users.models import User
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
import plotly.io as pio


class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    weight = models.DecimalField(decimal_places=1, max_digits=4)
    hip_girth = models.DecimalField(decimal_places=1, max_digits=4)     # обхват бедра
    biceps_girth = models.DecimalField(decimal_places=1, max_digits=4)  # обхват бицепса

    def get_charts(self, user, w):
        measurements = Measurement.objects.filter(user__id=user.id)
        x_data = []
        for note in measurements:
            date = note.date_create
            date_str = date.strftime('%d-%m-%y %H:%M')
            x_data.append(date_str)
        weight = list([int(note.weight) for note in measurements])
        hips = list([int(note.hip_girth) for note in measurements])
        biceps = list([int(note.biceps_girth) for note in measurements])

        layout = go.Layout(
            autosize=False,
            width=w,
            height=300,
            margin=go.layout.Margin(l=0, r=0, b=0, t=0),
            plot_bgcolor='rgba(0,0,0,0)'
        )

        fig = go.Figure(data=go.Scatter(
            x=x_data, y=weight,
            mode='lines',
            name='test',
            opacity=1),
            layout=layout)
        fig.update_xaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')  # добавление сетки
        fig.update_yaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')
        pio.write_image(fig, 'measurement/templates/measurement/graphs/graph_weight.svg')

        fig = go.Figure(data=go.Scatter(
            x=x_data, y=hips,
            mode='lines',
            name='test',
            opacity=1),
            layout=layout)
        fig.update_xaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')  # добавление сетки
        fig.update_yaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')
        pio.write_image(fig, 'measurement/templates/measurement/graphs/graph_hip.svg')

        fig = go.Figure(data=go.Scatter(
            x=x_data, y=biceps,
            mode='lines',
            name='test',
            opacity=1),
            layout=layout)
        fig.update_xaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')  # добавление сетки
        fig.update_yaxes(showline=True, linewidth=0.1, linecolor='black', gridcolor='gray')
        pio.write_image(fig, 'measurement/templates/measurement/graphs/graph_biceps.svg')
