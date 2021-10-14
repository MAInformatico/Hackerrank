'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'downToZero' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

const aux = [0,1,2,3];

function downToZero(n) {
    while(n >= aux.length) {
        const lenArray = aux.length;
        const sqrt = Math.floor(Math.sqrt(lenArray));
        let minimum = aux[lenArray - 1];
        for(let i = 2; i <= sqrt; i++) {
            if(lenArray % i === 0) minimum = Math.min(minimum, aux[lenArray / i]);
        }
        aux.push(1 + minimum);
    }
    return aux[n];

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine().trim(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
        const n = parseInt(readLine().trim(), 10);

        const result = downToZero(n);

        ws.write(result + '\n');
    }

    ws.end();
}
