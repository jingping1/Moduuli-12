import requests


def hae_saa():
    # ！！！请在这里填入你从官网申请到的 API Key ！！！
    api_key = "你的_OPENWEATHER_API_KEY"

    paikkakunta = input("Syötä paikkakunnan nimi: ")

    # 构造请求 URL
    # q 是城市名，appid 是你的密钥，units=metric 是直接要求返回摄氏度
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric"

    try:
        vastaus = requests.get(url)

        # 如果返回码是 200 表示成功
        if vastaus.status_code == 200:
            data = vastaus.json()

            # 提取天气描述和温度
            saa_kuvaus = data['weather'][0]['description']
            lampotila = data['main']['temp']

            print(f"Sää paikassa {paikkakunta}: {saa_kuvaus}")
            print(f"Lämpötila: {lampotila:.1f} °C")
        else:
            print("Paikkakuntaa ei löytynyt tai virhe pyynnössä.")

    except Exception as e:
        print(f"Virhe haettaessa säätietoja: {e}")


if __name__ == "__main__":
    hae_saa()