// There is a large pile of socks that must be paired by color. Given an array of integers 
// representing the color of each sock, determine how many pairs of socks with matching colors there are.

// Example


// There is one pair of color  and one of color . There are three odd socks left, 
// one of each color. The number of pairs is .

// Function Description

// Complete the sockMerchant function in the editor below.

// sockMerchant has the following parameter(s):

// int n: the number of socks in the pile
// int ar[n]: the colors of each sock
// Returns

// int: the number of pairs
// Input Format

// The first line contains an integer , the number of socks represented in .
// The second line contains  space-separated integers, , the colors of the socks in the pile.

// Constraints

//  where 
// Sample Input

// STDIN                       Function
// -----                       --------
// 9                           n = 9
// 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
// Sample Output

// 3

function sockMerchant(n, ar) {
    // Write your code here
    let pairs = 0;
    let sock = 1; 

    ar.sort((a,b)=> a-b)

    for(let i = 1; i<n; i++){
        if(ar[i] === ar[i-1]){
            sock++;
            if(sock ==2){
                sock = 0;
                pairs++;
            }
        }else{
            sock = 1;
        }
    }
    return pairs

}

console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

