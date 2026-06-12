// 関数の中が有効範囲になるスコープです。関数の中でvarでs年限される変数のみにこれに該当します
function funcScope(){
    var myFuncVar1 = "myFuncVar1"; //これが関数スコープの変数です
    console.log(myFuncVar1);
}

funcScope();
// console.log(myFuncVar1); //エラー：関数の外なのでmyFuncVar1は利用できません