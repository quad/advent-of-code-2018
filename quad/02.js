let exactly = function(n) {
  return function(xs) {
    let counts = {}
    let answers = new Set();

    for (let l of xs) {
      counts[l] = counts[l] ? counts[l] + 1 : 1

      if (counts[l] === n)
        answers.add(l)
      else
        answers.delete(l)
    }

    return !!answers.size
  }
}

let ids = document.body.innerText.split('\n')

let test_1_ids = [
  'abcdef',
  'bababc',
  'abbcde',
  'abcccd',
  'aabcdd',
  'abcdee',
  'ababab',
]

let part_1 = function(ids) {
  let l = ids.filter(id => exactly(2)(id))
  let r = ids.filter(id => exactly(3)(id))

  console.log(l)
  console.log(r)

  return l.length * r.length
}

console.log(part_1(test_1_ids), "== 12")
console.log(part_1(ids))

let test_2_ids = [
  "abcde",
  "fghij",
  "klmno",
  "pqrst",
  "fguij",
  "axcye",
  "wvxyz",
]

let differences = function(left, right) {
  if (left.length != right.length)
    console.log("length mismatch!", left, " ", right)

  let indexes = []

  for (let idx = 0; idx < left.length; idx++) {
    if (left[idx] != right[idx])
      indexes.push(idx)
  }

  return indexes
}

console.log(differences("abcde", "axcye"), "== [1, 3]")
console.log(differences("fghij", "fguij"), "== [2]")

let differ_by = function(ids) {
  let results = []

  for (let i = 0; i < ids.length; i++) {
    for (let j = i + 1; j < ids.length; j++) {
      if (differences(ids[i], ids[j]).length == 1)
        results.push(ids[i], ids[j])
    }
  }

  return results
}

console.log(differ_by(test_2_ids), "== ['fghij', 'fguij']")
console.log(differ_by(ids))
