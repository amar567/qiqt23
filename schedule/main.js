var loadData = (data) => {
  let detailCard = document.getElementById("detailCard")

  //   detailCard.innerHTML = `
  // `
}



let redirect = (link) => {
  window.location.href = link
}

Date.prototype.getWeek = function () {
  var onejan = new Date(this.getFullYear(), 0, 1);
  var today = new Date(this.getFullYear(), this.getMonth(), this.getDate());
  var dayOfYear = ((today - onejan + 86400000) / 86400000);
  return Math.ceil(dayOfYear / 7)
};

Date.prototype.getDay = function () {
  var onejan = new Date(this.getFullYear(), 0, 1);
  var today = new Date(this.getFullYear(), this.getMonth(), this.getDate());
  var dayOfYear = ((today - onejan + 86400000) / 86400000);
  return dayOfYear
};

var importdata = $.getJSON("/assets/data.json", function () {
  data = importdata.responseJSON

  let weeks = {
    "0": {},
    "1": {},
    "2": {},
    "3": {},
    "4": {},
  }

  for (let i = 0; i < data.length; i++) {
    var day = new Date(data[i]["Date (double click to pick)"]);
    var currentWeekNumber = day.getWeek();
    data[i]["weekNo"] = currentWeekNumber;

    var day = new Date(data[i]["Date (double click to pick)"]);
    var currentDayNumber = day.getDay();
    data[i]["dayNo"] = currentDayNumber;

    var time = data[i]["Time ( IST )"].split(":");
    var currentTime = parseInt(time[0])*3600 + parseInt(time[1])*60 + parseInt(time[2]);
    data[i]["time"] = currentTime
  }

  // data.sort((a, b) => (a.dayNo > b.dayNo) ? 1 : ((b.dayNo > a.dayNo) ? -1 : 0))
  // data.sort((a, b) => (a.time > b.time) ? 1 : ((b.time > a.time) ? -1 : 0));

  for (let i = 0; i < data.length; i++) {

    let currentWeekNumber = data[i]["weekNo"];
    let currentDayNumber = data[i]["dayNo"];

    if (currentWeekNumber === 19 | currentWeekNumber === 20 | currentWeekNumber === 21 | currentWeekNumber === 22) {
      if (weeks[String(currentWeekNumber - 19)][`${currentDayNumber}`]) {
        weeks[String(currentWeekNumber - 19)][`${currentDayNumber}`].push(data[i]);
      }
      else{
        weeks[String(currentWeekNumber - 19)][`${currentDayNumber}`] = []
        weeks[String(currentWeekNumber - 19)][`${currentDayNumber}`].push(data[i]);
      }
    }
  }

  for (const i in weeks) {
    for (const j in weeks[`${i}`]) {
      weeks[`${i}`][`${j}`].sort((a, b) => (a.time > b.time) ? 1 : ((b.time > a.time) ? -1 : 0))
    }
  }

  loadData(weeks)
})