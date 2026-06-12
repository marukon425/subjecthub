console.log('ファイルの読み込みテスト中です');

var element = document.getElementById('innerTest');
element.innerHTML = '<strong>これはJavaScriptで書いた要素です</strong>';

var buttomElm = document.getElementById('testButton');
buttomElm.addEventListener('click', function(){
    var numberElm = document.getElementById('number');
    var val = numberElm.value;  // ← ariaValueMax は誤り
    var num = parseInt(val);

    if (num % 2 === 0){
        alert('偶数です');
    } else {
        alert('偶数ではありません');
    }
});

var fruits = ['リンゴ', 'もも', 'みかん'];
var fruitsStr = '';

for (var i = 0; i < fruits.length; i++){  // ← fruits.length が必要
    fruitsStr += '<li class="fruit">' + fruits[i] + '</li>';
}

var arrayElm = document.getElementById('arrayTest');
arrayElm.innerHTML = fruitsStr;
