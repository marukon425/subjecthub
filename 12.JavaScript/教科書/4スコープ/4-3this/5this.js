const objArrow = {
    name: 'これはobjArrowです',
    test: function() {
        console.log('testの中です');
        console.log(this);

        const arrow = () => {
        console.log('arrowの中です');
        console.log(this); // => {name: 'これはobjArrowです', test: f}
        console.log(this === objArrow); // => true
        };

        const normal = function() {
        console.log('normalの中です');
        console.log(this); // => Window
        console.log(this === objArrow); // => false
        };

        arrow();
        normal();
    }
};

console.log(objArrow); // => {name: 'これはobjArrowです', test: f}
objArrow.test();
