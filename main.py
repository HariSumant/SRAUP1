import dash
import dash_auth
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


data2=pd.read_csv('SRA_Slum (2).csv')
#data3=pd.read_csv('cases_ulh.csv')
#data4=pd.read_csv('updatecas.csv')


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

auth = dash_auth.BasicAuth(
    app,
    {'Admin': 'SRA',
     'akhil': 'secure'}
)


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('SRA_LOGO.jpeg'),
                     id = 'corona-image',
                     style={'height': '150px',
                            'width': 'auto',
                            'margin-bottom': '35px',
                            'font-family':'Tahoma'})


        ], className='one-third column'),

        html.Div([
            html.Div([
                html.H3('SLUM REHABILITATION AUTHORITY', style={'margin-bottom': '10px', 'color': 'skyblue','font-style': 'Monaco','font-size':'40px'
                    ,'margin-right':'300px'}),

            ])

        ], className='one-half column', id = 'title'),

        html.Img(src=app.get_asset_url('Vlogo.jpeg'),
                     id = 'corona-image2',
                     style={'height': '180px',
                            'width': 'auto',
                            'margin-bottom': '35px',
                            'font-family':'Tahoma'})

        

    ], id = 'header', className= 'row flex-display', style={'margin-bottom': '25px','color': 'white'}),
     
    html.Div([
        html.Div([
            html.H6(children='Total Number Of Slums',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(f"{data2['FID'].count():,.0f}",
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 80})
           # html.P('new: ' + f"{covid_data_1['confirmed'].iloc[-1] - covid_data_1['confirmed'].iloc[-2]:,.0f}"
                  # + ' (' + str(round(((covid_data_1['confirmed'].iloc[-1] - covid_data_1['confirmed'].iloc[-2]) /
                               #    covid_data_1['confirmed'].iloc[-1]) * 100, 2)) + '%)',
                  # style={'textAlign': 'center',
                       #   'color': 'orange',
                         # 'fontSize': 15,
                         # 'margin-top': '-18px'})

        ], className='card_container three columns'),

html.Div([
            html.H6(children='SRA Status - YES',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(f"{'111'}",
                    style={'textAlign': 'center',
                           'color': '#dd1e35',
                           'fontSize': 80})
           # html.P('new: ' + f"{covid_data_1['death'].iloc[-1] - covid_data_1['death'].iloc[-2]:,.0f}"
                  # + ' (' + str(round(((covid_data_1['death'].iloc[-1] - covid_data_1['death'].iloc[-2]) /
                            #       covid_data_1['death'].iloc[-1]) * 100, 2)) + '%)',
                  # style={'textAlign': 'center',
                      #    'color': '#dd1e35',
                        #  'fontSize': 15,
                         # 'margin-top': '-18px'})

        ], className='card_container three columns'),

html.Div([
            html.H6(children='SRA Status - NO',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(f"{'445'}",
                    style={'textAlign': 'center',
                           'color': 'green',
                           'fontSize': 80})
           # html.P('new: ' + f"{covid_data_1['recovered'].iloc[-1] - covid_data_1['recovered'].iloc[-2]:,.0f}"
                  # + ' (' + str(round(((covid_data_1['recovered'].iloc[-1] - covid_data_1['recovered'].iloc[-2]) /
                          #         covid_data_1['recovered'].iloc[-1]) * 100, 2)) + '%)',
                   #style={'textAlign': 'center',
                          #'color': 'green',
                          #'fontSize': 15,
                          #'margin-top': '-18px'})

        ], className='card_container three columns'),

html.Div([
            html.H6(children='Total Area Under Slums(sq.km)',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            html.P(f"{'6.18'}",
                    style={'textAlign': 'center',
                           'color': '#e55467',
                           'fontSize': 60})
            #html.P('new: ' + f"{covid_data_1['active'].iloc[-1] - covid_data_1['active'].iloc[-2]:,.0f}"
                 #  + ' (' + str(round(((covid_data_1['active'].iloc[-1] - covid_data_1['active'].iloc[-2]) /
                     #              covid_data_1['active'].iloc[-1]) * 100, 2)) + '%)',
                  # style={'textAlign': 'center',
                       #   'color': '#e55467',
                         # 'fontSize': 15,
                         # 'margin-top': '-18px'})

        ], className='card_container three columns'),

    ], className='row flex display'),

    html.Div([
        html.Div([
            html.P('Select Ward:', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id = 'w_prabhag',
                         multi = False,
                         searchable= True,
                         value=1,
                         placeholder= 'Select Ward',
                         options= [{'label': c, 'value': c}
                                   for c in (data2['WARD_2017'].unique())], className='dcc_compon'),
            dcc.Graph(id = 'SLUM_CODE', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'}),
dcc.Graph(id = 'SRA_STATUS_NO', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'}),
dcc.Graph(id = 'SRA_STATUS_YES', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'}),
dcc.Graph(id = 'Shape_Area', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '20px'})

        ], className='create_container three columns'),


    ], className='row flex-display',style={'margin-left':'450px','width':'1500px'}),

    html.Div([
html.Div([
html.Iframe(srcDoc =open('SRAChangedF.html').read(),height='700',width='1250')  

                      
        ], className='create_container1 twelve columns')

    ], className='row flex-display')

], id = 'mainContainer', style={'display': 'flex', 'flex-direction': 'column'})

@app.callback(Output('SLUM_CODE', 'figure'),
              [Input('w_prabhag','value')])
def update_confirmed(w_prabhag):
    prabhag_data_2 = data2.groupby(['WARD_2017'])[['FID']].count().reset_index()
    prabhag_confirmed = data2[data2['WARD_2017'] == w_prabhag]['FID'].count()

    return {
        'data': [go.Indicator(
               mode='number',
               value=prabhag_confirmed,
               number={'valueformat': int(),
                       'font': {'size': 20}},
               domain={'y': [0, 1], 'x': [0, 1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total No.',
                   'y': 1,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color='orange'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height = 50,

        )
    }


@app.callback(Output('SRA_STATUS_NO', 'figure'),
              [Input('w_prabhag','value')])
def update_confirmed(w_prabhag):
    prabhag_data_4 = data2.groupby(['WARD_2017'])[['SRA_STATUS']].sum().reset_index()
    #status = prabhag_data_4[prabhag_data_4['WARD_2017'] == w_prabhag]['SRA_STATUS'].iloc[-1]
    status = data2[data2['WARD_2017'] == w_prabhag]['SRA_STATUS']=='NO'
    f = status.values.sum()
    return {
        'data': [go.Indicator(
               mode='number',
               value = f,
               number={'font': {'size': 20}},
               domain={'y': [0, 1], 'x': [0, 1]}
        )],

        'layout': go.Layout(
            title={'text': 'SRA Status NO',
                   'y': 1,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color='yellow'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height = 50,

        )
    }

@app.callback(Output('SRA_STATUS_YES', 'figure'),
              [Input('w_prabhag','value')])
def update_confirmed(w_prabhag):
    prabhag_data_4 = data2.groupby(['WARD_2017'])[['SRA_STATUS']].sum().reset_index()
    #status = prabhag_data_4[prabhag_data_4['WARD_2017'] == w_prabhag]['SRA_STATUS'].iloc[-1]
    status = data2[data2['WARD_2017'] == w_prabhag]['SRA_STATUS']=='NO'
    f1 = (~status).values.sum()
    return {
        'data': [go.Indicator(
               mode='number',
               value = f1,
               number={'font': {'size': 20}},
               domain={'y': [0, 1], 'x': [0, 1]}
        )],

        'layout': go.Layout(
            title={'text': 'SRA Status YES',
                   'y': 1,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color='green'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height = 50,

        )
    }

@app.callback(Output('Shape_Area', 'figure'),
              [Input('w_prabhag','value')])
def update_confirmed(w_prabhag):
    prabhag_data_5 = data2.groupby(['WARD_2017'])[['AREA_SQKM']].sum().reset_index()
    area = data2[data2['WARD_2017'] == w_prabhag]['AREA_SQKM'].sum()

    return {
        'data': [go.Indicator(
               mode='number',
               value=area,
               number={'valueformat': ',',
                       'font': {'size': 20}},
               domain={'y': [0, 1], 'x': [0, 1]}
        )],

        'layout': go.Layout(
            title={'text': 'Area(sq.km)',
                   'y': 1,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            font=dict(color='#e55467'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height = 50,

        )
    }



if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8080,debug=True)

