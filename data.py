from __future__ import annotations

MARKETS = [
('Saudi Arabia',97),('United States',95),('France',93),('Kuwait',92),('Morocco',91),('Germany',89),('United Kingdom',89),('Australia',88),('Canada',87),('Turkey',87),
('Romania',86),('South Korea',85),('Switzerland',85),('United Arab Emirates',84),('Algeria',84),('Poland',83),('Japan',83),('Italy',82),('Spain',81),('Netherlands',81),
('Belgium',80),('Qatar',80),('Oman',79),('Bulgaria',79),('Greece',79),('China',78),('Cyprus',78),('Mexico',77),('India',77),('Lebanon',76),
('Austria',76),('Sweden',75),('Norway',75),('Denmark',74),('Czechia',74),('Portugal',74),('Ireland',73),('Hong Kong',73),('Singapore',73),('Malaysia',72),
('Taiwan',72),('New Zealand',72),('Bahrain',71),('Jordan',71),('Iraq',70),('Israel',70),('Brazil',70),('Colombia',69),('Chile',69),('Peru',69),
('South Africa',68),('Kenya',68),('Ghana',67),('Nigeria',67),("Côte d’Ivoire",67),('Senegal',66),('Cameroon',66),('Tanzania',66),('Rwanda',65),('Zambia',65),
('Uganda',65),('Mauritius',64),('Libya',64),('Tunisia',64),('Ethiopia',63),('Djibouti',63),('Angola',63),('Mozambique',62),('Kazakhstan',62),('Azerbaijan',62),
('Georgia',61),('Dominican Republic',61),('Panama',61),('Costa Rica',60),('Uruguay',60),('Argentina',60),('Philippines',59),('Indonesia',59),('Thailand',59),('Vietnam',58),
('Cambodia',58),('Lithuania',58),('Latvia',57),('Estonia',57),('Slovakia',57),('Slovenia',56),('Croatia',56),('Serbia',56),('Hungary',55),('Finland',55),
('Malta',55),('Iceland',54),('Bahamas',54),('Uzbekistan',54),('Botswana',53),('Namibia',53),('Zimbabwe',53),('Madagascar',52),('Equatorial Guinea',52),('Guinea',52)
]

PRODUCTS = {
    'Sunny Light': {
        'family':'Marble','role':'Volume Driver','best_for':'Flooring, walls, residential & commercial projects',
        'positioning':'Reliable Egyptian beige marble for repeat stock and project quantities',
        'markets':['Saudi Arabia','Kuwait','Morocco','France','United Arab Emirates','United Kingdom','Romania','Algeria']
    },
    'Sunny Minya': {
        'family':'Marble','role':'Volume + Project Driver','best_for':'Large floors, façades, public/commercial projects',
        'positioning':'Project-ready Egyptian beige with scalable supply economics',
        'markets':['Saudi Arabia','Kuwait','Morocco','Qatar','Oman','Algeria','Jordan','Iraq']
    },
    'Galala Light': {
        'family':'Marble','role':'Export Hero','best_for':'Interior architecture, hospitality, floors and walls',
        'positioning':'Recognizable Egyptian cream stone with strong distributor and project appeal',
        'markets':['France','Saudi Arabia','United States','Canada','Australia','United Kingdom','Germany','Morocco']
    },
    'Meli Grey': {
        'family':'Marble','role':'Premium Design','best_for':'Contemporary interiors, architects, boutique projects',
        'positioning':'Distinctive Egyptian grey marble for design-led, higher-value specifications',
        'markets':['France','Germany','United Kingdom','Switzerland','Australia','Canada','United States','Netherlands']
    },
    'New Halayeb Granite': {
        'family':'Granite','role':'Commercial / Heavy-use','best_for':'Exterior, stairs, flooring, landscape, commercial projects',
        'positioning':'Durable Egyptian granite for heavy-use and repeat project supply',
        'markets':['Germany','Poland','United States','Japan','South Korea','Turkey','Romania','United Kingdom']
    },
    'Ramady El Sherka Granite': {
        'family':'Granite','role':'Premium Commercial','best_for':'Modern architecture, monuments, landscape and façades',
        'positioning':'Contemporary Egyptian grey granite for architectural and monumental applications',
        'markets':['Germany','Switzerland','United Kingdom','Poland','Netherlands','Belgium','Japan','Canada']
    },
}

TOP_DETAILS = {
'Saudi Arabia':('Projects + importers','Sunny Minya, Galala, New Halayeb','Project reliability + volume + fast regional logistics','Very High','High','Strong'),
'United States':('Slab distributors + fabricators','Galala, Meli Grey, New Halayeb','Distinctive Egyptian materials + distributor margin','Very High','Premium','Medium'),
'France':('Importers + distributors + marbriers','Galala, Sunny Light, Meli Grey','Mediterranean supply + EU access + consistency','High','Premium','Strong'),
'Kuwait':('Importers + project suppliers','Sunny Minya, Galala, New Halayeb','Proven Egyptian origin + project/value fit','High','High','Strong'),
'Morocco':('Importers + construction suppliers','Sunny, Galala, New Halayeb','Egyptian stone proof + volume economics','High','Mid-High','Strong'),
'Germany':('Granite importers + wholesalers + monuments','New Halayeb, Ramady El Sherka, Meli Grey','Technical reliability + granite + documentation','High','High','Strong'),
'United Kingdom':('Stone yards + importers + fabricators','Galala, Meli Grey, Ramady','Premium stock + consistent repeat supply','High','Premium','Strong'),
'Australia':('Premium distributors + project suppliers','Galala, Meli Grey','Premium Egyptian collection + higher-value positioning','High','Premium','Medium'),
'Canada':('Slab distributors + fabricators','Galala, Meli Grey, New Halayeb','Premium stock + repeat container supply','High','Premium','Medium'),
'Turkey':('Processors + importers','New Halayeb, Ramady, blocks/slabs','Processor economics + direct Egyptian source','High','Mid','Very Strong'),
'Romania':('Importers + stone distributors','New Halayeb, Galala, Sunny','Existing Egyptian granite fit + distributor supply','High','Mid-High','Very Strong'),
'South Korea':('Stone importers + processors','New Halayeb, Galala','Quality consistency + material differentiation','High','High','Strong'),
'Switzerland':('Premium importers + monuments','Ramady, Meli Grey, Galala','High-value architecture + technical confidence','Medium','Very Premium','Medium'),
'United Arab Emirates':('Project suppliers + developers','Sunny, Galala, Meli Grey','Project-ready stone + GCC logistics','High','High','Strong'),
'Algeria':('Importers + construction distributors','Sunny Minya, Galala','Strong Egyptian marble fit + volume','High','Mid','Very Strong'),
'Poland':('Granite wholesalers + monuments','New Halayeb, Ramady','Granite + monuments + EU distribution','High','High','Medium'),
'Japan':('Premium granite importers','New Halayeb, Ramady','Technical granite positioning + premium QC','High','Premium','Medium'),
'Italy':('Processors + block/slab traders','Blocks, Galala, Granite','Quarry economics + processing supply','High','Mid-High','Medium'),
'Spain':('Processors + stone distributors','Galala, Sunny, Meli Grey','Alternative Mediterranean source + margins','Medium-High','High','Medium'),
'Netherlands':('EU wholesalers + distribution hubs','Meli Grey, Galala, Granite','EU hub + stock/distribution economics','Medium-High','High','Medium'),
}

EVIDENCE = [
    {'market':'Saudi Arabia','metric':'HS 680221 imports (2024)','value':'~$370.3M','note':'Large cut/sawn stone demand; category-specific evidence','url':'https://wits.worldbank.org/trade/comtrade/en/country/SAU/year/2024/tradeflow/Imports/partner/ALL/product/680221'},
    {'market':'United States','metric':'HS 680291 imports (2024)','value':'~$1.278B','note':'Very large worked-marble market','url':'https://wits.worldbank.org/trade/comtrade/en/country/USA/year/2024/tradeflow/Imports/partner/ALL/product/680291'},
    {'market':'United States','metric':'HS 680293 imports (2024)','value':'~$722.5M','note':'Very large worked-granite market','url':'https://wits.worldbank.org/trade/comtrade/en/country/USA/year/2024/tradeflow/Imports/partner/ALL/product/680293'},
    {'market':'France','metric':'HS 680291 imports (2024)','value':'~$109.7M','note':'Large worked-marble import market','url':'https://wits.worldbank.org/trade/comtrade/en/country/FRA/year/2024/tradeflow/Imports/partner/ALL/product/680291'},
    {'market':'Germany','metric':'HS 680293 imports (2024)','value':'~$175.1M','note':'Large worked-granite import market','url':'https://wits.worldbank.org/trade/comtrade/en/country/DEU/year/2024/tradeflow/Imports/partner/ALL/product/680293'},
    {'market':'Australia','metric':'HS 680291 imports (2024)','value':'~$104.8M','note':'High-value worked-marble market','url':'https://wits.worldbank.org/trade/comtrade/en/country/AUS/year/2024/tradeflow/Imports/partner/ALL/product/680291'},
    {'market':'Turkey','metric':'Egypt-origin HS 680293 (2024)','value':'~$17.4M','note':'Strong direct proof of Egyptian granite demand','url':'https://wits.worldbank.org/trade/comtrade/en/country/TUR/year/2024/tradeflow/Imports/partner/EGY/product/680293'},
    {'market':'Romania','metric':'Egypt-origin HS 680293 (2024)','value':'~$7.36M','note':'Direct proof of Egyptian granite demand','url':'https://wits.worldbank.org/trade/comtrade/en/country/ROU/year/2024/tradeflow/Imports/partner/EGY/product/680293'},
]

SOURCES = [
    ('STYLE Website','https://styleformarble.com/'),
    ('EU–Egypt trade relationship','https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/egypt_en'),
    ('COMESA Trade & Customs','https://www.comesa.int/trade-customs-division-2/'),
    ('WITS / UN Comtrade','https://wits.worldbank.org/'),
]
