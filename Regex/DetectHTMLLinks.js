function processData(input) {
    var regex=/<a.*?href="(.*?)".*?>(.*?)<\/a>/ig;
    var result=[];
    input.replace(regex,function(_,href,text){ 
        result.push(href.trim()+','+text.replace(/<.*?>/g,'').trim())
    });
    console.log(result.join('\n'));
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
