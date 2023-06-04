// Consider an array/list of sheep where some sheep may be missing from their place.
//  We need a function that counts the number of sheep present in the array (true means present).
function countSheeps(arrayOfSheep) {
    let count = 0;
    for(let i =0; i < arrayOfSheep.length; i++){
        console.log(arrayOfSheep[i])
        if(arrayOfSheep[i] === true){
            count++;
        }
    }
    return count
}


// console.log(countSheeps([true,  true,  true,  false,
//     true,  true,  true,  true ,
//     true,  false, true,  false,
//     true,  false, false, true ,
//     true,  true,  true,  true ,
//     false, false, true,  true]));

// Given a non-empty array of integers, return the result of multiplying the values together in order.
function grow(x){
    let multiple = 1;
    for(let i = 0; i < x.length; i++){
        console.log(x[i])
        multiple *= x[i]
    }
    return multiple
}

// console.log(grow([1, 2, 3, 4]))

// Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) 
// that determines if a given non-negative integer is a power of two.
function isPowerOfTwo(n){
    //.. should return true or false ..
    for(let i = 0; i<= n/2; i++){
      if(2 ** i === n){
        return true
      }
    }
    return false
  }
// console.log(isPowerOfTwo(1024)) //true
// console.log(isPowerOfTwo(333)) //false

// Create a function named rotate() that accepts a string argument and returns an array of strings 
// with each letter from the input string being rotated to the end.
// rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
function rotate(str){
    let arr = []
    let begin = ''
    for(let i =0; i <str.length; i++){
        begin += str[i]
        let remove = str.slice(i+1)
        arr.push(remove + begin)
    }
    return arr
}
// console.log(rotate('Hello'))

//Remove words from the sentence if they contain exactly one exclamation mark. 
//Words are separated by a single space, without leading/trailing spaces.

function remove (string) {
    let newArr = []
    let strArr = string.split(' ')

    for(let i =0; i < strArr.length; i++){
        if(strArr[i].includes('!')){
            if(strArr[i].endsWith('!!') || (strArr[i].endsWith('!') && strArr[i].startsWith('!'))){
                strArr[i] = strArr[i]
                newArr.push(strArr[i])
            }
        }else{
            newArr.push(strArr[i])
        }
    }

    
    return newArr.join(' ');
}

console.log(remove("Hi!")) // = ''
console.log(remove("Hi Hi! Hi!")) // = 'Hi'

console.log(remove("Hi! Hi!! Hi!")) //=== "Hi!!"
console.log(remove("Hi! !Hi! Hi!")) //=== '!Hi!
console.log(remove("Hi! !Hi Hi!")) // === ' '
console.log(remove("!rgrbhy! !hwlud !vvomag srjxs iglj ncgnqb stac !wqd uzpcz"))// === '!rgrbhy! srjxs iglj ncgnqb stac uzpcz'