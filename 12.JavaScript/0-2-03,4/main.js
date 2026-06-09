console.log('ファイルの読み込みテスト中です')
var element = document.getElementById('innerTest');
element.innerHTML = '<strong>これはJavaSceriptで書いた要素です</strogng>'

var buttomElm = document.getElementById('testButton');
buttomElm.addEventListener('click', function(){
    alert('ボタンが押されました')
})