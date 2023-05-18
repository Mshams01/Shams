import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image

icon_pic=Image.open(r'C:\Users\mshams01\Desktop\download.png')

st.set_page_config(
    layout='wide',
    page_title='Dash board',
    page_icon=icon_pic

)




df=pd.read_excel(r'C:\Users\mshams01\Desktop\ergonamic project\16-April-2023 - Copy\data.xlsx')

page = st.sidebar.radio('Select Page', ['page1', 'page2', 'page3'])
if page=='page1':
    
    
    st.title(' Hello,This is Mohamed Shams Dashboard & website ')
    

    st.header(' i love python')
    #st.dataframe(df)
    btn2=st.button('Show Data')  
    if btn2:
        st.dataframe(df)
        
    btn=st.button('Submit')
    if btn:
        st.info('A7A')

    RD=st.radio('Select',['A','B','C']) 
    if RD=='A':
        st.info(' ايه اللى اخرك يا وحوح')   
    elif RD=='B':
        st.warning(' اه احنا جايين نهزر بقى ')   
    else:
        st.error('يابنى حل عنى الله يرضى عليك ')  
        
        
        
    chk=st.checkbox('I Agree')     
    if chk:
        st.exception('خلى بالك انت داخل على حوارات يا نجم ')

    st.selectbox('select you answer',['xx','yy','zz'])       

    st.slider('select',0,70)
    st.select_slider('select you answer',['X','Y','Z'])
    st.text_area('enter text here')
    st.text_area(' write parhgraf')
    st.file_uploader('Upload your file')
    #st.camera_input('picture')
    st.date_input('today')
    st.time_input('now')
    st.number_input('enter sap number')
    st.multiselect('select you answer',['xx','yy','zz'])


elif page =='page2':
    tab1, tab2 = st.tabs(['UniVariate', 'BiVariate'])
    with tab1:
        with st.container():
            space, col, space2 = st.columns([5, 3, 5])
            col_name = col.selectbox('select Column to show its distribution'.title(), df.columns)
            #fact_name= col.selectbox('select factroy to show its distribution'.title(), df['Factory'])
        if col_name in df.select_dtypes(include='number'):
            col1, space, col2 = st.columns([5, 3, 5])
            fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                title=f'{col_name} hist distribution', width=400)
            fig2 = px.box(df, y = col_name, color_discrete_sequence=px.colors.qualitative.Bold,
                          title=f'{col_name} boxplot distribution',width =  400)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2)
            
         
            
        else:
            col1, space, col2 = st.columns([5, 2, 5])
            fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                title=f'{col_name} hist distibution', width=550)
            fig2 = px.pie(df, names = col_name, color_discrete_sequence=px.colors.qualitative.Bold, hole= 0.3,
                          title=f'{col_name} pie distribution',width =  550)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2)
            
        with tab2:
            st.title('REBA_Degree distribution separated to each Factory')
            col1,  col2, col3 = st.columns([5,1,6])
            #with col2:
           
                #fig = px.bar(data_frame=df,x='REBA_CONDITION',color='Factory',barmode='group',
                       #color_discrete_sequence=px.colors.qualitative.Antique, width=350)
                                  
                
                
                
                #st.plotly_chart(fig)
               
            with col1:
                fig2= px.sunburst(df, path=['Factory', 'REBA_Degree', 'REBA_CONDITION'],
                                  color_discrete_sequence=px.colors.qualitative.Antique,
                                 width=550)
                
                st.plotly_chart(fig2)
    
            with col3:
           
                fig3 = px.box(data_frame=df,y='REBA_Degree',color= "REBA_CONDITION",
                       color_discrete_sequence=px.colors.qualitative.Antique, width=550
                                 )
                
                
                
                st.plotly_chart(fig3)
                
elif page =='page3':
    tab1, tab2 = st.tabs(['Uni','Bi'])
    with tab1: 
        
        img=Image.open(r'C:\Users\mshams01\Downloads\pngegg (26).png')
        st.image(img,width=300)              
    
    with tab2: 
        
        img2=Image.open(r'C:\Users\mshams01\Downloads\pngegg (12).png')
        st.image(img2,width=300)  
