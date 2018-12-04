let records = document.body.innerText.split('\n')
let fake_records = [
  "[1518-11-03 00:29] wakes up",
  "[1518-11-01 00:00] Guard #10 begins shift",
  "[1518-11-01 00:25] wakes up",
  "[1518-11-05 00:55] wakes up",
  "[1518-11-03 00:05] Guard #10 begins shift",
  "[1518-11-01 00:30] falls asleep",
  "[1518-11-05 00:03] Guard #99 begins shift",
  "[1518-11-04 00:02] Guard #99 begins shift",
  "[1518-11-02 00:40] falls asleep",
  "[1518-11-04 00:36] falls asleep",
  "[1518-11-03 00:24] falls asleep",
  "[1518-11-04 00:46] wakes up",
  "[1518-11-01 23:58] Guard #99 begins shift",
  "[1518-11-02 00:50] wakes up",
  "[1518-11-05 00:45] falls asleep",
  "[1518-11-01 00:55] wakes up",
  "[1518-11-01 00:05] falls asleep",
]

let re_shift = /\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\] Guard \#(\d+) begins shift/
let re_sleep = /\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\] falls asleep/
let re_wake = /\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\] wakes up/

let guard_sleep_total = {};
let guard_sleep_minutes = {};
var current_guard;
var current_guard_fell_asleep;

records.sort().forEach(function(ln) {
  if (re_shift.test(ln)) {
    let [_, month, day, hour, minute, guard_id] = ln.match(re_shift)

    current_guard = guard_id

    guard_sleep_total[current_guard] = guard_sleep_total[current_guard] || 0
  }
  else if (re_sleep.test(ln)) {
    let [_, month, day, hour, minute] = ln.match(re_sleep)

    current_guard_fell_asleep = parseInt(minute, 10)
  }
  else if (re_wake.test(ln)) {
    let [_, month, day, hour, _minute] = ln.match(re_wake)
    let minute = parseInt(_minute, 10)
    let minutes_asleep = minute - current_guard_fell_asleep

    guard_sleep_total[current_guard] += minutes_asleep

    for (let m = current_guard_fell_asleep; m < minute; m++) {
      if (!guard_sleep_minutes[m])
        guard_sleep_minutes[m] = []

      guard_sleep_minutes[m].push(current_guard)
    }
  }
  else {
    console.log("err:", ln)
  }
});

let iter_hash = function*(h) {
  for (let k in h) {
    if (h.hasOwnProperty(k)) {
      yield [k, h[k]]
    }
  }
}

let max_value = function(l, r) {
  let [old_k, old_v] = l
  let [new_k, new_v] = r

  if (new_v > old_v)
    return [new_k, new_v]
  else
    return [old_k, old_v]
}

let [sleepy_guard_id, sleepy_guard_total] = [...iter_hash(guard_sleep_total)].reduce(max_value)

let max_seen_for = function(id) {
  return function(l, r) {
    let [old_k, old_seen] = l
    let [new_k, new_seen] = r

    let old_times = old_seen.filter(x => x == id).length
    let new_times = new_seen.filter(x => x == id).length

    if (old_times > new_times)
      return [old_k, old_seen]
    else
      return [new_k, new_seen]
  }
}

let ih = [...iter_hash(guard_sleep_minutes)]
let [answer_1_at, answer_1_seen] = ih.reduce(max_seen_for(sleepy_guard_id))

console.log("A1 (reduce):", sleepy_guard_id * parseInt(answer_1_at, 10))

let keys = function*(h) {
  for (let k in h) {
    if (h.hasOwnProperty(k))
      yield k
  }
}


let values = function*(h) {
  for (let k in h) {
    if (h.hasOwnProperty(k))
      yield h[k]
  }
}

let guard_ids = [...keys(guard_sleep_total)];

var max_seen_id = null;
var max_seen_times = 0;
var max_seen_at = null;

[...values(guard_sleep_minutes)].forEach(function(seen, minute) {
  for (let i of guard_ids) {
    let times = seen.filter(x => x == i).length
    if (times > max_seen_times) {
      max_seen_id = i
      max_seen_times = times
      max_seen_at = minute
    }
  }
})

console.log(max_seen_id, max_seen_times, max_seen_at)
console.log(max_seen_id * max_seen_at)
