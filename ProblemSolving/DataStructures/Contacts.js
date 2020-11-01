'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the contacts function below.
 */
function contacts(queries) {
    let result = [];
    let dict = new Map();
    for(let i=0;i<queries.length;i++){
        let op = queries[i][0];
        let word = queries[i][1];
        let letter = word.charAt(0);
        if(op==='add'){
            for (let j = 1; j <= word.length; j++){
                let sub = word.substring(0, j);
                if (dict.get(sub) == null) dict.set(sub, 1);
                else{
                    let c = dict.get(sub);
                    dict.set(sub, ++c);
                }
            }
        }
        if(op==='find') {
            if (dict.get(word) == null) result.push(0);
            else {
                result.push(dict.get(word));
            }
        }
    }
    return result;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const queriesRows = parseInt(readLine(), 10);

    let queries = Array(queriesRows);

    for (let queriesRowItr = 0; queriesRowItr < queriesRows; queriesRowItr++) {
        queries[queriesRowItr] = readLine().split(' ');
    }

    let result = contacts(queries);

    ws.write(result.join("\n") + "\n");

    ws.end();
}
