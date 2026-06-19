// asyncでawaiをつかえるようにする
async function displayMessage() {
    // await(非同期処理が終わるまで待つ)でjsonファイルを持ってくる
    const response = await fetch('./hello.json');
    // jsonファイルをデータに変換
    const data = await response.json();
    // jsonをhtmlに入れる
    const messageElm = document.getElementById('message')
    messageElm.innerHTML = data.meessage;
    console.log('終了')
}

console.log('開始前');
displayMessage();
console.log('開始後');


// コード上で見る出力結果 ✕
// 開始前 → 終了 → 開始後

// コンソール上の出力 〇
// 開始前 → 開始後 → 終了