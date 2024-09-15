import requests
from datetime import datetime, timedelta


def reserveSeats():
    # 获取第推迟一天的时间
    tomorrow = (datetime.now() + timedelta(1)).date()
    today = datetime.now().date()
    # 获取时间戳
    tomorrow_timestamp = datetime.combine(tomorrow, datetime.min.time()).timestamp()  # 第二天零点的时间戳
    today_timestamp = datetime.combine(today, datetime.min.time()).timestamp()

    # 预约哪个时间点 07：00-20:00 ; 预约多久 0-6h
    beginTime = int(tomorrow_timestamp) + 8 * 3600
    duration = 6 * 3600
    seats = ["18110", "18082"]  # 18110对应的是348座，每个座位在此基础上加减2，有部分座位不太一样，懒得搞了
    seatBookers = ["282797", "281901"]  # xxx、 me  这是每个人的账号，这个必须抓包才能拿到，到现在没找到别的方法，将就一下用吧
    # 现在还没能实现cookie的自动化，主要是没时间搞，不然必拿下它好吧！
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 NchuApp/1.0.16 NetType/4G MicroMessenger/8.0.32.2300",
        "Cookie": "auth=9fd1EMV69z8FpUWKIroTwSRaP9vFar_8_70W9t0dMV-JHuY_tT3LL0OVoH4Arft6XVOXHGVBHZhOSHqg;uid=f962zwW5z5_DT3KxDgo9a3sCfvyJw51lK8m-NtPTu0;"
    }

    data = {
        "beginTime": beginTime,
        "duration": duration,
        "seats[0]": seats[0],
        "seatBookers[0]": seatBookers[0],
        "seats[1]": seats[1],
        "seatBookers[1]": seatBookers[1],
    }

    r = requests.post("http://lib-zw.lib.nchu.edu.cn/Seat/Index/bookSeats?LAB_JSON=1", data=data, headers=headers)
    print(r.json())

    with open("log.txt", "a", encoding="utf8") as f:
        f.write(str(r.json()["MESSAGE"])+"\t")
        if str(r.json()["DATA"]["result"]) != "fail":
            f.write("bookingId: "+str(r.json()["DATA"]["bookingId"]))
        f.write("\n")
        f.close()
    # print(beginTime)
    return 0


if __name__ == '__main__':
    reserveSeats()
