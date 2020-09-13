'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the kaprekarNumbers function below.
function kaprekarNumbers(p, q) {
    let listResult = [];
    for(let i = p; i<=q;i++){
        let square = (i*i).toString();
        let r = square.substring(square.length - i.toString().length);
        let l = square.substring(0, square.length - i.toString().length);
        if (parseInt(r) + parseInt(l || 0) === i) {
            listResult.push(i);
        }
    }
    console.log(listResult.length ? listResult.join(' ') : 'INVALID RANGE');
}

function main() {
    const p = parseInt(readLine(), 10);

    const q = parseInt(readLine(), 10);

    kaprekarNumbers(p, q);
}
