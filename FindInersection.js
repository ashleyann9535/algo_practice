// Find Intersection
// Have the function FindIntersection(strArr) read the array of strings stored in strArr 
// which will contain 2 elements: the first element will represent a list of comma-separated 
// numbers sorted in ascending order, the second element will represent a second list of 
// comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
// containing the numbers that occur in elements of strArr in sorted order. 
// If there is no intersection, return the string false.

// Examples
// Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
// Output: 1,4,13
// Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
// Output: 1,9,10

function FindIntersection(strArr) { 

    // code goes here
      let str1 = strArr[0].split(', ')
      let str2 = strArr[1].split(', ')
    
      let finalStr = ""
    
      for(let i = 0; i<str1.length; i++){
          if(str2.includes(str1[i])){
              finalStr += str1[i]
              finalStr += ','
          }
      }
  
      if(finalStr === ''){
        return false
      }else{
        return finalStr.slice(0,finalStr.length-1).split(' ').join(''); 
      }
      
      
  }
     
  // keep this function call here 
  console.log(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));