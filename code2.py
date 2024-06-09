import requests
import smtplib
import email.utils
from email.mime.text import MIMEText


# 获取成都天气信息
def get_weather():
    url = "https://cn.apihz.cn/api/tianqi/tqyb.php?id=88888888&key=88888888&sheng=四川&place=成都"
    response = requests.get(url)
    weather_data = response.json()
    weather_info = (
        f"城市: 成都\n"
        f"温度: {weather_data['temperature']}°C\n"
        f"风速: {weather_data['windSpeed']} km/h\n"
        f"湿度: {weather_data['humidity']}%\n"
    )
    return weather_info


if __name__ == "__main__":
    weather_info = get_weather()
    message = MIMEText(weather_info)
    message["To"] = email.utils.formataddr(("接收者", "xxxx@qq.com"))
    message["From"] = email.utils.formataddr(("发送者", "xxxx@qq.com"))
    message["Subject"] = "今日天气"
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login("xxxxxx@qq.com", "tklwdfcd")
    server.set_debuglevel(True)
    try:
        server.sendmail("xxxxx@qq.com", ["xxx@qq.com"], msg=message.as_string())
    finally:
        server.quit()
