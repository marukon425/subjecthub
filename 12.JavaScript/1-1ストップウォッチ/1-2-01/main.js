/////// スタートボタンが押されたら一定時間ごとにイベントを呼び出す


//  startButtonというclassがついているタグ要素のうち、
//  最初のもの(スタートボタン)を取り出す
var staratButtno = document.getElementsByClassName('startButton')[0]; //getElementsByClassNameでもqerySelecterでもいい

// 取り出したstartButtonに対してクリックイベントのリスナを仕掛ける
staratButtno.addEventListener('click', function(){
    // この行はクリックしたときに呼ばれる
    var seconds = 0;
    console.log('start')
    // setInterval：指定した時間ごとに何度も繰り返す(今回の場合は1000ミリ秒ごと)
    setInterval(function(){
        seconds++
        console.log(seconds);
    }, 1000)
})