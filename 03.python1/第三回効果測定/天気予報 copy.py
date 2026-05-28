import requests
from datetime import datetime

def get_weather(city_name):
    try:
        conversion_city_cods = {
        '北海道': '016010',
        '青森県': '020010',
        '岩手県': '030010',
        '宮城県': '040010',
        '秋田県': '050010',
        '山形県': '060010',
        '福島県': '070010',
        '茨城県': '080010',
        '栃木県': '090010',
        '群馬県': '100010',
        '埼玉県': '110010',
        '千葉県': '120010',
        '東京都': '130010',
        '神奈川県': '140010',
        '新潟県': '150010',
        '富山県': '160010',
        '石川県': '170010',
        '福井県': '180010',
        '山梨県': '190010',
        '長野県': '200010',
        '岐阜県': '210010',
        '静岡県': '220010',
        '愛知県': '230010',
        '三重県': '240010',
        '滋賀県': '250010',
        '京都府': '260010',
        '大阪府': '270000',
        '兵庫県': '280010',
        '奈良県': '290010',
        '和歌山県': '300010',
        '鳥取県': '310010',
        '島根県': '320010',
        '岡山県': '330010',
        '広島県': '340010',
        '山口県': '350010',
        '徳島県': '360010',
        '香川県': '370000',
        '愛媛県': '380010',
        '高知県': '390010',
        '福岡県': '400010',
        '佐賀県': '410010',
        '長崎県': '420010',
        '熊本県': '430010',
        '大分県': '440010',
        '宮崎県': '450010',
        '鹿児島県': '460010',
        '沖縄県': '471010'
        }
        city = conversion_city_cods[city_name]
        url = f"https://weather.tsukumijima.net/api/forecast?city={city}"
        response  = requests.get(url)
        response.raise_for_status()

        data_json = response.json()
    
        date_str = data_json["forecasts"][1]["date"]
        date = datetime.strptime(date_str,"%Y-%m-%d").strftime("%Y年%m月%d日")
        title = data_json["title"]
        weather = data_json["forecasts"][1]["telop"]
        max_temp = data_json["forecasts"][1]["temperature"]["max"]["celsius"]
        min_temp = data_json["forecasts"][1]["temperature"]["min"]["celsius"]
        
        results = f"{date}の{city_name}の天気は{weather}です。\n最高気温は{max_temp}度、最低気温は{min_temp}度です。"
        return results
    
    except requests.exceptions.RequestException as e:
        return f"正しい都道府県名を入力してください: {e}"
        
    except KeyError as e:
        return f"予期しないデータ形式です: {e}"
    


print('天気予報を起動します')
try_serch = 'yes'
while True:
    if try_serch == str('yes'):
        city_number = input("正式な都道府県名を入力してください")
        # 検索結果を表示
        result = get_weather(city_number)
        print(result)
        
        # もう一度使うか聞く
        try_serch = input('まだほかのの天気予報を検索しいですか？yes/no')
        # noだった場合繰り返し処理を終了させる
    elif try_serch == str('no'):
        break
    else:
        try_serch = str(input('yesかnoで答えてください'))
print('天気予報を終了します')
# まだほかの機能を使うか聞く
try_function = input('まだほかの機能を使いますか？yes/no>>>')
try_function_flg_flg = True
if try_function == 'yes':
    None
elif try_function == 'no':
    try_function_flg = False
else:
    while try_function_flg_flg == True:
        try_game = input('yesかnoで答えてください>>>')
        if try_function == 'yes':
            try_function_flg_flg = False
        elif try_function == 'no':
            try_function_flg_flg = False
            try_function_flg = False