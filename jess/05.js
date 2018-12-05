var str = document.body.innerText.trim();
// console.log(str);

/**
dabAcCaCBAcCcaDA',  The first 'cC' is removed.
dabAaCBAcCcaDA',    This creates 'Aa', which is removed.
dabCBAcCcaDA',      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA',        No further actions can be taken.
*/

var test = 'dabAcCaCBAcCcaDA'; 

function isLowercase(char) {
  return char == char.toLowerCase();
}

function isUppercase(char) {
  return char == char.toUpperCase(); 
}

function isSameLetter(char1, char2) {
  return char1.toLowerCase() === char2.toLowerCase(); 
}

function isReactive(char1, char2) {
  return isSameLetter(char1, char2) && (
    (isLowercase(char1) && isUppercase(char2)) ||
    (isUppercase(char1) && isLowercase(char2)) )
}

function negateReactiveThings(str) {
  var i = 0;
  while (i < str.length - 1) {
    var curr = str[i];
    var next = str[i + 1];

    if (isReactive(curr, next)) {
      str = str.slice(0, i).concat(str.slice(i + 2))
    }
    i++;
  }
  return str;
}

function outerLoop(str) {
  var updatedStr = negateReactiveThings(str);
  if (str === updatedStr) { 
    return updatedStr; 
  } else {
    return outerLoop(updatedStr);
  }
}

// outerLoop(test).length;

/**
Part2: What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
*/
var abc = 'abcdefghijklmnopqrstuvwyz'.split('');

function findShortestPolymer(str) {
  var shortestLength;
  abc.forEach((letter, index) => {
    var updatedStr = str
      .replace(new RegExp(letter.toLowerCase(), "g"), "")
      .replace(new RegExp(letter.toUpperCase(), "g"), "")
    updatedStr = outerLoop(updatedStr); 
    if (index === 0) {
      shortestLength = updatedStr.length;
    }
    if (updatedStr.length < shortestLength) {
      shortestLength = updatedStr.length;
    }
  })
  return shortestLength;
}

findShortestPolymer(str);
