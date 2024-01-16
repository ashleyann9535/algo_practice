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

console.log(commonLetters("aabcc", "adcaa")); // 3