// asyncでawaiをつかえるようにする
async function displayMessage() {
    // await(非同期処理が終わるまで待つ)でjsonファイルを持ってくる
    const response = await fetch('./hello.json');
    // jsonファイルをデータに変換
    const data = await response.json();
    // jsonをhtmlに入れる
    const messageElm = document.getElementById('message')
    messageElm.innerHTML = data.meessage;
}

displayMessage();