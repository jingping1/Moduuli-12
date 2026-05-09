import requests


def hae_chuck_norris_vitsi():
    # 接口地址
    url = "https://api.chucknorris.io/jokes/random"

    try:
        # 发送请求
        vastaus = requests.get(url)
        # 将返回的 JSON 转换为 Python 字典
        data = vastaus.json()

        # 题目要求只显示笑话文本（键名为 'value'）
        print(data['value'])

    except Exception as e:
        print(f"Haku epäonnistui: {e}")


if __name__ == "__main__":
    hae_chuck_norris_vitsi()