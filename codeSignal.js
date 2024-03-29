//Source = https://app.codesignal.com/
//Arcade Levels

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
    const border = '*';
    
    const borderedPic = picture.map(elem => `${border}${elem}${border}`);
    
    const borderRow = border.repeat(borderedPic[0].length);
    
    borderedPic.unshift(borderRow);
    borderedPic.push(borderRow);
    
    return borderedPic
}
//console.log(addBorder(["abc","ded"])); //["*****","*abc*","*ded*","*****"]

//Two arrays are called similar if one can be obtained from another by swapping at most one pair of 
//elements in one of the arrays.
const similarArr = (a, b) => {
    if(a.length != b.length){
        return false;
    };

    let diffSpots = [];

    for(let i =0; i <= a.length; i++){
        if(a[i] !== b[i]){
            diffSpots.push(i);
        };
    };

    if(diffSpots.length === 0 || (diffSpots.length === 2 && a[diffSpots[0]] === b[diffSpots[1]] && a[diffSpots[1]] === b[diffSpots[0]])){
        return true;
    }else{
        return false;
    };
}

//console.log(similarArr([1, 2, 3], [1, 2, 3])); //true
//console.log(similarArr([1, 2, 3], [2, 1, 3])); //true
//console.log(similarArr([1, 2, 2], [2, 1, 1])); //false

//You are given an array of integers. On each move you are allowed to increase exactly one of its element 
//by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

const increaseCount = inputArray => {
    let count = 0;

    for(let i = 0; i < inputArray.length; i++){
        if(inputArray[i] >= inputArray[i+1]){
            count += (inputArray[i] - inputArray[i+1] + 1);
            inputArray[i+1] = inputArray[i] + 1;
        };
    }

    console.log(inputArray);

    return count;

}

//console.log(increaseCount([-1000, 0, -2, 0])); //5
//console.log(increaseCount([1, 1, 1])); //3

//Given a string, find out if its characters can be rearranged to form a palindrome.

const isPalindrome = inputString => {
//count each character and put into an object to store counts
    let charCount = {};

    for(let char of inputString){
        //create key value pair; if key exists use value and add 1, if not use 0 and add 1
        charCount[char] = (charCount[char] || 0) + 1;
    };

//Check if more than 1 character has an odd count. if does, cant be a palindrome
    let oddCount = 0;

    for(let key in charCount){
        if(charCount[key] % 2 !== 0){
            oddCount++;
        };
        if(count > 1){
            return false;
        };
    };

    return true;
}

//console.log(isPalindrome('aabb')) //true abba
//console.log(isPalindrome('abd')) //false

//Call two arms equally strong if the heaviest weights they each are able to lift are equal.
//Call two people equally strong if their strongest arms are equally strong 
//(the strongest arm can be both the right and the left), and so are their weakest arms.
//Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

const equallyStrong = (yourLeft, yourRight, friendsLeft, friendsRight) => {
    return (yourLeft === friendsLeft && yourRight === friendsRight) || (yourLeft === friendsRight && yourRight === friendsLeft);
};

//console.log(equallyStrong(10, 15, 10, 15)); //true
//console.log(equallyStrong(10, 15, 15, 10)); //true
//console.log(equallyStrong(10, 15, 9, 15)); //false

//Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
const absoluteDifference = inputArray => {
    let absDiff = Math.abs(inputArray[0] - inputArray[1]);

    for(let i = 1; i < inputArray.length -1; i++){
        let difference = Math.abs(inputArray[i] - inputArray[i+1]);
        if(difference > absDiff){
            absDiff = difference;
        };
    };
    return absDiff;
};

//console.log(absoluteDifference([2, 4, 1, 0])); //3

//An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a 
//computer network that uses the Internet Protocol for communication. 
//There are two versions of the Internet protocol, and thus two versions of addresses. 
//One of them is the IPv4 address. Given a string, find out if it satisfies the IPv4 address naming rules.

const ipV4 = (inputString) => {
    //make string into array and then filer elements that dont match ipv4 rules
    const ipv4Arr = inputString.split('.').filter(element => {
        //use early return if element does not meet criteria
        return !(element.length > 1 && element[0] === '0' || Number(element) > 255 || isNaN(Number(element)));
});

    if(ipv4Arr.length !== 4){
        return false;
    }

    return true;
}

// console.log(ipV4("172.16.254.1")); //true
// console.log(ipV4("17.233.01.131")); //false
// console.log(ipV4("172.316.254.1")); // false
// console.log(ipV4(".254.255.0")); // false
// console.log(ipV4("01.233.161.131"));// false
// console.log(ipV4("1.1.1.1.1")); //false
// console.log(ipV4("1.1.1.1a")); //false

//You are given an array of integers representing coordinates of obstacles situated on a straight line.
//Assume that you are jumping from the point with coordinate 0 to the right. 
//You are allowed only to make jumps of the same length represented by some integer.
//Find the minimal length of the jump enough to avoid all the obstacles.
const avoidObstacles = inputArray => {
    const maxCoordinate = Math.max(...inputArray)

    for(let jump = 1; jump <= maxCoordinate + 1; jump++){
        let canClear = true;

        for(let obstacle of inputArray){
            if(obstacle % jump === 0) {
                canClear = false;
                break;
            }
        }
        if(canClear){
            return jump;
        }
    }
    return maxCoordinate + 1;
};

// console.log(avoidObstacles([5, 3, 6, 7, 9])); //4
// console.log(avoidObstacles([5, 8, 9, 13, 14])); //6
// console.log(avoidObstacles([19, 32, 11, 23]))//3

//Box Blur
const boxBlur = image => {
    const calculateSum = (i, j) => {
        let sum = 0;
        for(let dx = -1; dx <= 1; dx++){
            for(let dy = -1; dy <= 1; dy++){
                sum += image[i + dx][j + dy];
            }
        }
        return sum;
    };

    const blurImage = image.slice(1, -1).map((row, i) => 
        row.slice(1, -1).map((_, j) => 
            Math.floor(calculateSum(i + 1, j+1) /9)
        )
    );

    return blurImage;
};

console.log(boxBlur([[1, 1, 1], [1, 7, 1], [1, 1, 1]])); // [[1]]
console.log(boxBlur([[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]])); // [[5,4][4,4]]
