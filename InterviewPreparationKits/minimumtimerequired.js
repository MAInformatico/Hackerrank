'use strict';

const fs = require('fs');

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

// Complete the minTime function below.
function minTime(machines, goal) {
    let faster = Math.min(...machines)
    let slower = Math.max(...machines)

    let lower = Math.ceil((goal / machines.length) * faster)
    let upper = Math.ceil((goal / machines.length) * slower)

    while(lower < upper){
        let day = Math.floor((upper + lower) / 2)
        let sum = machines.reduce((a, b) => a + Math.floor(day / b), 0)
        if (sum < goal) {
            lower = day+1
        } else if (sum >= goal) {
            upper = day
        }
    }

    return lower
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nGoal = readLine().split(' ');

    const n = parseInt(nGoal[0], 10);

    const goal = parseInt(nGoal[1], 10);

    const machines = readLine().split(' ').map(machinesTemp => parseInt(machinesTemp, 10));

    const ans = minTime(machines, goal);

    ws.write(ans + '\n');

    ws.end();
}
