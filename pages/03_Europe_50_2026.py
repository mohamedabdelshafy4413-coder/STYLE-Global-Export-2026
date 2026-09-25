import pandas as pd
import plotly.express as px
import streamlit as st
from research_2026 import EUROPE_50

st.set_page_config(page_title="STYLE | Europe 50 2026",page_icon="🇪🇺",layout="wide")
st.title("STYLE — Europe 50 / Extended Europe 2026")
st.caption("Europe is separated from World 50. The final rows are radar/extended-Europe markets; Russia/Belarus are explicitly compliance-held.")

cols=["Rank","Country","Score","Tier","Zone","Hero Products","Demand","Evidence"]
df=pd.DataFrame(EUROPE_50,columns=cols)
a,b,c,d=st.columns(4)
a.metric("Markets","50"); b.metric("Golden",(df.Tier=="Golden").sum()); c.metric("Golden + Strong",df.Tier.isin(["Golden","Strong"]).sum()); d.metric("Compliance Hold",(df.Tier=="Compliance Hold").sum())

fig=px.bar(df.head(25).sort_values("Score"),x="Score",y="Country",orientation="h",color="Score",color_continuous_scale=["#29424b","#C6A466"],hover_data=["Tier","Hero Products","Evidence"])
fig.update_layout(height=760,coloraxis_showscale=False,margin=dict(l=0,r=0,t=20,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

tiers=st.multiselect("Tier",df.Tier.unique().tolist())
view=df if not tiers else df[df.Tier.isin(tiers)]
st.dataframe(view,use_container_width=True,hide_index=True,height=700)
st.download_button("Download Europe 50 CSV",view.to_csv(index=False).encode(),"STYLE_EUROPE_50_2026.csv","text/csv")

st.warning("Europe 50 includes Extended Europe / radar markets because there are not 50 equally strong stone-import markets in Europe. Do not treat the bottom tier as equal to France, Germany, Romania or Turkey.")
