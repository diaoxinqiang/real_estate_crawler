import pandas as pd
import pyecharts



class analysis:
    data = pd.read_csv("houses.csv")
    def __init__(self):
        self.data['area'] = self.data['area'].str.replace(u'平米', '')
        self.data['area'] = self.data['area'].astype('float')
        # 去掉房屋面积中「平米」并保存为浮点型
        self.data['unit-price'] = self.data['price'] / self.data['area']
        # 生成每平方米房屋单价
        self.data = self.data.round(1)
        self.data.head()






    def run(self):
        # self.area_and_prices()
        self.areas_price_distribution()

    def areas_price_distribution(self):

        temp = self.data.groupby(['area_positon'])['unit-price'].mean().reset_index()
        temp = temp.round(1)
        attr = list(temp['area_positon'])
        value = list(temp['unit-price'])

        map = pyecharts.Map("深圳各行政区二手房均价", "统计时间：2018-09-22", width=800, height=600)
        map.add(
            "二手房均价(单位：万元)", attr, value, maptype=u"深圳", is_legend_show=False, is_label_show=True,
            is_visualmap=True, visual_text_color="#000", visual_range=[3, 8]
        )
        map.render()

    def filter(self):
        data = pd.read_csv("2.csv")
        # bool =   data['area'].str.match('.*?平米')
        # filter_data = data[bool]
        # print(filter_data)
        data = data[data['area'].str.match('.*?平米').str.len() > 0]
        data.to_csv('lianjia.csv', encoding='utf-8-sig')

    def area_and_prices(self):

        scatter = pyecharts.Scatter("总价-面积散点图", '统计时间：2018-9-30')
        scatter.add('🏠总价(单位：万元)', self.data['area'], self.data['price'], is_legend_show=False,
                    visual_pos='right',
                    is_visualmap=True, visual_type="color", visual_range=[100, 1000],
                    mark_point=['max'],
                    xaxis_name='面积', yaxis_name='总价')
        scatter.render()


if __name__ == '__main__':
    analysis = analysis()
    # analysis.filter()
    analysis.run()
