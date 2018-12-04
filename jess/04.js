// get guard with the most minutes asleep
// then find the minute at which they slept the most.

// Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
var rows = document.body.innerText.split('\n').filter((item) => {
  return item.length;
}).sort();

var guardMap = {};

function getDate(str) {
  return new Date(str.split('[')[1].split(']')[0]);
}

function getDiff(later, earlier) {
  return (later - earlier) / 1000 / 60
}

var asleepMinuteMap = {}

function updateMinutesAsleepMap(sleep, wake, guardId) {
  var sleepHour = sleep.getHours();
  var sleepMins = sleep.getMinutes();
  var wakeHour = wake.getHours();
  var wakeMins = wake.getMinutes();
  if (sleepHour === 23) {
    sleepMins = 0;
  }
  if (!asleepMinuteMap.hasOwnProperty(guardId)) {
    asleepMinuteMap[guardId] = {};
  }
  for (var i = sleepMins; i < wakeMins; i++) {
    asleepMinuteMap[guardId][i] = (asleepMinuteMap[guardId][i] + 1) || 1; 
  }
}

function buildMap(rows) {
  var i = 0;
  
  while (i < rows.length) {
    var localWakeStart;
    var locaSleepStart;
    var localGuardId;
    if (rows[i].indexOf('Guard #') > -1) {
      var id = rows[i].split('Guard #')[1].split(' ')[0];
      localGuardId = id;
      if (guardMap.hasOwnProperty(id)) {
        guardMap[id].awake = guardMap[id].awake && guardMap[id].awake;
        guardMap[id].asleep = guardMap[id].asleep && guardMap[id].asleep;
      } else {
        guardMap[id] = {
          awake: 0,
          asleep: 0,
        }        
      }
      localWakeStart = getDate(rows[i])
    } 
    if (rows[i].indexOf('falls') > -1) {
      localSleepStart = getDate(rows[i]);
      guardMap[localGuardId].awake += getDiff(localSleepStart, localWakeStart);
    }
    if (rows[i].indexOf('wakes') > -1) {
      localWakeStart = getDate(rows[i]);
      guardMap[localGuardId].asleep += getDiff(localWakeStart, localSleepStart);
      updateMinutesAsleepMap(localSleepStart, localWakeStart, localGuardId)
    }
    i++;
  }

  return guardMap;
}

function minuteWithMostSleeps(sleepObj) {
  var localMax = 0;
  var sleepiestMinute;;
  for (var minute in sleepObj) {
    if (sleepObj[minute] > localMax) {
      localMax = sleepObj[minute];
      sleepiestMinute = minute;
    }
  }
  return sleepiestMinute;
}

function getAsleepTheMost(rows) {
  var mapOfGuardsToAsleepAwake = buildMap(rows);
  var mostSleep = 0;
  var sleepiestGuard;
  for (var guard in mapOfGuardsToAsleepAwake) {
    if (mapOfGuardsToAsleepAwake[guard].asleep > mostSleep) {
      sleepiestGuard = guard;
      mostSleep = mapOfGuardsToAsleepAwake[guard].asleep
    }
  }
  return sleepiestGuard * minuteWithMostSleeps(asleepMinuteMap[sleepiestGuard]);
}

getAsleepTheMost(rows);

function getGuardAndFavoriteSleepyMinute(map) {
  var sleepiestMinute = 0;
  var freqOfSleepsAtSleepiestMinute = 0;
  var guardWithSleepiestMinute;
  for (var guardId in asleepMinuteMap) {
    for (var minute in asleepMinuteMap[guardId]) {
      var freqOfSleeps = asleepMinuteMap[guardId][minute];
      if (freqOfSleeps > freqOfSleepsAtSleepiestMinute) {
        freqOfSleepsAtSleepiestMinute = freqOfSleeps;
        sleepiestMinute = minute;
        guardWithSleepiestMinute = guardId;
      }
    }
  }
  return sleepiestMinute * guardWithSleepiestMinute;
}

getGuardAndFavoriteSleepyMinute(asleepMinuteMap);
