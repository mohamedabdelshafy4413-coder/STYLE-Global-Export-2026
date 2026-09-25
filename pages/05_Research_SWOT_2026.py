import pandas as pd
import streamlit as st
from research_2026 import SWOT_2026, VERIFIED_SIGNALS, SOURCES_2026

st.set_page_config(page_title="STYLE | Research & SWOT 2026",page_icon="◆",layout="wide")
st.title("STYLE 2026 — Intensive Research, SWOT & Commercial Thesis")
st.caption("Source-derived trade/buyer signals are separated from STYLE strategic inference.")

a,b=st.columns(2)
for i,(name,items) in enumerate(SWOT_2026.items()):
    target=a if i%2==0 else b
    with target:
        st.subheader(name)
        for x in items: st.write("• "+x)

st.subheader("Commercial thesis")
st.markdown("""
### 1) The problem is no longer country discovery
STYLE already tested 50 countries and 5,000+ emails. The bottleneck is **buyer precision**.

### 2) Shipment-verified buyer intelligence should replace broad lead lists
Prioritize companies that imported relevant HS/product descriptions in the last 3–12 months, then verify company type and decision maker.

### 3) Egypt-origin proof should change the ranking
Turkey, Romania, Morocco and regional GCC markets deserve extra weight when trade data already proves Egyptian stone acceptance.

### 4) Product-market fit must be explicit
- Sunny Minya → GCC, North Africa, volume/project
- Galala → Europe, North America, GCC
- Meli Grey → France, Germany, UK, Switzerland, Australia
- New Halayeb → Germany, Poland, Korea, Japan, USA
- Ramady El Sherka → Germany, Switzerland, UK, monuments/architecture

### 5) Fast-reply potential is not a promise
No public database can guarantee a first-day reply. The system uses recency, density, fit and reachability to **increase the odds**, not guarantee outcomes.
""")

st.subheader("Verified current-market signals")
st.dataframe(pd.DataFrame(VERIFIED_SIGNALS),use_container_width=True,hide_index=True)

st.subheader("Source register")
for name,url in SOURCES_2026:
    st.markdown(f"- [{name}]({url})")
