from operator import truediv
from django_echarts.entities import Jumbotron, LinkItem
from django_echarts.starter.sites import DJESite, SiteOpts
from django.urls import reverse_lazy
from pyecharts import options as opts

from pyecharts.charts import Kline
from pyecharts.charts import Bar3D
from static.AnualEPS import listYearFirmEPS, TOP5_EQUITY_EPS
from static.histdatascrape import Techlist, Finlist

site_obj = DJESite(
    site_title='Mini Honours Project',
    
    opts=SiteOpts(
        list_layout='grid',
        nav_shown_pages=[],
        paginate_by=10,
        #detail_tags_position = 'bottom'
    )
)

site_obj.nav.add_menu(text='About', slug='about', url=reverse_lazy('dje_home'))

site_obj.add_widgets(
    jumbotron=Jumbotron('S&P 500 data visualistion', main_text='mini group project - University of Edinburgh', small_text='10/2022'),
)

site_obj.add_right_link(
    LinkItem(text='Project Repo', url='https://github.com/YongjiangChen/miniProject', new_page=True)
)

candleStickDescription = 'This Chart displays prices in real-time, you may click/scroll to move/zoom. The S&P 500® Information Technology comprises those companies included in the S&P 500 that are classified as members of the GICS information technology sector.'
candleStickDescription2 = 'This Chart displays prices in real-time, you may click/scroll to move/zoom. The S&P 500 Financials comprises those companies included in the S&P 500 that are classified as members of the GICS financials sector.'

#########################################################################################################
#make-up data, need to append real data from json dictionary to list of lists.
# [open, close, lowest, highest] 
prices = [[2320.26, 2320.26, 2287.3, 2362.94]]
columnAverage = [sum(priceList) / len(priceList) for priceList in zip(*prices)],
max_value = max(sublist[0] for sublist in prices)
###########################################################################################################


def findDay(theList, price):
    for ind in range(len(theList)):
        if price in theList[ind]:
            return ind

max_value_day = findDay(prices, max_value)
#print(max_value_day)

timeAxis = []
for i in range(9,17):
    if i == 9:
        for j in range(30,60,5):
            timeAxis.append(str(i)+":"+str(j))
    elif i>9 and i<16:
        for j in range(0,60,5):
            timeAxis.append(str(i)+":"+str(j))
    else:
        for j in range(0,35,5):
            timeAxis.append(str(i)+":"+str(j))


@site_obj.register_chart(title='Intraday prices for S&P 500 Information Technology Sector', description = candleStickDescription, catalog='Data Visualisation')
def mytechchart():
    candleStick = Kline().add_xaxis(
        [timeAxis[i] for i in range(len(Techlist))]
    ).add_yaxis(
        'Candlestick Prices', Techlist, itemstyle_opts=opts.ItemStyleOpts(color="#8fce00", color0="#ff3a3a", border_color="#8fce00", border_color0="#ff3a3a"),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="INDEXSP: SP500-45", subtitle="Time interval: 5-min"),
        datazoom_opts=opts.DataZoomOpts(is_show = True, type_ = "inside", orient = "horizontal", range_start=1, range_end=200)).set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_ = 'average', value_dim='close', name="Close Price Average",)
                #opts.MarkLineItem(y=columnAverage[0][1], name="Overall Close Price Average",)
            ],
            linestyle_opts=opts.LineStyleOpts( width = 2, type_ = "dashed", color="#5b5b5b")
        ),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_='max', value_dim='highest',  value=max_value, symbol_size=[80,50], name="Highest Price", itemstyle_opts=opts.ItemStyleOpts(color="#5b5b5b")),
                #opts.MarkPointItem(coord=(max_value_day,max_value), value=max_value, symbol_size=[80,50], name="Overall Highest Price"),
            ]
        ),
    )
    return candleStick

@site_obj.register_chart(title='Intraday prices for S&P 500 Financials Sector', description = candleStickDescription2, catalog='Data Visualisation')
def myfinchart():
    candleStick2 = Kline().add_xaxis(
        [timeAxis[i] for i in range(len(Techlist))]
    ).add_yaxis(
        'Candlestick Prices', Finlist, itemstyle_opts=opts.ItemStyleOpts(color="#8fce00", color0="#ff3a3a", border_color="#8fce00", border_color0="#ff3a3a"),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="INDEXSP: SP500-40", subtitle="Time interval: 5-min"),
        datazoom_opts=opts.DataZoomOpts(is_show = True, type_ = "inside", orient = "horizontal", range_start=1, range_end=200)).set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_ = 'average', value_dim='close', name="Close Price Average",)
                #opts.MarkLineItem(y=columnAverage[0][1], name="Overall Close Price Average",)
            ],
            linestyle_opts=opts.LineStyleOpts( width = 2, type_ = "dashed", color="#5b5b5b")
        ),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_='max', value_dim='highest',  value=max_value, symbol_size=[80,50], name="Highest Price", itemstyle_opts=opts.ItemStyleOpts(color="#5b5b5b")),
                #opts.MarkPointItem(coord=(max_value_day,max_value), value=max_value, symbol_size=[80,50], name="Overall Highest Price"),
            ]
        ),
    )
    return candleStick2

description3D = "This page illustrate the EPS change in the TOP 5 S&P 500 entities over past 10 years, together they make up 17.5% of the S&P 500"

#years = ["2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
equities = ["Apple", "Microsoft", "Alphabet", "Amazon", "Meta"]

@site_obj.register_chart(title='Earnings per share', description = description3D, catalog='Data Visualisation')
def Bar3Dchart():
    c=(
    Bar3D(init_opts=opts.InitOpts(width="900px", height="600px", bg_color="#f3f6f4",))
    .add(
        series_name="Earnings Per Share",
        #data=listYearFirmEPS,
        data = TOP5_EQUITY_EPS,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", name='Years',),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=equities, name='Top 5 Entities in S&P500', name_gap =40),
        zaxis3d_opts=opts.Axis3DOpts(type_="value", name='EPS'),
        grid3d_opts=opts.Grid3DOpts(is_rotate=True)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="3D Visualistion for change in Profitability", subtitle="Unit: USD"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )

)
    return c



