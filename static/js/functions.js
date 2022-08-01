const displayChart = () => {
  if(window.innerHeight < window.innerWidth) {
    document.querySelector(".zoomed-container").classList.toggle("hide-chart");
  }
}