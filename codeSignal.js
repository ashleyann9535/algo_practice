//Given an array of strings, return another array containing all of its longest strings.
const longestStr = arr => {
    let sortArr = arr.sort((a,b) => b.length - a.length)
                    .filter(element => element.length === arr[0].length);

    return sortArr;
}
//console.log(longestStr(["aba", "aa", "ad", "vcd", "aba"])); // ["aba", "vcd", "aba"]

//Given two strings, find the number of common characters between them.
const commonLetters = (s1, s2) => {
    let counter = 0;
    let arr1 = s1.split('');
    let arr2 = s2.split('');

    arr1.map(char1 => {
        if(arr2.includes(char1)){
            counter++;
            arr2.splice(arr2.indexOf(char1), 1);
        };
    });

    return counter;
}

//console.log(commonLetters("aabcc", "adcaa")); // 3

//Ticket numbers usually consist of an even number of digits.
//A ticket number is considered lucky if the sum of the first half of the digits is equal 
//to the sum of the second half. Given a ticket number n, determine if it's lucky or not.
const luckyTicket = n => {
    const numStr = n.toString();

    let middle = Math.floor(numStr.length / 2);

    let part1 = numStr.substring(0, middle);
    let part2 = numStr.substring(middle);

    let partsArr = [part1, part2];

    const digitSum = partsArr.map(str =>
        str.split('').reduce((acc, curr) => acc + parseInt(curr), 0)
    );
    
    if(digitSum[0] === digitSum[1]){
        return true;
    }else {
        return false;
    }
}

console.log(luckyTicket(1230)); //True
console.log(luckyTicket(239017)); //False