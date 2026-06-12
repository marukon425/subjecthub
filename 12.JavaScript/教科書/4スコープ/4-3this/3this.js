const obj2 = {
    name: 'これはobj2です'
};

obj2.test = obj1.test; // obj1の関数の参照をobj2に代入
obj2.test();