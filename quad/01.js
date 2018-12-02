let infinite = function*(xs) {
  yield* xs;
  console.log("went again");
  yield* infinite(xs);
}

let freqs = document.body.innerText.split('\n')
let frequency = freqs.reduce((l, r) => Number(l) + Number(r))

let find_repeat = function(xs) {
  var accum = 0;
  let seen = new Set([accum]);

  let vs = xs.map(x => parseInt(x, 10)).filter(Number.isInteger);

  for (let f of infinite(vs)) {
    accum += f;

    if (seen.has(accum))
      return accum;
    seen.add(accum);
  }
}

console.log(find_repeat("+3, +3, +4, -2, -4".split(', ')), "== 10");
console.log(find_repeat(freqs))
