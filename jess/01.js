var seenSet = {};
var count = 0;
var nums = document.body.innerText.split('\n').filter((item) => {
  return item.length
}).map(item => Number(item));

function findDupe(numbers, sum) {;
  for (var i = 0; i < numbers.length; i++) {
    var num = numbers[i];
    sum += num;
    seenSet[sum] = !seenSet[sum] ? 1 : seenSet[sum] + 1;
    if (seenSet[sum] > 1) {
      return sum;
    }
  }
  function shouldRepeat(seenSet) {
    for (var key in seenSet) {
      if (seenSet[key] > 1) {
        return false;
      } 
    }
    return true;
  }
  if (shouldRepeat(seenSet)) {
    console.log('recurse', count++)
    return findDupe(numbers, sum);  
  }
}

findDupe(nums, 0);
