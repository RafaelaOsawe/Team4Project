console.log("JS Loaded");

const expanded = document.getElementsByClassName("prof_button");
const closeButton = document.getElementsByClassName("close_button");
var body = document.querySelector("body");
var slidePos = 0;

function slideDoorOut() {
    console.log("open called")
    expanded[0].style.cssText = "width: 100vw; height: 100vh; opacity: 1; backdrop-filter: blur(30vw); transition: 2s smooth; animation: animateOut 1.2s;";
    closeButton[0].style.cssText = "display: block;"
};

function slideDoorIn() {
    console.log("close called")
    expanded[0].style.cssText = "width: 10vw; height: 100vh; background-color: transparent; backdrop-filter: blur(10vw); opacity: 1; transition: 2s smooth; animation: animateIn 1.2s;";
    closeButton[0].style.cssText = "display: none;"
}

function carouselAuto() { 
    var slides = document.getElementsByClassName("Slide");
    
      for (let i = 0; i < slides.length; i++) {
        slides[i].style.cssText = "animation: FadeOut 2s ease; display: none; ";
        console.log("for1")
      }
      slidePos++ 
      if (slidePos > slides.length) {slidePos = 1}

    slides[slidePos-1].style.cssText = "animation: FadeIn 2s ease; display: block; animation: zoom 18s;";
    setTimeout(carouselAuto, 18000); //18 sec
      
    console.log(slidePos);
    return slidePos
}

carouselAuto()