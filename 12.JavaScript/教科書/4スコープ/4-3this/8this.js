function MyClass2() {
    this.name = 'これはMyClass2です';
    console.log(this);
}

MyClass2.prototype.test = function() {
    console.log(this === instance2); // => true
    console.log('test!');
};

const instance2 = new MyClass2();
instance2.test();
