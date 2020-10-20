import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.

import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


st.title('DATALAND INC. LIMITED')
st.header('Data Is The New Oil ')

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select no of emails per week',
      0, 10, (0, 10)
)

st.subheader('choose your age:')
x = st.slider('x')
st.write('your age', x)

st.write('WElcome at our *data apps* :sunglasses:')


st.subheader('##DataFrames @no 1:')

st.write(pd.DataFrame({ 
      'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
   }))

st.subheader('##DataFrames @no 2:')

df = pd.DataFrame(
       np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


st.subheader('##DataFrames @no 3:')

df = pd.DataFrame(
  np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=1))


st.subheader('##DataFrames @no 4: Table')

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

st.subheader('##DataFrames @no 5:Line_Chart')

df = pd.DataFrame({
        'column 1':[1,2,3,4,5] , 
        'column 2': [10,20,30,40,50],
    })
st.line_chart(df)


st.subheader('##DataFrames @no 6:Area_Chart')


chart_data = pd.DataFrame(
    np.random.randn(10, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.subheader('##DataFrames @no 5:Line_Chart')

st.line_chart(chart_data)

st.subheader('##DataFrames @no 7:Bar_Chart')

st.bar_chart(chart_data)

st.subheader('##DataFrames @no 8:#matplotlib.pyplot figure')


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#streamlit.altair_chart(altair_chart, use_container_width=False)
#Display a chart using the Altair library.

st.subheader('##streamlit.pydeck_chart(pydeck_obj=None, use_container_width=False) Draw a chart using the PyDeck library.')

df = pd.DataFrame(
       np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
         map_style='mapbox://styles/mapbox/light-v9',
         initial_view_state=pdk.ViewState(
               latitude=37.76,
                longitude=-122.4,
                 zoom=11,
                 pitch=50,
        ),
       layers=[
                 pdk.Layer(
                        'HexagonLayer',
                       data=df,
                        get_position='[lon, lat]',
                        radius=200,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                       pickable=True,
                        extruded=True,
            ),
                pdk.Layer(
                         'ScatterplotLayer',
                      data=df,
                         get_position='[lon, lat]',
                         get_color='[200, 30, 0, 160]',
                        get_radius=200,
            ),
        ],
    ))
