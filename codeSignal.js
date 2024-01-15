//Given an array of strings, return another array containing all of its longest strings.

const longestStr = arr => {
    let sortArr = arr.sort((a,b) => b.length - a.length)
                    .filter(element => element.length === arr[0].length);

    return sortArr
}

console.log(longestStr(["aba", "aa", "ad", "vcd", "aba"])) // ["aba", "vcd", "aba"]

