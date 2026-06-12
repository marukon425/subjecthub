/////// 開始と終了のログの表示


//  startButtonというclassがついているタグ要素のうち、
//  最初のもの(スタートボタン)を取り出す
var displayElm = document.getElementsByClassName('display')[0];
var timer = null;

var staratButtno = document.getElementsByClassName('startButton')[0]; //getElementsByClassNameでもqerySelecterでもいい

// 取り出したstartButtonに対してクリックイベントのリスナを仕掛ける
staratButtno.addEventListener('click', function(){
    // タイマーが何もない場合にのみスタートボタンが機能する
    if(timer === null){
        // この行はクリックしたときに呼ばれる
        var seconds = 0;
        // console.log('start') 削除
        // setInterval：指定した時間ごとに何度も繰り返す(今回の場合は1000ミリ秒ごと)
        timer = setInterval(function(){
            seconds++
            displayElm.innerHTML = seconds;
            console.log(seconds);
        }, 1000);
        var message = '開始';
        var messageElm = document.createElement('div');
        messageElm.innerText = message;
        var logElm = document.querySelector('.log');
        logElm.appendChild(messageElm);
        console.log('start:' + timer);
    }
});

var stopButton = document.getElementsByClassName('stopButton')[0];
stopButton.addEventListener('click', function() {
    // タイマーにカウントしてる間はストップボタンが機能する
    if (timer !== null){
        console.log('stop:' + timer)
        clearInterval(timer);
        timer = null;
    }
});