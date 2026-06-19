function createClosure() {
    const value = 'myClosureValue';

    function myClosure() {
        // valueはmyClosureの外であるが、myclosureと同じcreateClosureの関数スコープにいるので束縛する
        console.log(value);
    }

    return myClosure;
}

const closure = createClosure();
closure();