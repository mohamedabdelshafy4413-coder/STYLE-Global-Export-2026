import streamlit as st
from research_2026 import CASE_STUDY

st.set_page_config(page_title="STYLE | Campaign Case Study",page_icon="📨",layout="wide")
st.title("STYLE Global Outbound — Case Study")
st.caption("Observed campaign results supplied by the project owner. Rates below use 5,000 as the minimum denominator because the actual send count was stated as more than 5,000.")

c1,c2,c3,c4=st.columns(4)
c1.metric("Markets contacted",CASE_STUDY["markets"])
c2.metric("Emails sent","5,000+")
c3.metric("Positive commercial replies",CASE_STUDY["positive_replies"])
c4.metric("Near-order signal",CASE_STUDY["near_order"])

c5,c6,c7=st.columns(3)
c5.metric("Positive-conversation rate","≤ 0.20%")
c6.metric("Near-order signal rate","< 0.02%")
c7.metric("Future-potential accounts",CASE_STUDY["future_potential"])

st.subheader("Five promoted STYLE products")
st.write(" • ".join(CASE_STUDY["products"]))

st.subheader("What the pilot actually says")
for x in CASE_STUDY["interpretation"]:
    st.write("• "+x)

st.subheader("Why the next 100-market system must change")
st.markdown("""
**Old motion:** high-volume country coverage + broad company lists + one outbound system.  

**New motion:** recent-import filter → exact product fit → 2–4 decision makers/account → country-specific offer → 72-hour RFQ conversion lane.

The campaign is useful because it gave a real baseline. It does **not** prove that every country or every list source performs equally. We need per-country sent/delivered/replied/RFQ data to identify statistical winners.
""")

st.subheader("Next KPI stack")
st.dataframe({
"Metric":["Delivered","Positive Reply","Qualified Buyer","RFQ","Quote","Sample","Negotiation","Order","Repeat Order"],
"Why it matters":["Deliverability","Message-market fit","ICP quality","Buying intent","Commercial fit","Technical confidence","Deal maturity","Revenue","Account quality"]
},hide_index=True,use_container_width=True)
