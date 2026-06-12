// 関数呼び出しの際、所有者のオブジェクトを指し示すthis
// クラスを作成した場合

class MyClass {
  constructor() {
    this.name = 'これはMyClassです';
  }

  test() {
    console.log(this);
    console.log(this === instance1);
  }
}

const instance1 = new MyClass();

console.log(instance1); // => MyClass { name: "これはMyClassです" } ③

instance1.test();
// => MyClass { name: "これはMyClassです" }
// => true
