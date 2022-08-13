// TOGGLE MENU
let sideMenu = document.querySelector("aside");
let menuBtn = document.querySelector("#menu-btn");
let closeBtn = document.querySelector("#close-btn");

menuBtn.addEventListener("click", () => {
  sideMenu.style.display = "block";
});

closeBtn.addEventListener("click", () => {
  sideMenu.style.display = "none";
});


