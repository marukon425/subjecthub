
// asyncを使うことでawaitが使える
async function displayMessage(params) {

    // hello.jsonからデータを取ってくる
    // await：fetchが終わるまで次の行を実行しない。
    const response = await fetch('./hello.json');

    // response：サーバーから帰ってきた結果を変数に代入する
    const data = await response.json();
    const messageElm = document.getElementById("message");
    messageElm.innerHTML = data.message
}

displayMessage();