from __future__ import annotations
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from data import MARKETS, PRODUCTS, TOP_DETAILS, EVIDENCE, SOURCES

st.set_page_config(page_title='STYLE | Global Export Intelligence 100', page_icon='◆', layout='wide', initial_sidebar_state='expanded')

GOLD='#C6A466'; INK='#0D1720'; NAVY='#112E3C'; TEAL='#123F4A'; OLIVE='#59624B'; CREAM='#F4F0E8'; MUTED='#A7A096'; WHITE='#F9F8F4'

st.markdown(f'''<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap');
html,body,[class*="css"]{{font-family:'Inter',sans-serif}}
.stApp{{background:radial-gradient(circle at 15% 0%,#173440 0,#0b151d 34%,#080f15 100%);color:{WHITE}}}
section[data-testid="stSidebar"]{{background:linear-gradient(180deg,#0b151d,#101f28 55%,#121813);border-right:1px solid rgba(198,164,102,.22)}}
section[data-testid="stSidebar"] *{{color:#ece8df}}
h1,h2,h3{{font-family:'Manrope',sans-serif;letter-spacing:-.02em}}
.hero{{padding:28px 30px;border:1px solid rgba(198,164,102,.22);border-radius:24px;background:linear-gradient(135deg,rgba(17,46,60,.96),rgba(9,16,22,.96) 52%,rgba(89,98,75,.35));box-shadow:0 18px 70px rgba(0,0,0,.28);margin-bottom:18px}}
.kicker{{color:{GOLD};font-weight:800;font-size:.77rem;letter-spacing:.16em;text-transform:uppercase}}
.hero h1{{font-size:2.1rem;margin:.35rem 0 .2rem;color:#fff}}
.hero p{{color:#d9d4cb;max-width:980px;font-size:1rem}}
.metric-card{{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.018));border:1px solid rgba(198,164,102,.18);border-radius:18px;padding:16px 18px;min-height:116px}}
.metric-label{{color:#aaa397;font-size:.76rem;text-transform:uppercase;letter-spacing:.08em;font-weight:700}}
.metric-value{{font-family:'Manrope';font-size:1.72rem;font-weight:800;color:#fff;margin-top:7px}}
.metric-note{{font-size:.76rem;color:#bfb9ae;margin-top:4px}}
.section-label{{color:{GOLD};font-size:.76rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;margin:22px 0 5px}}
.insight{{border-left:3px solid {GOLD};padding:12px 16px;background:rgba(198,164,102,.07);border-radius:0 12px 12px 0;color:#dfdbd2}}
.small{{font-size:.78rem;color:#aaa397}}
[data-testid="stDataFrame"]{{border:1px solid rgba(198,164,102,.16);border-radius:14px;overflow:hidden}}
div.stButton>button{{border-radius:12px;border:1px solid rgba(198,164,102,.45);background:linear-gradient(180deg,#c6a466,#a8874c);color:#111;font-weight:800}}
[data-testid="stDownloadButton"] button{{border-radius:12px;border:1px solid rgba(198,164,102,.45);background:#142934;color:#f5eee0}}
hr{{border-color:rgba(255,255,255,.08)}}
</style>''', unsafe_allow_html=True)

@st.cache_data
def market_df():
    region_sets = {
        'GCC': {'Saudi Arabia','Kuwait','United Arab Emirates','Qatar','Oman','Bahrain'},
        'Europe': {'France','Germany','United Kingdom','Switzerland','Poland','Italy','Spain','Netherlands','Belgium','Romania','Bulgaria','Greece','Austria','Sweden','Norway','Denmark','Czechia','Portugal','Ireland','Cyprus','Lithuania','Latvia','Estonia','Slovakia','Slovenia','Croatia','Serbia','Hungary','Finland','Malta','Iceland'},
        'North America': {'United States','Canada','Mexico'},
        'Asia': {'Turkey','South Korea','Japan','China','India','Hong Kong','Singapore','Malaysia','Taiwan','Philippines','Indonesia','Thailand','Vietnam','Cambodia','Kazakhstan','Azerbaijan','Georgia','Uzbekistan'},
        'Africa': {'Morocco','Algeria','South Africa','Kenya','Ghana','Nigeria','Côte d’Ivoire','Senegal','Cameroon','Tanzania','Rwanda','Zambia','Uganda','Mauritius','Libya','Tunisia','Ethiopia','Djibouti','Angola','Mozambique','Botswana','Namibia','Zimbabwe','Madagascar','Equatorial Guinea','Guinea'},
        'Oceania': {'Australia','New Zealand'},
        'Latin America': {'Brazil','Colombia','Chile','Peru','Dominican Republic','Panama','Costa Rica','Uruguay','Argentina'},
        'Levant': {'Lebanon','Jordan','Iraq','Israel'},
        'Caribbean': {'Bahamas'},
    }
    rows=[]
    for rank,(country,score) in enumerate(MARKETS,1):
        region=next((r for r,s in region_sets.items() if country in s),'Other')
        tier='Wave 1' if rank<=5 else 'Wave 2' if rank<=11 else 'Wave 3' if rank<=20 else 'Global Radar'
        det=TOP_DETAILS.get(country)
        if det:
            buyer,hero,angle,demand,price,egypt=det
        else:
            buyer='Importers + distributors'
            hero='Galala / Sunny / Granite'
            angle='Reliable Egyptian supply + commercial fit'
            demand='Medium-High' if score>=70 else 'Medium'
            price='High' if score>=75 else 'Mid-High'
            egypt='Medium'
        rows.append(dict(Rank=rank,Country=country,Score=score,Tier=tier,Region=region,Buyer=buyer,HeroProducts=hero,Angle=angle,Demand=demand,Price=price,EgyptProof=egypt))
    return pd.DataFrame(rows)

DF=market_df()

st.sidebar.markdown(f"<div class='kicker'>STYLE FOR MARBLE & GRANITE</div><h2 style='margin-top:.35rem'>Export Intelligence 100</h2><p class='small'>Global market prioritization • product-market fit • GTM • campaign engine</p>", unsafe_allow_html=True)
page=st.sidebar.radio('Navigation', ['Executive Command Center','Global 100 Ranking','Golden 20 Deep Dive','Product–Market Fit','Market Explorer','90-Day GTM','Campaign Studio','Revenue Scenarios','Lead File Analyzer','SWOT & Positioning','Evidence & Methodology'])
st.sidebar.divider()
st.sidebar.caption('Strategic scores are prioritization models — not guaranteed sales probabilities.')

st.markdown("<div class='hero'><div class='kicker'>STYLE GLOBAL EXPORT COMMAND CENTER</div><h1>Reliable Egyptian Stone Supply — ranked, targeted, and converted.</h1><p>A decision system for where STYLE should sell, what to lead with, who to target, what message to use, and what sales should do next across 100 markets.</p></div>", unsafe_allow_html=True)

def cards(items):
    cols=st.columns(len(items))
    for c,(label,val,note) in zip(cols,items):
        c.markdown(f"<div class='metric-card'><div class='metric-label'>{label}</div><div class='metric-value'>{val}</div><div class='metric-note'>{note}</div></div>", unsafe_allow_html=True)

def gold_header(text): st.markdown(f"<div class='section-label'>{text}</div>", unsafe_allow_html=True)

if page=='Executive Command Center':
    cards([('Markets mapped','100','Global strategic radar'),('Execution markets','20','Golden focus markets'),('Wave 1','5','Saudi • USA • France • Kuwait • Morocco'),('Hero materials','6','4 marble + 2 granite')])
    gold_header('Market priority map')
    fig=px.choropleth(DF, locations='Country', locationmode='country names', color='Score', hover_name='Country', hover_data=['Rank','Tier','HeroProducts'], color_continuous_scale=[[0,'#26333a'],[.45,'#59624B'],[.72,'#9f824d'],[1,'#E0C07A']], range_color=(50,100))
    fig.update_layout(height=490,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#eee',coloraxis_colorbar_title='EAI')
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
    c1,c2=st.columns([1.1,.9])
    with c1:
        gold_header('Golden 10')
        top=DF.head(10).copy()
        fig2=px.bar(top.sort_values('Score'),x='Score',y='Country',orientation='h',text='Score',color='Score',color_continuous_scale=['#59624B','#C6A466'])
        fig2.update_layout(height=440,showlegend=False,coloraxis_showscale=False,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#ddd',xaxis=dict(range=[75,100],gridcolor='rgba(255,255,255,.06)'))
        st.plotly_chart(fig2,use_container_width=True,config={'displayModeBar':False})
    with c2:
        gold_header('Board-level decisions')
        st.markdown("""
        <div class='insight'><b>1. Saudi Arabia = first battlefield.</b><br>High project demand, regional logistics and proven Egyptian-origin acceptance.</div><br>
        <div class='insight'><b>2. USA = largest upside.</b><br>Large addressable marble/granite demand; target distributors and fabricators, not generic contractors.</div><br>
        <div class='insight'><b>3. France/Germany = proof-led Europe.</b><br>Technical documentation, origin, consistency and distributor economics matter more than generic “premium marble” language.</div><br>
        <div class='insight'><b>4. Turkey/Romania/Morocco = Egypt-proof markets.</b><br>Direct evidence of Egyptian stone demand lowers the education barrier.</div>
        """,unsafe_allow_html=True)
    gold_header('Wave architecture')
    wave=DF.groupby('Tier',sort=False).agg(Markets=('Country','count'),AvgScore=('Score','mean')).reset_index()
    st.dataframe(wave,use_container_width=True,hide_index=True)

elif page=='Global 100 Ranking':
    c1,c2,c3=st.columns(3)
    region=c1.multiselect('Region',sorted(DF.Region.unique()),default=[])
    tier=c2.multiselect('Execution tier',DF.Tier.unique().tolist(),default=[])
    minscore=c3.slider('Minimum score',50,97,60)
    view=DF[DF.Score>=minscore]
    if region:view=view[view.Region.isin(region)]
    if tier:view=view[view.Tier.isin(tier)]
    st.dataframe(view[['Rank','Country','Score','Tier','Region','Demand','Price','EgyptProof','Buyer','HeroProducts']],use_container_width=True,hide_index=True,height=620)
    st.download_button('Download filtered market list',view.to_csv(index=False).encode(),'style_market_100.csv','text/csv')

elif page=='Golden 20 Deep Dive':
    country=st.selectbox('Select market',DF.head(20).Country)
    r=DF[DF.Country==country].iloc[0]
    cards([('Rank',f"#{int(r.Rank)}",r.Tier),('EAI score',f"{int(r.Score)}/100",'Strategic prioritization'),('Demand',r.Demand,'Category demand signal'),('Egypt proof',r.EgyptProof,'Origin acceptance signal')])
    gold_header('Commercial playbook')
    a,b=st.columns(2)
    with a:
        st.markdown(f"**Primary buyer:** {r.Buyer}\n\n**Hero products:** {r.HeroProducts}\n\n**Positioning angle:** {r.Angle}")
    with b:
        st.markdown("**Required proof pack**\n\n• Real quarry/factory footage  \n• Batch photos  \n• Packing & container loading  \n• Technical sheet / lab support  \n• FOB + CIF option  \n• Lead time + MOQ")
    ev=pd.DataFrame([x for x in EVIDENCE if x['market']==country])
    if not ev.empty:
        gold_header('Verified external evidence')
        st.dataframe(ev[['metric','value','note']],hide_index=True,use_container_width=True)
        for x in ev.to_dict('records'): st.markdown(f"[{x['metric']}]({x['url']})")
    gold_header('Recommended first 30 days')
    st.progress(min(int(r.Score),100)/100)
    st.markdown(f"""1. Build **50 Golden Accounts** in {country}.  
2. Map **2–4 decision makers** per large account.  
3. Lead with **{r.HeroProducts}** only — not the full catalogue.  
4. Use the **{r.Angle}** message.  
5. Push positive replies into a 72-hour quote/sample workflow.""")

elif page=='Product–Market Fit':
    product=st.selectbox('Hero material',list(PRODUCTS))
    p=PRODUCTS[product]
    cards([('Family',p['family'],'Material family'),('Strategic role',p['role'],'Portfolio role'),('Best use',p['best_for'],'Application fit')])
    st.markdown(f"<div class='insight'><b>Positioning:</b> {p['positioning']}</div>",unsafe_allow_html=True)
    fit=DF.copy()
    fit['Fit']=fit.Country.apply(lambda c: min(99,fit.loc[fit.Country==c,'Score'].iloc[0]+(6 if c in p['markets'] else 0)))
    fit=fit.sort_values(['Fit','Score'],ascending=False).head(20)
    gold_header('Top 20 product-market matches')
    fig=px.bar(fit.sort_values('Fit'),x='Fit',y='Country',orientation='h',color='Fit',color_continuous_scale=['#29424b','#C6A466'],hover_data=['Buyer','Angle'])
    fig.update_layout(height=560,coloraxis_showscale=False,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#ddd',xaxis=dict(range=[50,100],gridcolor='rgba(255,255,255,.06)'))
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})

elif page=='Market Explorer':
    left,right=st.columns([.55,.45])
    with left: country=st.selectbox('Country',DF.Country)
    with right: buyer=st.selectbox('Buyer type',['Importer / Distributor','Stone Yard / Wholesaler','Fabricator / Processor','Contractor / Developer','Monument / Headstone','Interior / Architect'])
    r=DF[DF.Country==country].iloc[0]
    cards([('Market rank',f"#{int(r.Rank)}",r.Tier),('Market score',int(r.Score),'EAI 2.0'),('Price signal',r.Price,'Strategic classification'),('Egypt proof',r.EgyptProof,'Origin fit')])
    gold_header('Recommended route to market')
    if buyer=='Importer / Distributor': route='Trial container → recurring stock programme → annual volume commitment'
    elif buyer=='Fabricator / Processor': route='Slab/block offer → technical fit → repeat raw-material programme'
    elif buyer=='Contractor / Developer': route='BOQ/project brief → cut-to-size + finish → phased project supply'
    elif buyer=='Monument / Headstone': route='Granite technical proof → standard monument sizes → recurring programme'
    else: route='Sample/spec pack → material shortlist → project/RFQ collaboration'
    st.markdown(f"<div class='insight'><b>{buyer}</b><br>{route}</div>",unsafe_allow_html=True)
    st.markdown(f"**Best current angle:** {r.Angle}\n\n**Suggested products:** {r.HeroProducts}\n\n**Commercial objective:** move from first reply → sample/RFQ → quote → trial order → repeat programme.")

elif page=='90-Day GTM':
    plan=pd.DataFrame([
        ('Days 1–10','Trust Repair','Fix website contradictions, claims, contact consistency, export CTA, real proof assets','Export-ready digital trust layer'),
        ('Days 11–20','Sales Assets','6 product sheets, technical pack, packing/loading proof, quote template, sample kit','Complete export sales kit'),
        ('Days 21–30','Account Intelligence','Top 10 markets × 100 accounts; map decision makers and buying signals','1,000 researched accounts'),
        ('Days 31–45','Pilot Outreach','Saudi, USA, France, Kuwait, Morocco; 50 Golden accounts/market','250-account controlled pilot'),
        ('Days 46–60','Learn & Double Down','Measure positive replies, RFQs, product/segment/country performance','Winning message-market fit'),
        ('Days 61–75','Wave 2','Germany, UK, Canada, Turkey, Romania','Scaled qualified pipeline'),
        ('Days 76–90','Deal Conversion','Samples, calls, FOB/CIF quotes, negotiations, trial containers','First orders + repeat path'),
    ],columns=['Window','Workstream','Actions','Output'])
    st.dataframe(plan,use_container_width=True,hide_index=True,height=360)
    gold_header('Funnel targets — planning ranges, not guarantees')
    funnel=pd.DataFrame({'Stage':['Researched Accounts','A/GOLDEN Accounts','Decision-Maker Contacts','Personalized First Touches','Meaningful Replies','Qualified Buyers','RFQ / Samples','Negotiations','Initial Orders'],'Low':[1000,500,750,500,40,15,8,4,1],'High':[1000,500,1200,750,80,35,20,10,4]})
    fig=go.Figure()
    fig.add_bar(y=funnel.Stage,x=funnel.High,orientation='h',name='High case',marker_color='#59624B')
    fig.add_bar(y=funnel.Stage,x=funnel.Low,orientation='h',name='Low case',marker_color='#C6A466')
    fig.update_layout(barmode='overlay',height=520,margin=dict(l=0,r=0,t=20,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#ddd',xaxis=dict(type='log',gridcolor='rgba(255,255,255,.06)'))
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})

elif page=='Campaign Studio':
    c1,c2,c3=st.columns(3)
    country=c1.selectbox('Country',DF.head(30).Country)
    buyer=c2.selectbox('Buyer persona',['Importer / Distributor','Stone Yard / Wholesaler','Fabricator / Processor','Contractor / Developer','Monument / Headstone'])
    first=c3.text_input('First name','{{First Name}}')
    r=DF[DF.Country==country].iloc[0]
    company=st.text_input('Company','{{Company}}')
    subject=f"Egyptian stone supply option for {company}"
    body=f"""Dear {first},\n\nI’m reaching out from STYLE for Marble & Granite in Egypt.\n\nI noticed {company} operates in the {buyer.lower()} space in {country}. Rather than sending a generic catalogue, I wanted to see whether an additional Egyptian source could be commercially relevant for your purchasing team.\n\nFor {country}, the materials I would prioritize are {r.HeroProducts}. Our focus is consistent supply, project-ready processing, quality inspection, export packing and documentation — not one-off spot selling.\n\nIf you currently import marble or granite, I can send a focused FOB offer for the 2–3 materials that best match your market.\n\nWould it be useful if I sent the current export selection and indicative FOB levels?\n\nBest regards,\nSTYLE for Marble & Granite\nEgypt"""
    st.text_input('Subject',subject)
    st.text_area('Email',body,height=360)
    gold_header('Message rule')
    st.markdown(f"<div class='insight'><b>{country} angle:</b> {r.Angle}<br><b>Do not lead with:</b> “best price” or a generic full catalogue.<br><b>Lead with:</b> business relevance + 2–3 matched materials + low-friction quotation CTA.</div>",unsafe_allow_html=True)

elif page=='Revenue Scenarios':
    st.caption('Scenario model only. Values are user assumptions, not forecasts or guarantees.')
    c1,c2,c3,c4=st.columns(4)
    contacts=c1.number_input('Qualified contacts',100,5000,750,50)
    reply=c2.slider('Meaningful reply %',1.0,20.0,8.0,.5)/100
    qual=c3.slider('Qualified from replies %',10,80,40,5)/100
    close=c4.slider('Initial order close %',2,40,12,1)/100
    c5,c6,c7=st.columns(3)
    order_value=c5.number_input('Avg first order revenue ($)',5000,250000,30000,5000)
    margin=c6.slider('Gross margin %',5,50,22,1)/100
    repeat=c7.slider('12-month repeat multiplier',1.0,12.0,3.0,.5)
    replies=contacts*reply; qualified=replies*qual; wins=qualified*close; first_rev=wins*order_value; annual_rev=first_rev*repeat; gross=annual_rev*margin
    cards([('Meaningful replies',f"{replies:.0f}",'Assumption-driven'),('Qualified buyers',f"{qualified:.1f}",'Assumption-driven'),('Initial orders',f"{wins:.1f}",'Assumption-driven'),('12m gross contribution',f"USD {gross:,.0f}",'Scenario, not forecast')])

elif page=='Lead File Analyzer':
    st.caption('Upload a CSV/XLSX. The analyzer prioritizes records using known market priority + contact completeness. It does not claim purchase intent.')
    up=st.file_uploader('Upload lead file',type=['csv','xlsx','xls'])
    if up:
        if up.name.lower().endswith('.csv'): leads=pd.read_csv(up)
        else: leads=pd.read_excel(up)
        st.write(f"Rows: **{len(leads):,}** • Columns: **{len(leads.columns)}**")
        cols_lower={c.lower().strip():c for c in leads.columns}
        def pick(keys):
            for k in keys:
                for low,orig in cols_lower.items():
                    if k in low:return orig
            return None
        c_country=pick(['country','nation']); c_email=pick(['email','e-mail']); c_company=pick(['company','business','account']); c_phone=pick(['phone','mobile','whatsapp']); c_web=pick(['website','web','url'])
        scoremap=dict(zip(DF.Country,DF.Score))
        out=leads.copy(); out['STYLE Lead Score']=50
        if c_country: out['STYLE Lead Score']+=out[c_country].map(scoremap).fillna(55).sub(55).mul(.45).clip(-5,20)
        if c_email: out['STYLE Lead Score']+=out[c_email].fillna('').astype(str).str.contains('@').astype(int)*10
        if c_phone: out['STYLE Lead Score']+=out[c_phone].notna().astype(int)*5
        if c_web: out['STYLE Lead Score']+=out[c_web].notna().astype(int)*5
        if c_company: out['STYLE Lead Score']+=out[c_company].notna().astype(int)*5
        out['STYLE Lead Score']=out['STYLE Lead Score'].clip(0,100).round(0).astype(int)
        out=out.sort_values('STYLE Lead Score',ascending=False)
        st.dataframe(out.head(500),use_container_width=True,height=520)
        st.download_button('Download prioritized file',out.to_csv(index=False).encode(),'style_prioritized_leads.csv','text/csv')
    else:
        st.info('No file uploaded yet.')

elif page=='SWOT & Positioning':
    a,b=st.columns(2)
    with a:
        gold_header('Strengths')
        st.markdown('• Quarry/source positioning  \n• Marble + granite portfolio  \n• Blocks / slabs / tiles / finishes  \n• Egypt location across EU/GCC/Africa  \n• Export packing/documentation story')
        gold_header('Opportunities')
        st.markdown('• Recurring importer programmes  \n• European technical/value positioning  \n• GCC project supply  \n• Granite monument segment  \n• African country-distributor model')
    with b:
        gold_header('Weaknesses')
        st.markdown('• Digital trust inconsistencies  \n• Proof assets need stronger organization  \n• Technical claims need lab/document backing  \n• Generic “premium marble” messaging  \n• RFQ journey needs stronger conversion design')
        gold_header('Threats')
        st.markdown('• Turkey: proximity + processing  \n• India/Brazil: granite scale  \n• Italy: premium brand equity  \n• China: pricing/scale  \n• Spain/Portugal/Greece: Mediterranean competition')
    gold_header('Recommended positioning architecture')
    st.markdown("""<div class='hero' style='margin-top:8px'><div class='kicker'>MASTER POSITION</div><h1 style='font-size:1.75rem'>STYLE — Reliable Egyptian Stone Supply.</h1><p><b>Distributor:</b> Built for importers who need consistent Egyptian stone, not one-off shipments.<br><b>Projects:</b> Project-ready marble & granite — cut, finished, inspected and export-prepared.<br><b>Design:</b> Distinctive Egyptian stone for architecture that needs material identity.</p></div>""",unsafe_allow_html=True)

elif page=='Evidence & Methodology':
    st.markdown("""**How to read the dashboard**  
- **Verified evidence:** public trade/company sources linked below.  
- **Strategic inference:** STYLE-specific market prioritization derived from demand, price/value, Egypt fit, logistics, buyer density and competitive opportunity.  
- **Scenario:** user-adjustable planning model, not a forecast.  
- **Needs verification:** tariffs, customs treatment, lab claims, buyer contacts and shipment-level activity before execution.""")
    gold_header('Selected trade evidence')
    ev=pd.DataFrame(EVIDENCE)
    st.dataframe(ev[['market','metric','value','note']],use_container_width=True,hide_index=True)
    for s,u in SOURCES: st.markdown(f"• [{s}]({u})")
    gold_header('EAI 2.0 weighting')
    weights=pd.DataFrame({'Factor':['Import demand','Import unit value / price quality','Existing Egyptian product proof','Construction / project demand','Logistics from Egypt','Trade agreement / tariff access','Buyer density','Competition opportunity','Commercial/payment risk'],'Weight %':[25,15,15,10,10,10,8,4,3]})
    fig=px.bar(weights.sort_values('Weight %'),x='Weight %',y='Factor',orientation='h',color='Weight %',color_continuous_scale=['#59624B','#C6A466'])
    fig.update_layout(height=430,coloraxis_showscale=False,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font_color='#ddd',xaxis=dict(gridcolor='rgba(255,255,255,.06)'))
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})

st.divider()
st.caption('STYLE Global Export Intelligence 100 • Strategy model for B2B export prioritization • Built for decision support, not guaranteed outcomes.')
