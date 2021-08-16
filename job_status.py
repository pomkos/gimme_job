import streamlit as st
import pandas as pd

st.title("Pete's Job Search")

st.info("Where Pete applied so far")

df = pd.read_table('Status.md', delimiter='|').iloc[:,1:7].drop(0, axis=0).reset_index(drop=True)
df.columns = [col.strip() for col in df.columns]
for col in df.columns:
    df[col] = df[col].str.strip()
# df['Applied'] = pd.to_datetime("2021 " + df['Applied'], format='%Y %b %d')

df = df[['Site','Applied','Company','Position','Status','Other']]
df = df.sort_values(['Site','Applied']).reset_index(drop=True)

st.table(df)