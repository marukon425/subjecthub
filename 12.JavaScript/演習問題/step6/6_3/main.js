const rootElm = document.getElementById('areaSelector');

async function initAreaSelector() {
    await updatePref();
    await updateCity();
}

async function getPrefs() {
    const prefResponse = await fetch('./prefectures.json');
    return await prefResponse.json();
}

async function getCities(prefCode) {
    const cityResponse = await fetch(`./cities/${prefCode}.json`);
    return await cityResponse.json();
}

async function updatePref() {
    const prefs = await getPrefs();
    createPrefOptionsHtml(prefs);
}

async function updateCity() {
    const prefSelectorElm = rootElm.querySelector('.prefectures');
    const cities = await getCities(prefSelectorElm.value);
    createCityOptionsHtml(cities);
}

function createPrefOptionsHtml(prefs) {
    const optionStrs = [];
    for (const pref of prefs) {
        optionStrs.push(`
<option name="${pref.name}" value="${pref.code}">${pref.name}</option>
`);
    }

    const prefSelectorElm = rootElm.querySelector('.prefectures');
    prefSelectorElm.innerHTML = optionStrs.join('');

    prefSelectorElm.addEventListener('change', (event) => {
        updateCity();
    });
}

function createCityOptionsHtml(cities) {
    const optionStrs = [];
    var name = '';
    for (const city of cities) {
        name = '<strong>' + city.name + '</strong>';
    }

    var element = document.getElementById('innerTest');
    element.innerHTML = name;
}

initAreaSelector();
