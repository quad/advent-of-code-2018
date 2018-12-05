let polymer = document.body.innerText.trim()

let react = function(l, right) {
  let [head, left] = [l.slice(0, -1), l.slice(-1)]

  if (
    left.toLowerCase() == right.toLowerCase() &&
    left != right
  ) {
    return head
  } else {
    return l + right
  }
}

let full_react = function(p) {
  var last_p = null

  while(p != last_p) {
    last_p = p
    p = [...p].reduce(react)
  }

  return p
}

let test_polymer = "dabAcCaCBAcCcaDA"
let test_polyer_react_single = [...test_polymer].reduce(react)
let test_polyer_react_loop = full_react(test_polymer)

console.log("test_polyer_react_single:", test_polyer_react_single === "dabCBAcaDA")
console.log("test_polyer_react_loop:", test_polyer_react_loop === "dabCBAcaDA")

console.log("polyer units remain:", full_react(polymer).length)

let alphabet = "abcdefghijklmnopqrstuvwxyz"

let react_without_letter = function(l, p) {
  let re = new RegExp("[" + l.toLowerCase() + l.toUpperCase() +"]", "g")
  return full_react(p.replace(re, ""))
}

let test_removed_reactions = [...alphabet].map(l => [l, react_without_letter(l, test_polymer).length])
let removed_reactions = [...alphabet].map(l => [l, react_without_letter(l, polymer).length])
