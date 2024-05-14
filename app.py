import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as px

import translators as ts
import pyttsx3
import time

engine = pyttsx3.init()

text = "This company was founded in 2010 by the infamous movie star, \
          Graeme Alexander. Currently, the company worths USD 1 billion \
          according to Forbes report in 2023. What an achievement in just \
          13 years."
engine.say(text)
engine.runAndWait()
time.sleep(2)
engine.say("terjemahannya dalam bahasa Indonesia sebagai berikut")
engine.runAndWait()
time.sleep(2)
hasil = ts.translate_text(text, to_language="id", translator='google')
print(hasil)
time.sleep(1)
engine.say(hasil)
engine.runAndWait()
engine.stop()

st.title("Halo, This is Imelda Audina!")
st.markdown("Dataset Data Visual ini diambil dari data Tips.csv")

############################################################
st.subheader("Diagram Batang")
# reading the database
data = pd.read_csv("tips.csv")

# Create the figure and axis objects
fig, ax = plt.subplots()

# Bar chart with day against tip
ax.bar(data['day'], data['tip'])
ax.set_title("Bar Chart")
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Display the plot using st.pyplot() with the figure object
st.pyplot(fig)

############################################################
st.subheader("Histogram")
# reading the database
data = pd.read_csv("tips.csv")

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the histogram using seaborn
sns.histplot(x='total_bill', data=data, kde=True, hue='sex', ax=ax)

# Display the plot using st.pyplot() with the figure object
st.pyplot(fig)

############################################################
st.subheader("Sliders and Selectors")
# reading the database
data = pd.read_csv("tips.csv")

# Create the plotly figure
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

# Display the plot using st.plotly_chart()
st.plotly_chart(plot)
