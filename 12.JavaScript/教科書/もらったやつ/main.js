// 0-1-04  HTMLで継承して表示してみる　f12のコンソールに表示される
console.log('ファイルの読み込みのテストです');

// 0-2-02　HTMLからinnerTestを探されるので実行
var element = document.getElementById('innerTest');
// 上記で定義した element の表示するHTMLを定義
element.innerHTML = '<strong>JavaScript</strong>で書きました';

// 0-2-04  HTMLの 0-2-03 で行われたボタンに関する処理
// HTMLからtestButtonを探されるので実行
var buttomElm = document.getElementById('testButton');
// 上記で定義した buttomElm の実行されるアラート文
buttomElm.addEventListener('click', function(){
    alert('ボタンが押されました')
    var numberElm = numberElm.value;
    var num = parseInt(val);
    if (num % 2 == 2){
        alert(`偶数です`)
    }else{
        alert(`偶数ではありません`)
    }
})