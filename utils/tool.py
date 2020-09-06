import base64
import random
from datetime import datetime
from io import BytesIO

from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

def gen_trans_id():
    now = datetime.now()
    str_date = now.strftime('%Y%m%d%H%M%S%f')
    return str_date + str(random.randint(1000, 9999))

def draw_picture(x, y):
    fig = plt.figure(figsize=(9, 4)) # 设置画布大小
    plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.xticks(rotation=-90)
    plt.tick_params(axis='x', labelsize=8)    # 设置x轴标签大小
    plt.bar(x, y)
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64,"+ims
    # print(imd)
    # plt.show()
    plt.close(fig)
    return imd