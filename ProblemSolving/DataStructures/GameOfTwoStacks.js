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

function twoStacks(maxSum, a, b) {
    const numsFromA = [];
    let sum = 0;
    
    for(const iterA of a) {
        const next = sum + iterA;
        if(next > maxSum) break;
        else sum = next;
        numsFromA.push(iterA);
    }
    
    let countNumsB = 0;
    let max = numsFromA.length;
    
    for(const iterB of b) {
        sum += iterB, countNumsB++;
        if(sum > maxSum) {
            if(!numsFromA.length) break;
            else sum -= numsFromA.pop();
        } else {
            max = Math.max(countNumsB + numsFromA.length, max);
        }
    }    
    return max;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const g = parseInt(readLine().trim(), 10);

    for (let gItr = 0; gItr < g; gItr++) {
        const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

        const n = parseInt(firstMultipleInput[0], 10);

        const m = parseInt(firstMultipleInput[1], 10);

        const maxSum = parseInt(firstMultipleInput[2], 10);

        const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

        const b = readLine().replace(/\s+$/g, '').split(' ').map(bTemp => parseInt(bTemp, 10));

        const result = twoStacks(maxSum, a, b);

        ws.write(result + '\n');
    }

    ws.end();
}
