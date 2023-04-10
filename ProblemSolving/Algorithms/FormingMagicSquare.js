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
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

function formingMagicSquare(s) {
    const magicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    ];
    
    let arrayCosts = [];
    magicSquares.forEach( array => {
        let cost = 0;
        for(let i = 0; i < 3; i++){
            for(let j = 0; j < 3; j++){
                cost += Math.abs(s[i][j]- array[i][j]);
            }
        }
        arrayCosts.push(cost);
    });
    return arrayCosts.sort((a,b) => a-b)[0];
       
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let s = Array(3);

    for (let i = 0; i < 3; i++) {
        s[i] = readLine().replace(/\s+$/g, '').split(' ').map(sTemp => parseInt(sTemp, 10));
    }

    const result = formingMagicSquare(s);

    ws.write(result + '\n');

    ws.end();
}
