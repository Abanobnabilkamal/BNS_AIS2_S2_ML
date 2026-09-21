import pandas as pd
import plotly.express as px
from dash import Dash , dcc , html , Input , Output

df = pd.read_csv('sales_data.csv')
app = Dash()
num_col = df.select_dtypes(include='number').columns

app.title='Interactive Dashboard'


app.layout = html.Div([
    html.H1('Interactive Dashboard with pie plot'),
    html.Label('select a value to show in the pie chart'),
    dcc.Dropdown(id='columns-dropdown',
    options= [{'label' : col , 'value' : col} for col in num_col ],
    value = num_col[0]),
    dcc.Graph(id='pie-chart')
    
])

@app.callback(Output('pie-chart','figure'),
              Input('columns-dropdown','value'))



def update_pie(select_col):
    grouped = df.groupby('Area')[select_col].sum().reset_index()
    fig = px.pie(grouped,names='Area',values=select_col,
                title=f'distribution of {select_col} by Area',hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set2)
    
    return fig



if __name__ == '__main__':
    app.run(debug=True)