var testValue = 'test';
(function(){
    // この中の処理も順番に実行されます
    var testValue = 'test1';
    // ...
})();
console.log(testValue); // => test

// これは上記の即時関数とほぼ同じ動作です
// letやconstはブロックスコープなのでこれだけでOKです
{
    let testValue = 'test1';
    // ...
}