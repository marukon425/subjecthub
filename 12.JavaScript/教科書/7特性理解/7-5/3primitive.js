let testStr1 = 'Hello';
const testStr2 = testStr1;
console.log(testStr1, testStr2);
testStr1 = testStr1.concat('Warld')

//以下の2つは違う値を示している
console.log(testStr1, testStr2);
