/////// const/let

// var, let → 変数宣言 ※ varは古いため現在はlet推奨
// const → 定数宣言(後から中身が変えられない)
// ` ${} ` でpythonのfストリングみたいなことができる
function stopWatch(options = {}){
    // 変数宣言してアロー関数を使う方法
    const addMessage = (massage) =>{
        var messageElm = document.createElement('div');
        var now = new Date();
        messageElm.innerText = `${now.getHours()}時${now.getUTCMinutes()}分${now.getSeconds()}秒${massage}`;
        messageElm.classList = ['message'];
        logElm.appendChild(messageElm);
    }

    // options = options || {};
    // var color = options.color || 'lightblue';
    // var backgroundColor = options.backgroundColor || 'black';
    let {color, backgroundColor} = options;
    var displayElm = document.getElementsByClassName('display')[0];
    displayElm.style.color = color;
    displayElm.style.backgroundColor = backgroundColor;
    //  startButtonというclassがついているタグ要素のうち、
    //  最初のもの(スタートボタン)を取り出す
    var logElm = document.querySelector('.log')
    
    let timer = null;

    const staratButtno = document.getElementsByClassName('startButton')[0]
    // 取り出したstartButtonに対してクリックイベントのリスナを仕掛ける
    staratButtno.addEventListener('click', () => {
        // タイマーが何もない場合にのみスタートボタンが機能する
        if(timer === null){
            // この行はクリックしたときに呼ばれる
            let seconds = 0;
            // console.log('start') 削除
            // setInterval：指定した時間ごとに何度も繰り返す(今回の場合は1000ミリ秒ごと)
            timer = setInterval(function(){
                seconds++
                displayElm.innerHTML = seconds;
                console.log(seconds);
            }, 1000);
            // var message = '開始';
            // var messageElm = document.createElement('div');
            // messageElm.innerText = message;
            // logElm.appendChild(messageElm);
            var logElm = document.querySelector('.log');
            console.log('start:' + timer);
            addMessage('開始')
        }
    });
    
    var stopButton = document.getElementsByClassName('stopButton')[0];
    stopButton.addEventListener('click', () => {
        // タイマーにカウントしてる間はストップボタンが機能する
        if (timer !== null){
            console.log('stop:' + timer)
            clearInterval(timer);
            timer = null;
            addMessage('終了')
        }
    });
}

var options = {
    color: 'limegreen',
    backgroundColor: '#333'
};
stopWatch(options);

// stopWatch();