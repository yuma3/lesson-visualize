import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

import chart_studio
import chart_studio.plotly as py



# df = pd.read_csv('assets/2010YumaAZ.csv')

# days = ['TUESDAY','WEDNESDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
# data = []
# for day in days:
#   trace = go.Scatter(
#                     x=df['LST_TIME'],
#                     y=df[df['DAY'] == day]['T_HR_AVG'],
#                     mode='lines',
#                     name=day
#                     )
#   data.append(trace)

# layout = go.Layout(title='平均温度')

# fig = go.Figure(data=data,layout=layout)


emi_stats = pd.read_csv('assets/argen/emiliano_martinez.csv')
emi_stats = emi_stats.fillna(0)
emi_stats.loc[1, 'Season'] = '2012-2013'
emi_float = emi_stats.drop('Season', axis=1)
emi_float = emi_float.replace(',', '.', regex=True).astype(float)
emi_float.iloc[5, 2] = 1136.00
emi_float.iloc[9, 2] = 1620.00

emi_dict = emi_float.to_dict()
emi_dict.keys()


fig = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=['シーズン', '試合数', '先発', '出場時間', '失点', '失点率/90(%)', '被シュート', 'セーブ数', 'セーブ率', 'クリーンシート', 'クリーンシート率(%)'],
                fill_color='paleturquoise',
                align='left',
                height=28,
                font=dict(size=13),
                ),
            cells=dict(
                values=[
                    emi_stats['Season'],
                    emi_stats['Game'],
                    emi_stats['Start'],
                    emi_stats['Minute'],
                    emi_stats['Against'],
                    emi_stats['Against90'],
                    emi_stats['Sot'],
                    emi_stats['Saves'],
                    emi_stats['Save %'] * 100 ,
                    emi_stats['Clean-sheet'],
                    emi_stats['Clean-sheet %'],
                    ],
                font=dict(size=14),
                fill_color='lavender',
                align='right',
                height=30,
                ))])
   
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H2(
        children='「Squad Age Balance 20/21 ~11/01」',
        style={
            'textAlign': 'center',
            'font-family': 'monospace',
            'color': '#ffffff',
            'padding-top': 20
        }
    ),
    html.H5(
        children='by Bucciarati',
        style={
            'textAlign': 'center',
            'font-family': 'monospace',
            'color': '#eeeeee'
        }
    ),
    html.Div([
        dcc.Graph(
            id='table',
            figure=fig,
            style={
                # "display": "inline-block",
                # "margin-left": "auto",
                # "margin-right": "auto",
            }
        )
    ])
], style={
    # 'margin': 'auto', 'width': "70%",
    # 'background-color': '#000000'
}
)

fig['layout'].update(
    title='Emiliano Martínez',
    font={"family": "Monospace", "size": 12},
    title_x=0.5,
    width=1700, height=1000,
)

if __name__ == '__main__':
    app.run_server(debug=True)
