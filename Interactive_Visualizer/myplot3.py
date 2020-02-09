import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

df =  pd.read_csv('cachexic.csv') 
colors = {
    'background': '#111111',
    'text': 'white'
}
app = dash.Dash()

app.layout = html.Div([
		html.H3(
			children='Multiplot Interactive Plaform',
			style={
				'textAlign': 'center',
				 'fontWeight': 'bold',
				 'color': 'teal'
			}
		),
		html.Div([
			
			html.Div([
				dcc.Dropdown(
					id='state-id',
					options=[{'label': i, 'value': i} for i in df.Muscle_loss.unique()],multi = True,
					placeholder='Filter by Muscle loss (control or cachexic...'
				)
			],
			style={'width': '49%', 'display': 'inline-block'}),
			html.Div([
			dcc.Dropdown(
				id='compound', 
				options=[{'label': i , 'value': i} for i in df.columns.to_list()[1:]],
				multi=True, placeholder='Filter by Compound Name...'
				)
			],
			style={'width':'48%', 'display': 'inline-block'}),
		
		
			
		
		 #    html.Div([
			# dcc.Dropdown(
			# 	id='indicator-id',
			# 	options=[{'label': i , 'value': i} for i in df.Age.unique()],
			# 	multi=True, placeholder='Filter by Age ...'
			# 	)
			# ],
			# style={'width':'48%', 'display': 'inline-block'}),
		
		
		dcc.Graph(id='indicator-graphic',style={'width':'1300','height':'700'},figure={
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
        )
		])
	])


@app.callback(
	dash.dependencies.Output('indicator-graphic', 'figure'),
	[dash.dependencies.Input('state-id', 'value'),dash.dependencies.Input('compound', 'value')
	 ]) # dash.dependencies.Input('indicator-id', 'value'),

def update_time_series(state_id,compound):
	
	#print(dff.head())
	data = []
	if state_id is not None or compound is not None:
		for state in state_id :
			try:
			#for  indicator_id in indicator_ids:
				for compd in compound:
					
					#print(df.head())
					if state is not None or compd is not None:

						dff = df.loc[(df['Muscle_loss'] == state )][compd]
						dff.reset_index(drop=True, inplace=True)
						
						#for indicator_id in indicator_ids:
							#print(indicator_id)
						#for columns in ['2013','2014','2015','2016']:
						
						trace = go.Scatter(
							x = dff.index,
							y = np.log(dff.values),
							name = 'Type: ' + state + ', Metabolites: ' + compd 
							
							)
						data.append(trace)
					else:
						print('error')
			except:
				print('try catch: something went wrong')
				#pass
		return {
			'data' : data,
			'layout' : go.Layout(
				xaxis={'title': 'Time line'},
				yaxis={'title': 'Metabolites Concentration'},
				plot_bgcolor = colors['background'],
                paper_bgcolor=colors['background'],
                font= {
                    'color': colors['text'],
                    'family': 'Courier New',
                    'size': 14

                }
				
			)

		}
	else:
		pass

if __name__ == '__main__':
	app.run_server(debug=True)


# family
#             HTML font family - the typeface that will be applied by
#             the web browser. The web browser will only be able to
#             apply a font if it is available on the system which it
#             operates. Provide multiple font families, separated by
#             commas, to indicate the preference in which to apply
#             fonts if they aren't available on the system. The
#             plotly service (at https://plot.ly or on-premise)
#             generates images on a server, where only a select
#             number of fonts are installed and supported. These
#             include "Arial", "Balto", "Courier New", "Droid Sans",,
#             "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
#             Standard TT", "Open Sans", "Overpass", "PT Sans
#             Narrow", "Raleway", "Times New Roman".
#         size
