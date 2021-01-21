from datetime import datetime, timedelta
import time


class Tool(object):
    """
    工具类
    """
    def __init__(self):
        pass

    # 格式化输出时间
    def format_time(self, year=1970, month=1, day=1, t_str='', m=False):
        n = datetime.now()
        d = datetime(year=year, month=month, day=day)
        if m:
            s = datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S.%f')  # 精确到微秒
        else:
            s = datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
        return s.strftime("%Y-%m-%d %H:%M:%S")

    # 时间对象运算
    def cal_time(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        n = datetime.now()
        t = n + timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)
        return t

    # 时间戳 time.time()
    def unix_time(self):
        n = datetime.now()
        un_time = time.mktime(n.timetuple())
        t = datetime.fromtimestamp(un_time)
        return un_time

    def run_time(self, m, p):
        """
        :param m: 分钟
        :param p: 次数
        :return:
        """
        n = time.mktime(datetime.now().timetuple())
        i = 1
        while True:
            t = time.mktime(datetime.now().timetuple())
            if t == n + (m * 60) * i:
                print(i)
                i = i + 1
            else:
                time.sleep(1)
            if (i-1) == p:
                break


if __name__ == '__main__':
    tool = Tool()
    tool.run_time(1, 2)