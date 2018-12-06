/**
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:
..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
**/

var test = `1, 1
1, 6
8, 3
3, 4
5, 5
8, 9`
var rows = document.body.innerText.split('\n').filter((item) => {
  return item.length;
});

var testRows = test.split('\n').filter((item) => {
  return item.length;
});

function makeDictFromRows(rows) {
  var dict = {}
  for (var i = 0; i < rows.length; i++) {
    var prefix = 'cell';
    if (i < 10) {
      prefix = 'cell0';
    }
    dict[prefix + i] = {
      x: Number(rows[i].split(',')[0].trim()),
      y: Number(rows[i].split(',')[1].trim()),
    }
  }
  return dict;
}

function getMaxX(dict) {
  var localMax = 0;
  for (var key in dict) {
    var x = dict[key].x;
    if (x > localMax) {
      localMax = x;
    }
  }
  return localMax;
}

function getMaxY(dict) {
  var localMax = 0;
  for (var key in dict) {
    var y = dict[key].y;
    if (y > localMax) {
      localMax = y;
    }
  }
  return localMax;
}

function getTaxicabDistanceFromGivenPoint(x1, y1, x2, y2) {
  return Math.abs((x2 - x1)) + Math.abs((y2 - y1));
}

function getTaxicabDistanceForEveryPointFromGivenPoint(key, givenPointX, givenPointY, maxX, maxY, finalArray) {
  for (var x = 0; x <= maxX; x++) {
    for (var y = 0; y <= maxY; y++) {
      var distance = getTaxicabDistanceFromGivenPoint(givenPointX, givenPointY, x, y);
      if (!finalArray[x]) {
        finalArray[x] = [];
      }
      if (!finalArray[x][y]) {
        finalArray[x][y] = {
          id: key,
          distance: distance,
        };
      } else if (distance === finalArray[x][y].distance) {
        finalArray[x][y].id = '.';
        finalArray[x][y].distance = distance;
      }
      if (givenPointX === x && givenPointY === y) {
        finalArray[x][y] = {
          id: key,
          distance: null, 
        }
      } if (distance < finalArray[x][y].distance) {
        finalArray[x][y].id = key;
        finalArray[x][y].distance = distance;
      }  
    }
  }
  return finalArray;
}

function allTheThings(rows) {
  var dict = makeDictFromRows(rows);

  var finalArray = [];
  var maxX = getMaxX(dict);
  var maxY = getMaxY(dict); 

  for (var key in dict) {
    var x = dict[key].x;
    var y = dict[key].y;
    finalArray = getTaxicabDistanceForEveryPointFromGivenPoint(key, x, y, maxX, maxY, finalArray);
  }
  var invalidAreaIds = getInvalidAreaIds(finalArray);
  var obj = {};

  // sum the area for each sub-area
  finalArray.forEach((row) => {
    row.forEach((item) => {
      if (!invalidAreaIds.hasOwnProperty(item.id) && item.id !== '.') {
        if (!obj[item.id]) {
          obj[item.id] = 0;
        }
        obj[item.id]++      
      }
    })
  })

  // find max area for letter
  var max = 0;
  for (var key in obj) {
    if (obj[key] > max) {
      max = obj[key];
    }
  }
  return max;
}

function getInvalidAreaIds(arr) {
  var invalidAreaIds = {};
  for (var x = 0; x <= maxX; x++) {
    for (var y = 0; y <= maxY; y++) {
      var id = arr[x][y].id;
      if (x === 0 || x === maxX || y === 0 || y === maxY) {
        invalidAreaIds[id] = true;
      }
    }
  }
  return invalidAreaIds;

}
allTheThings(rows);
