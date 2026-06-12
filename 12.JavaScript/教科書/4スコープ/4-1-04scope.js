// 最上位(関数等で囲まれてない)でのvarはグローバルスコープに変数を宣言します
var myGlobalVar = 'myGlobalVar';

// これもグローバルスコープに変数を宣言しています
myGlobalVar1 = 'myGlobalVar';

function myFunction1(){
    // 関数の中で初めて使いましたが、varやconstがついて今井のでグローバル変数です
    myGlobalVar2 = 'myGlobalVar2'
}

console.log(myGlobalVar1);

// console.log(myGlobalVar2); // まだ宣言していないのでここで呼ぶとエラー
myFunction1(); // 関数の中でグローバル変数myGlobalVar2が宣言されます
console.log(myGlobalVar2); // ここまでmyGlobalVar2は利用できます