import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
data = pd.read_csv('gapminder_with_codes.csv')
data_2007 = data[data['year'] == 2007]

data_violin = []
data_violin.append(data['gdpPercap'])
data_violin.append(data['pop'])
data_violin.append(data['lifeExp'])

fig = plt.figure()
sns.violinplot(data=data_violin)
plt.title('Violin_plots', fontsize=20, fontweight="bold")

st.pyplot(fig)

fig = plt.figure()
sns.violinplot(data=data_2007, x='pop')
plt.title('POPULATION', fontsize=20, fontweight="bold")
st.pyplot(fig)

fig = plt.figure()
sns.violinplot(data=data_2007, x='gdpPercap')
plt.title('GDP PER CAPITA', fontsize=20, fontweight="bold")
st.pyplot(fig)
