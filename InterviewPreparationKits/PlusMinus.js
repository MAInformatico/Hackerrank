'use strict';

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
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    let positives = 0;
    let negatives = 0;
    let zero = 0;
    for(let i = 0; i<arr.length; i++){
        if (arr[i] == 0)
            zero++;
        if(arr[i] > 0)
            positives++;
        if(arr[i] < 0)
            negatives++;            
    }
    let num = arr.length;
    console.log((positives/num).toFixed(6));
    console.log((negatives/num).toFixed(6));
    console.log((zero/num).toFixed(6));

}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
