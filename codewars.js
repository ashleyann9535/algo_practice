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

console.log(grow([1, 2, 3, 4]))