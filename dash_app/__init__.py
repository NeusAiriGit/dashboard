import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash

import numpy as np
import pandas as pd
import math as mh

path = r'https://raw.githubusercontent.com/NeusAiriGit/dashboard/main/Df_PI.csv'
df = pd.read_csv(path)

colorG = 'black'
txg1 ='''Esta grafica indica la cantidad porcentual de personas internacionalizadas 
que se van en un programa de Intercambio o como Study Abroad, filtrado por la escuela 
a la que pertenecen, mostrando como varía esta relación entre los distintos colegios.'''

txg2 = '''Este porcentaje es el total de personas internacionalizadas por intercambio en el 
Tec de Monterrey'''

txg3 ='''Esta grafica de barras representa en una proporción de x en cada 5 
personas que quedan en su primera opción inscrita para intercambio vs las 
restantes que quedan en otras opciones,de igual forma esta grafica se 
filtra año.'''

txg4 = '''El grafico aluvial anteriormente mostrado es una representación del 
flujo de alumnos por escuela, que son seleccionados para su primera u otra 
opción de internacionalización, y a su vez cuales son los destinos (Continentes) 
a los que se dirige este flujo de estudiantes. 

El filtro que existe para este grafico es a través del nivel educativo 
desde prepa Tec hasta el Doctorado. '''

txg5 = '''Este grafico representa la cantidad de alumnos enviados por las diferentes escuelas, 
se puede hacer un filtrado por el campus de origen de estos alumnos , 
lo que permite visualizar el impacto de los programas internacionales 
por cada uno de los campus matrices del ITESM.'''

Creden = '''Por: José Rodrigo Hernández A01610903'''

def create_dash_application(flask_app):
    app = dash.Dash(
        server=flask_app,name="Dashboard",
        url_base_pathname='/dash/'
    )
    app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Dashboard // Programas internacionales', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),
        html.Div(children=Creden,style = {'textAlign':'right','color':colorG}),
        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'Ingeniería y Ciencias', 'value':'Ingeniería y Ciencias' },
            {'label': 'Negocios', 'value':'Negocios'},
            {'label': 'Humanidades y Educación', 'value':'Humanidades y Educación'},
            {'label':'Ciencias Sociales y Gobierno', 'value':'Ciencias Sociales y Gobierno' },
            {'label': 'Arquitectura, Arte y Diseño', 'value':'Arquitectura, Arte y Diseño'},
            {'label': 'Salud', 'value':'Salud'},
            ],
        value = 'Negocios'),
        dcc.Graph(id = 'graph_pie'),
        dcc.Graph(id = 'porcenmuestra'),
        dcc.Graph(id = 'numenmuestra'),
        html.Div(children=txg1,style = {'textAlign':'center','color':colorG}),
        
        dcc.Graph(id = 'PorcenSa'),
        html.Div(children=txg2,style = {'textAlign':'center','color':colorG}),

        dcc.Dropdown( id = 'dropdown5',
        options = [
            {'label':'2014', 'value':2014},
            {'label': '2015', 'value':2015},
            {'label': '2016', 'value':2016},
            {'label':'2017', 'value':2017},
            {'label': '2018', 'value':2018},
            {'label': '2019', 'value':2019},
            {'label': '2020', 'value':2020},
            {'label': '2021', 'value':2021},
            {'label': '2022', 'value':2022},
            ],
        value = 2022),
        dcc.Graph(id = 'Picto_chart'),
        
        dcc.Graph(id = 'PorcenAcep'),
        html.Div(children=txg3,style = {'textAlign':'center','color':colorG}),

        dcc.Dropdown( id = 'dropdown3',
        options = [
            {'label':'Profesional', 'value':'Profesional' },
            {'label': 'Maestría', 'value':'Maestría'},
            {'label': 'Preparatoria', 'value':'Preparatoria'},
            {'label':'Doctorado', 'value':'Doctorado' },
            {'label': 'Especialidad', 'value':'Especialidad'},
            {'label': 'Indefinido', 'value':'Indefinido'},
            ],
        value = 'Profesional'),

        dcc.Graph(id = 'Alluvial'),
        html.Div(children=txg4,style = {'textAlign':'center','color':colorG}),

        dcc.Dropdown( id = 'dropdown4',
        options = [
            {'label':'Monterrey', 'value':'Monterrey' },
            {'label': 'Santa Fe', 'value':'Santa Fe'},
            {'label': 'Querétaro', 'value':'Querétaro'},
            {'label':'Chihuahua', 'value':'Chihuahua' },
            {'label': 'Estado de México', 'value':'Estado de México'},
            {'label': 'Guadalajara', 'value':'Guadalajara'},
            {'label':'León', 'value':'León' },
            {'label': 'Toluca', 'value':'Toluca'},
            {'label': 'EGADE Monterrey', 'value':'EGADE Monterrey'},
            {'label':'Laguna', 'value':'Laguna' },
            {'label': 'Puebla', 'value':'Puebla'},
            {'label': 'Aguascalientes', 'value':'Aguascalientes'},
            {'label':'Ciudad Juárez', 'value':'Ciudad Juárez' },
            {'label': 'San Luis Potosí', 'value':'San Luis Potosí'},
            {'label': 'Morelia', 'value':'Morelia'},
            {'label':'Tampico', 'value':'Tampico' },
            {'label': 'Ciudad de México', 'value':'Ciudad de México'},
            {'label': 'Zacatecas', 'value':'Zacatecas'},
            {'label':'Central de Veracruz', 'value':'Central de Veracruz' },
            {'label': 'EGADE Santa Fe', 'value':'EGADE Santa Fe'},
            {'label': 'EGADE Ciudad de México', 'value':'EGADE Ciudad de México'},
            {'label':'Valle Alto', 'value':'Valle Alto' },
            {'label': 'Santa Catarina', 'value':'Santa Catarina'},
            {'label': 'Cuernavaca', 'value':'Cuernavaca'},
            {'label':'Universidad Virtual en Línea', 'value':'Universidad Virtual en Línea' },
            {'label': 'Cumbres', 'value':'Cumbres'},
            {'label': 'Sonora Norte', 'value':'Sonora Norte'},
            {'label':'Saltillo', 'value':'Saltillo' },
            {'label': 'Irapuato', 'value':'Irapuato'},
            {'label': 'Ciudad Obregón', 'value':'Ciudad Obregón'},
            {'label':'Sinaloa', 'value':'Sinaloa' },
            {'label': 'Chiapas', 'value':'Chiapas'},
            {'label': 'Eugenio Garza Sada', 'value':'Eugenio Garza Sada'},
            {'label':'Eugenio Garza Lagüera', 'value':'Eugenio Garza Lagüera' },
            {'label': 'Ciudad Matamoros', 'value':'Ciudad Matamoros'},
            {'label': 'EGAP Santa Fe', 'value':'EGAP Santa Fe'},
            {'label': 'EGAP Monterrey', 'value':'EGAP Monterrey'},
            ],
        value = 'Monterrey'),

        dcc.Graph(id = 'BubbleCHa'),
        html.Div(children=txg5,style = {'textAlign':'center','color':colorG}),


    ])

    '''Grafica de PIE'''
    @app.callback(Output(component_id='graph_pie', component_property= 'figure'),
                [Input(component_id='dropdown', component_property= 'value'),])
    def graph_update(dropdown_value):

        vallist = dict(df['IntVsSa'].where(df['Escuela'] == dropdown_value).value_counts())


        fig = go.Figure([go.Pie(values= list(vallist.values()), labels = list(vallist.keys()),
            insidetextorientation='radial',
                        
                        )]) 
        fig.update_layout(title_text='% de personas en intercambio Vs SA',
        
        )                     
        return fig
    
    @app.callback(Output(component_id='porcenmuestra', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value'),])
    def graph_update(dropdown_value):

        vallist = dict(df['IntVsSa'].where(df['Escuela'] == dropdown_value).value_counts())
        filterval = sum(list(vallist.values()))
        tatalval = sum(list(dict(df['IntVsSa'].value_counts()).values()))

        porcfil = round(((filterval*100)/tatalval),2)

        fig6 = go.Figure()
        fig6.add_trace(go.Indicator(
            mode='number',
            value=porcfil,
            number = {'suffix': "%"},
            title = {"text": "Porcentaje de la muestra total"},
            
        ))
        return fig6

    @app.callback(Output(component_id='numenmuestra', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value'),])
    def graph_update(dropdown_value):

        vallist = dict(df['IntVsSa'].where(df['Escuela'] == dropdown_value).value_counts())
        filterval = sum(list(vallist.values()))

        fig7 = go.Figure()
        fig7.add_trace(go.Indicator(
            mode='number',
            value=filterval,
            number = {'suffix': " Instancias"},
            title = {"text": "Numero de instancias en la muestra"},
            
        ))
        return fig7

    def porcenta(porcen):
        if porcen >= 0 and porcen < 20:
            canti = 0
        elif porcen >= 20 and porcen < 40:
            canti = 1
        elif porcen >= 40 and porcen < 60:
            canti = 2
        elif porcen >= 60 and porcen < 80:
            canti = 3
        elif porcen >= 80 and porcen < 98:
            canti = 4
        elif porcen >= 98:
            canti = 5
        return canti


    @app.callback(Output(component_id='Picto_chart', component_property= 'figure'),
                [Input(component_id='dropdown5', component_property= 'value')])
    def graph_update(dropdown_value):

        top_l = ['Primera opción','Otra']
        colors = ['rgba(226, 77, 24, 0.6)', 'rgba(71, 58, 131, 0.6)']
        colors_line = ['rgba(226, 77, 24, 1.0)', 'rgba(71, 58, 131, 1.0)']
        x_data = list(df['PrimeraOp'].where(df['yearOfRec'] == dropdown_value).value_counts())
        totaldata = x_data[0] + x_data[1]

        porcenAcep = mh.floor((x_data[0]*100)/totaldata)
        porcenOtr = mh.floor((x_data[1]*100)/totaldata)
        x_data[1] = x_data[1]*(-1)

        porcenAcepnum = porcenta(porcenAcep)
        porcenOtrnum = porcenta(porcenOtr)
        if porcenOtrnum == 0:
            porcenOtrnum = 1
        elif porcenOtrnum == porcenAcepnum or (porcenOtrnum+porcenAcepnum) != 5:
            if x_data[0] > (x_data[1]*(-1)):
                porcenAcepnum += 1
            else:
                porcenOtrnum += 1

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            y = ['Opción Asignada',],
            x = [x_data[0],],
            name=top_l[0],
            orientation='h',
            text = str(porcenAcepnum) + ' de cada 5 personas',
            textposition='inside',
            textfont_size=20,
            marker=dict(
                color=colors[0],
                line=dict(color=colors_line[0],width =3)
            )
        ))

        fig2.add_trace(go.Bar(
            y = ['Opción Asignada',],
            x = [x_data[1],],
            name=top_l[1],
            orientation='h',
            text = str(porcenOtrnum) + ' de cada 5 personas',
            textposition='inside',
            textfont_size=20,

            marker=dict(
                color=colors[1],
                line=dict(color=colors_line[1],width =3)
            )
            
        ))
        
        fig2.update_layout(barmode='overlay',title_text='Personas aceptadas en primera opción')
        return fig2

    @app.callback(Output(component_id='PorcenAcep', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
    def graph_update(dropdown_value):

        x_data = list(df['PrimeraOp'].value_counts())
        totaldata = x_data[0] + x_data[1]

        porcenAcep = round(((x_data[0]*100)/totaldata),3)
        
        fig5=  go.Figure(go.Indicator(
            mode = "gauge+number",
            value =  porcenAcep,
            number={'suffix':'%'},
            title = {'text':'Porcentaje de personas aceptadas en su primera opción'},
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge={'axis':{'range':[None,100]}}
            
        ))
        
        return fig5

    @app.callback(Output(component_id='PorcenSa', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
    def graph_update(dropdown_value):

        IntVsSaData = dict(df['IntVsSa'].value_counts())
        totalInterSa = sum(list(IntVsSaData.values()))
        InterData = IntVsSaData.get('Intercambio')
        porcenInt = round(((InterData*100)/totalInterSa),2)
        
        fig8=  go.Figure(go.Indicator(
            mode = "gauge+number",
            value =  porcenInt,
            number={'suffix':'%'},
            title = {'text':'Porcentaje de personas en Intercambio'},
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge={'axis':{'range':[None,100]}}
            
        ))
        
        return fig8

    def colorsrun(lista,tipo):
        colors = []
        colors_line = []

        if tipo == 1:
            for i in range(0,len(lista)):
                colors.append('rgba('+ str(226-(i*10))+',' + str(77+(i*10))+','+ str(24+(i*5))+','+str(0.3)+')')
                colors_line.append('rgba('+ str(226-(i*10))+',' + str(77+(i*10))+','+ str(24+(i*5))+','+str(1.0)+')')
        elif tipo == 2:
            for i in range(0,len(lista)):
                colors.append('rgba('+ str(156-(i*10))+',' + str(177+(i*10))+','+ str(104+(i*5))+','+str(0.3)+')')
                colors_line.append('rgba('+ str(156-(i*10))+',' + str(177+(i*10))+','+ str(104+(i*5))+','+str(1.0)+')')
        elif tipo == 3:
            for i in range(0,len(lista)):
                colors.append('rgba('+ str(126-(i*10))+',' + str(200+(i*10))+','+ str(104+(i*5))+','+str(0.3)+')')
                colors_line.append('rgba('+ str(126-(i*10))+',' + str(200+(i*10))+','+ str(104+(i*5))+','+str(1.0)+')')
        
        return colors,colors_line
    
    '''Alluvial'''
    @app.callback(Output(component_id='Alluvial', component_property= 'figure'),
                [Input(component_id='dropdown3', component_property= 'value')])
    def graph_update(dropdown_value):
        
        
        dfFIL = df.where(df['Nivel'] == dropdown_value).copy()

        df2 =dfFIL.groupby(['Escuela','PrimeraOp'])['Area Academica'].count().reset_index()
        df2.columns = ['source','target','value']
        df2['target'] = df2.target.map({0.0 : 'Otra op', 1.0 : 'Primera'})
        unicEsc = list(df2['source'].unique())

        df3 =dfFIL.groupby(['PrimeraOp','Continent_Name'])['Area Academica'].count().reset_index()
        df3.columns = ['source','target','value']
        df3['source'] = df3.source.map({0.0 : 'Otra op', 1.0 : 'Primera'})
        unicOp = list(df3['source'].unique())
        unicCont = list(df3['target'].unique())

        links = pd.concat([df2,df3],axis=0)

        unique_s_t = list(pd.unique(links[['source','target']].values.ravel('K')))
        mappin_dict = {k: v for v, k in enumerate(unique_s_t)} 
        links['source'] = links.source.map(mappin_dict)
        links['target'] = links.target.map(mappin_dict)
        liks_dic = links.to_dict(orient='list')

        colors =[]
        colors2a =[]
        colors_line =[]
        colors1,colors_line1 = colorsrun(unicEsc,1)
        colors2,colors_line2 = colorsrun(unicOp,2)
        colors3,colors_line3 = colorsrun(unicCont,3)
        

        colors.extend(colors1)
        colors.extend(colors2)
        colors.extend(colors3)

        ncolors = colors.copy()
        ncolors.extend(colors1)
        ncolors.extend(colors2)
        ncolors.extend(colors3)


        colors_line.extend(colors_line1)
        colors_line.extend(colors_line2)
        colors_line.extend(colors_line3)
        
        fig3 = go.Figure(data=[go.Sankey(
            node=dict(
                pad= 15,
                thickness = 20,
                line = dict(color=colors,width = 0.5),
                label = unique_s_t,
                color=colors_line
            ),
            link=dict(
                source= liks_dic['source'],
                target= liks_dic['target'],
                value= liks_dic['value'],
                color = ncolors
            )
        )])

        fig3.update_layout(title_text='Flujo de estudiantes internacionales',)
        return fig3
    
    @app.callback(Output(component_id='BubbleCHa', component_property= 'figure'),
              [Input(component_id='dropdown4', component_property= 'value')])
    def graph_update(dropdown_value):

        valorEsc = list(df['Escuela'].where(df['Campus'] == dropdown_value).value_counts().to_dict().values())
        nameEsc = list(df['Escuela'].where(df['Campus'] == dropdown_value).value_counts().to_dict().keys())
        posiList = []
        colorList = []
        for i in range(0, len(valorEsc)):
            posiList.append(0)
            colorList.append('rgba('+ str(226-(i*12))+',' + str(77+(i*12))+','+ str(24+(i*7))+','+str(1.0)+')')

        fig4 = go.Figure()
        fig4.add_trace(go.Histogram(
            x=nameEsc,
            y=valorEsc,
            histfunc='sum',
            marker = dict(color=colorList,)


        ))
        
        fig4.update_layout(title_text='Enviados por escuela')
        
        return fig4

    return app
