import pandas as pd
import plotly.express as px
import streamlit as st
from research_2026 import WORLD_50, VERIFIED_SIGNALS, METHODOLOGY

st.set_page_config(page_title="STYLE | World 50 2026",page_icon="🌍",layout="wide")
st.title("STYLE — World 50 Expansion 2026")
st.caption("50 non-European markets selected separately from the old Global 100. Scores are STYLE strategic priority scores, not guaranteed reply or purchase probabilities.")

cols=["Rank","Country","Score","Tier","Region","Hero Products","Reply Potential","Demand","Why"]
df=pd.DataFrame(WORLD_50,columns=cols)
a,b,c,d=st.columns(4)
a.metric("Markets","50"); b.metric("Tier A",(df.Tier=="Tier A").sum()); c.metric("Tier A+B",df.Tier.isin(["Tier A","Tier B"]).sum()); d.metric("Top score",df.Score.max())

fig=px.choropleth(df,locations="Country",locationmode="country names",color="Score",hover_name="Country",hover_data=["Tier","Hero Products","Reply Potential","Why"],color_continuous_scale=["#24333b","#59624B","#C6A466"])
fig.update_layout(height=520,margin=dict(l=0,r=0,t=20,b=0),paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

c1,c2,c3=st.columns(3)
regions=c1.multiselect("Region",sorted(df.Region.unique()))
tiers=c2.multiselect("Tier",df.Tier.unique().tolist())
min_score=c3.slider("Minimum score",50,100,60)
view=df[df.Score>=min_score]
if regions:view=view[view.Region.isin(regions)]
if tiers:view=view[view.Tier.isin(tiers)]
st.dataframe(view,use_container_width=True,hide_index=True,height=650)
st.download_button("Download World 50 CSV",view.to_csv(index=False).encode(),"STYLE_WORLD_50_2026.csv","text/csv")

st.subheader("What makes this list stronger")
st.write("The list combines recent shipment/buyer activity, STYLE product fit, Egypt-origin compatibility, import scale, decision-maker accessibility, recent RFQ signals, logistics and risk. It is intentionally different from the older 100-country radar.")
w=pd.DataFrame(METHODOLOGY,columns=["Factor","Weight %"])
st.bar_chart(w.set_index("Factor"))

st.subheader("Verified live-market signals used")
s=pd.DataFrame(VERIFIED_SIGNALS)
st.dataframe(s,use_container_width=True,hide_index=True)
