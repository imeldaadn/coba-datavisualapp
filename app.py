import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as px

st.title("Halo, This is Imelda Audina!")
st.markdown("Dataset Data Visual ini diambil dari data Tips.csv")

############################################################
st.subheader("Diagram Batang")
# reading the database
data = pd.read_csv("tips.csv")

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])
plt.title("Bar Chart")
plt.xlabel('Day')
plt.ylabel('Tip')

# Now use st.pyplot to render the plot
st.pyplot()

############################################################
st.subheader("Histogram")
# reading the database
data = pd.read_csv("tips.csv")

sns.histplot(x='total_bill', data=data, kde=True, hue='sex')

# Use st.pyplot to render the histogram
st.pyplot()

############################################################
st.subheader("Sliders and Selectors")
# reading the database
data = pd.read_csv("tips.csv")

plot = px.Figure(data=[px.Scatter(
  y=data['tip'],
  mode='lines',)
])

plot.update_layout(
  xaxis=dict(
    rangeselector=dict(
      buttons=list([
        dict(count=1,
            step="day",
            stepmode="backward"),
      ])
    ),
    rangeslider=dict(
      visible=True
    ),
  )
)

# Use st.plotly_chart to render the plotly figure
st.plotly_chart(plot)
