const displayChart = (id) => {
  if(window.innerHeight < window.innerWidth) {
    let myId = id.includes("/") ? id.split("/")[0] : id;
    document.getElementById(myId).classList.toggle("hide-chart");
  }
}