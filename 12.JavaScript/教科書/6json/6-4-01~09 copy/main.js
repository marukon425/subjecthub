const rootElm = document.getElementById('areaSlector');

async function initAreaSelecter() {
    await updatePref();
    await updateCtiy();
}

async function getPrefs() {
    // prefectures.jsonかデータを拾う
    const prefResponse = await fetch('./prefectures.json');
    // データとして使えるようにして戻り値にする
    return await prefResponse.json();
}

async function getCities(prefCode) {
    const cityResponse = await fetch(`./cties/${prefCode}.json`);
    return await cityResponse.json();
}

// async function displayPrefs() {
//     const result = await getPrefs();
//     console.log(result)
// }
async function updatePref(){
    // データを拾ってくる
    const prefs = await getPrefs();

    // htmlのリストにする
    createPrefOptionsHtml(prefs)
}

async function updateCtiy() {
    const prefSelectorElm = rootElm.querySelector('.prefectures');
    const cities = await getCities(prefSelectorElm.value);
    createCityOptionsHtml(cities);
}

function createPrefOptionsHtml(prefs){
    const optionStrs = [];

    // ここのfor文はpythonで言うと「for i in list」みたいな感じの書き方
    for (const pref of prefs){
        // jsonから拾ってきたデータをhtmlのリストに入れていく
        optionStrs.push(`
            <option name="${pref.name}" value="${pref.code}">
                ${pref.name}
            </option>
            `)
    }

    // リストの親リストを指定
    const prefSelectElm = rootElm.querySelector('.prefectures');
    // すだれのリストを代入
    prefSelectElm.innerHTML = optionStrs.join('');

    prefSelectElm.addEventListener('change', (event) => {
        updateCtiy();
    });
}

function createCityOptionsHtml(cities) {
    const optionStrs = [];
    for(const city of cities) {
        optionStrs.push(`
        <option name="${city.name}" value="${city.code}">
            ${city.name}
        </option>
        `);
    }

    const citySelectorElm = rootElm.querySelector('.cities');
    citySelectorElm.innerHTML = optionStrs.join('');

}


// displayPrefs()
// つかえるようにする
// updatePref();
initAreaSelecter();

rootElm.querySelector('.prefectures').addEventListener('change', updateCtiy);