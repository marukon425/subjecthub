/////// buttonにイベントリスナを仕掛ける


//  startButtonというclassがついているタグ要素のうち、
//  最初のもの(スタートボタン)を取り出す
var staratButtno = document.getElementsByClassName('startButton')[0]; //getElementsByClassNameでもqerySelecterでもいい

// 取り出したstartButtonに対してクリックイベントのリスナを仕掛ける
staratButtno.addEventListener('click', function(){
    // この行はクリックしたときに呼ばれる
    console.log('start')
})