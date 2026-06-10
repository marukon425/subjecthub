console.log('ファイルの読み込みテスト中です')
var element = document.getElementById('innerTest');
element.innerHTML = '<strong>これはJavaSceriptで書いた要素です</strogng>'

var buttomElm = document.getElementById('testButton');
buttomElm.addEventListener('click', function(){
    // alert('ボタンが押されました') 削除
    var numberElm = document.getElementById('number');
    var val = numberElm.ariaValueMax;
    var num = parseInt(val);
    if (num % 2 == 0){
        alert('偶数です');
    }else{
        alert('偶数ではありません')
    }
})