#!pip install dash
import dash
app=dash.Dash(__name__)
from dash import dcc, html
app.layout=html.Div([
    html.H1("My dash App", style={'textAlign':'center'}),
    dcc.Input(id='input-box',type='text', value='Type something...'),
    html.Button('Submit', id='button'),
    html.Div(id='output-div')
])
from dash.dependencies import Input, Output

@app.callback(
Output('Output-div','children'),
Input('button','n_clicks'),
[dash.dependencies.State('input-box','value')]
)
def update_output(n_clicks,value):
    if n_clicks is not None:
        return f'You have entered:{value}'
    return
if __name__=='__main__':
    app.run_server(debug=True)
    