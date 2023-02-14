import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
data = pd.read_csv('gapminder_with_codes.csv')
data_2007 = data[data['year'] == 2007]

fig = plt.figure()
sns.violinplot(data=data_2007, x='lifeExp')
plt.title('LIFE EXPECTANCY', fontsize=20, fontweight="bold")

st.pyplot(fig)

fig = plt.figure()
sns.violinplot(data=data_2007, x='pop')
plt.title('POPULATION', fontsize=20, fontweight="bold")
st.pyplot(fig)

fig = plt.figure()
sns.violinplot(data=data_2007, x='gdpPercap')
plt.title('GDP PER CAPITA', fontsize=20, fontweight="bold")
st.pyplot(fig)
