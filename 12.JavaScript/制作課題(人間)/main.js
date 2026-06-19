
// 都市名を格納してる変数
let citiesData = [];
fetch('./cities.json')
    .then(res => res.json())
    .then(data => {
        citiesData = data;
    })
    .catch(err => {
        alert('都市名の取得に失敗!');
    });

// APIを使って天気予報を調べる
function fetchWeather(lat, lon) {
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,weathercode,windspeed_10m,relativehumidity_2m,apparent_temperature&hourly=temperature_2m,weathercode&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=Asia%2FTokyo&forecast_days=7`;

    fetch(url)
        .then(res => res.json())
        .then(data => {
            // 現在の天気
            const current = data.current;
            console.log(`現在の気温：${current.temperature_2m}`);// 気温
            console.log(`現在の体感温度：${current.apparent_temperature}`);// 体感温度
            console.log(current.weathercode);          // 天気コード
            console.log(current.windspeed_10m);        // 風速
            console.log(current.relativehumidity_2m);  // 湿度

            // 週間予報
            const daily = data.daily;
            console.log(daily.time);              // ['2026-06-19', '2026-06-20', ...]
            console.log(daily.temperature_2m_max); // [29.4, 31.2, ...]
            console.log(daily.temperature_2m_min); // [22.1, 23.4, ...]
            console.log(daily.weathercode);        // [1, 2, ...]

            // 時間別予報（168件 = 7日×24時間）
            const hourly = data.hourly;
            console.log(hourly.time[0]);          // '2026-06-19T00:00'
            console.log(hourly.temperature_2m[0]); // その時間の気温
        })
        .catch(err => {
            alert('天気の取得に失敗!');
        });
}

// 都市の検索結果を出力する
function disResult(filtered = []) {
    const result_box = document.getElementById("result");
    result_box.innerHTML = "";

    filtered.forEach(city => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${city.prefecture} ${city.name}
            <input type="hidden" class="result-city-name" value="${city.name}">
        `;
        
        li.addEventListener("click", (e) => {
            const clickedLi = e.currentTarget;
            const hiddenInput = clickedLi.querySelector(".result-city-name");
            document.getElementById("search-city").value = hiddenInput.value
            disResult();
            fetchWeather(city.lat, city.lon);
        });
        
        result_box.appendChild(li);
    });
}

// 入力されたらリアルタイムで出力
const search_city = document.getElementById("search-city");
search_city.addEventListener("input", () => {
    const query = search_city.value;

    if (query === "") {
        disResult();
        return;
    }

    // citiesDataからqueryが含まれるものだけ抽出
    const filtered = citiesData.filter(city =>
        city.name.includes(query)
    );

    disResult(filtered);
});
