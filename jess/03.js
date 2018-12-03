// Part 1
// If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
var rows = document.body.innerText.split('\n').filter((item) => {
  return item.length
});

function getNumberOfSqInchesInTwoOrMoreclaims(rows) {
  function parseRow(str) {
    var id = Number(str.split(' @ ')[0].slice(1));
    var x = Number(str.split(' @ ')[1].split(',')[0]);
    var y = Number(str.split(',')[1].split(':')[0]);
    var width = Number(str.split('x')[0].split(': ')[1]);
    var height = Number(str.split('x')[1]);
    return {
      id,
      x,
      y,
      width,
      height
    }
  }

  var parsedRows = rows.map(parseRow);

  function findWidthAndHeight(rows) {
    var width, height;

    width = rows.reduce((acc, item, index) => {
      if (item.x + item.width > acc) {
        acc = item.x + item.width; 
      }
      return acc;
    }, 0);

    height = rows.reduce((acc, item, index) => {
      if (item.y + item.height > acc) {
        acc = item.y + item.height; 
        return acc;
      }
      return acc;
    }, 0);

    return {
      width,
      height,
    }
  }

  var dimensions = findWidthAndHeight(parsedRows);

  function makeArray(dimensions) {
    var finalArray = [];
    for (var i = 0; i < dimensions.height; i++) {
      var row = [];
      for (var j = 0; j < dimensions.width; j++) {
        row.push([]);
      }
      finalArray.push(row);
    }
    return finalArray;
  }

  var fabric = makeArray(dimensions)


  function incrementFabricCell(claim) {
    var { id, x, y, width, height } = claim; 
    for (var i = x; i < x + width; i++) {
      for (var j = y; j < y + height; j++) {
        fabric[j][i].push(claim.id)
      }
    }
  }

  var isOverlappingArray = [];

  parsedRows.forEach(function(claim) {
    isOverlappingArray[claim.id] = false;
    incrementFabricCell(claim);
  })
  // Answer for Part 1
  function countTwoOrMoreClaims(fabric) {
    return fabric.flat().filter(item => item.length > 1).length;
  }

  for (var y = 0; y < fabric.length; y++) {
    for (var x = 0; x < fabric[y].length; x++) {
      if (fabric[y][x].length > 1) {
        var arr = fabric[y][x];
        arr.forEach(id => {
          isOverlappingArray[id] = true;  
        })
      }
    }
  }
//   return isOverlappingArray.indexOf(false);
//   return countTwoOrMoreClaims(fabric);
}


getNumberOfSqInchesInTwoOrMoreclaims(rows);
