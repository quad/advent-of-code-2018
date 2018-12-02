// Part 1
var rows = document.body.innerText.split('\n').filter((item) => {
  return item.length
});

function getLetterCounts(str) {
  var letterObj = {};
  for (var i = 0; i < str.length; i++) {
    var letter = str.charAt(i);
    letterObj[letter] = letterObj[letter] + 1 || 1;
  }
  return letterObj;
}

function updateTwoOrThreeObj(obj, twoOrThree) {
  var addedTwo, addedThree = false;
  for (var key in obj) {
    if (obj[key] === 2 && !addedTwo) {
      addedTwo = true;
      twoOrThree.two += 1;
    }
    if (obj[key] === 3 && !addedThree) {
      addedThree = true;
      twoOrThree.three += 1;
    }
  }
  return twoOrThree;
}

function getCheckSum(rows) {
  var twoOrThree = {
    two: 0,
    three: 0,
  };

  rows.forEach((item, index) => {
    var letterCountObjForItem = getLetterCounts(item);
    updateTwoOrThreeObj(letterCountObjForItem, twoOrThree);
  });

  return twoOrThree.two * twoOrThree.three;
}


getCheckSum(rows);

// Part 2
function findDifferentLetters(arr1, arr2) {
  var diff = {};
  for (var i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      diff[arr1[i]] = i;
    }
    if (Object.keys(diff).length > 2) {
      return diff; // short circuit, we don't need to keep looping through
    }
  }
  return diff;
}

// brute force
function getCommonLetters(rows) {
  for (var i = 0; i < rows.length; i++) {
    var arr1 = rows[i].split('');
    for (var j = i; j < rows.length; j++) {
      var arr2 = rows[j].split('');
      var diff = findDifferentLetters(arr1, arr2);
      if (Object.keys(diff).length === 1) {
        var index = diff[Object.keys(diff)[0]]
        return arr1.slice(0, index).concat(arr1.slice(index + 1)).join('');
      }
    }
  }
  return null;
}

getCommonLetters(rows);
