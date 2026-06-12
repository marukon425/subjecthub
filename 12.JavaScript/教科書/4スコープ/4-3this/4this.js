// call/apply/bindで意図的に変更されたthis

//グローバルオブジェクトのthis


// 何も関数に囲まれてないグローバルスコープのthisはグローバルオブジェクトです
console.log(this === window); // => true

function globalTest() {
    console.log(this === window); // => true
}

// オブジェクトに所有されてないのでthisはwindowです
globalTest()