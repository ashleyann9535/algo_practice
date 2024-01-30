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

//console.log(luckyTicket(1230)); //True
//console.log(luckyTicket(239017)); //False

//Some people are standing in a row in a park. There are trees between them which cannot be moved. 
//Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
//People can be very tall! -1 means a tree
const seeInThePark = arr => {
    if(arr.includes(-1)){
        let people = arr.filter(h => h !== -1).sort((a,b) => a-b);

        let newArr = arr.map(n => {
            if(n !== -1){
                n = people[0];
                people.shift();
            }
            return n;
        });
        return newArr;
    }

    return arr.sort((a,b) => a-b)
};

//console.log(seeInThePark([-1, 150, 190, 170, -1, -1, 160, 180])); //[-1, 150, 160, 170, -1, -1, 180, 190]
//console.log(seeInThePark([4, 2, 9, 11, 2, 16])); //[2, 2, 4, 9, 11, 16]
//console.log(seeInThePark([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3])); //[1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

//Write a function that reverses characters in (possibly nested) parentheses in the input string.
const reverseParen = inputString => {
    const stack = [];
    let result = '';

    for(let char of inputString){
        if(char === '('){
            stack.push(result);
            result = '';
        }else if(char === ')'){
            result = stack.pop() + result.split('').reverse().join('');
        }else{
            result += char;
        };
    };
    return result;
}

//console.log(reverseParen('(bar)')); // rab
//console.log(reverseParen('foo(bar)baz')) // foorabbaz
//console.log(reverseParen('foo(bar(baz))blim')); // foobazrabblim

//Several people are standing in a row and need to be divided into two teams. 
//The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, 
//the fourth into team 2, and so on.
//You are given an array of positive integers - the weights of the people. 
//Return an array of two integers, where the first element is the total weight of team 1, 
//and the second element is the total weight of team 2 after the division is complete.
const dividedGroups = arr => {
    let groupArr = [0,0];

    arr.map((num, index) => {
        if(index % 2 !== 0){
            groupArr[1] += num;
        }else{
            groupArr[0] += num;
        }
    });

    return groupArr;
}

//console.log(dividedGroups([50, 60, 60, 45, 70])); //[180, 105]

//Given a rectangular matrix of characters, add a border of asterisks(*) to it.
const addBorder = picture => {
    let border = '*'

    const borderedPic = picture.map(elem => {
        return `${border}${elem}${border}`
    })

    borderedPic.unshift(border.repeat(borderedPic[0].length))
    borderedPic.push(border.repeat(borderedPic[0].length))
    
    return borderedPic
}

console.log(addBorder(["abc","ded"])); //["*****","*abc*","*ded*","*****"]