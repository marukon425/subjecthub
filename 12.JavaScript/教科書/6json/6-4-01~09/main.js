// 地域セレクタ全体を囲むdiv要素を取得
const rootElm = document.getElementById('areaSlector');

// ページ読み込み時に都道府県と市区町村を初期表示する
async function initAreaSelecter() {
    await updatePref();
    await updateCtiy();
}

// prefectures.json から都道府県一覧を取得して返す
async function getPrefs() {
    // prefectures.jsonかデータを拾う
    const prefResponse = await fetch('./prefectures.json');
    // データとして使えるようにして戻り値にする
    return await prefResponse.json();
}

// 選択中の都道府県コードに対応する市区町村JSONを取得して返す
async function getCities(prefCode) {
    const cityResponse = await fetch(`./cties/${prefCode}.json`);
    return await cityResponse.json();
}

// 都道府県セレクタを更新する（データ取得→HTML生成）
async function updatePref(){
    // データを拾ってくる
    const prefs = await getPrefs();

    // htmlのリストにする
    createPrefOptionsHtml(prefs)
}

// 市区町村セレクタを更新する（現在選択中の都道府県を元にデータ取得→HTML生成）
async function updateCtiy() {
    const prefSelectorElm = rootElm.querySelector('.prefectures');
    const cities = await getCities(prefSelectorElm.value);
    createCityOptionsHtml(cities);
}


// 個々がメインの処理
// 都道府県の<option>要素を生成してセレクタに流し込む
// 都道府県が変更されたら市区町村を再取得するイベントも登録する
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

// 市区町村の<option>要素を生成してセレクタに流し込む
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
