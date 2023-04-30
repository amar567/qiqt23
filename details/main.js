$(document).ready(function () {

  //hamburger Toggle
  $('.humbarger').click(function (event) {
    $('.menu-list').slideToggle(500);
    event.preventDefault();

    $('.menu-list li a').click(function (event) {
      if ($(window).width() < 768) {
        $('.menu-list').slideUp(500);
        event.preventDefault();
      }
    });
  });

});

var loadData = (data) => {
  
  let detailCard = document.getElementById("detailCard")
  // console.log(data["Name"]);

//   detailCard.innerHTML = `
//   <div class="card">
//       <div class="card__border">
//           <img src="/assets/speakers/prof2.jpg" alt="card image" class="card__img" />
//       </div>

//       <h3 class="card__name">${data["Name"]}</h3>
//       <span class="card__profession">${data["Affiliation"]}</span>

//       <div class="card__social " id="card-social" style="cursor: pointer;" onclick="openDetailsPg()">
//           <div class="card__social-control">
//               Details
//           </div>
//       </div>
//   </div>
// `
  // console.log(data);
}

// const queryString = window.location.search;
// console.log(queryString);
// const urlParams = new URLSearchParams(queryString);

var importdata = $.getJSON("/assets/data.json", function () {
  data = importdata.responseJSON

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const id = urlParams.get('id')

  loadData(data[id])
})