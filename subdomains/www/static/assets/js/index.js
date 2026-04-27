 // Define the function to be called repeatedly
function updateCypress() {
    let cypress = document.getElementById("cypress-animation")
    let keyframe = Number(cypress.getAttribute("keyframe")) + 1;
    if(keyframe == 10){
        keyframe = 1
    }
    let src = cypress.getAttribute("src");
    src = src.substring(0, src.length - 5) + keyframe + ".png";
    cypress.setAttribute("src", src);
    cypress.setAttribute("keyframe", keyframe);
  }

  // Call the function every 2000ms (2 seconds)
  let intervalId = setInterval(updateCypress, 250);
