
$( window ).resize(function() {
    checkSize();
});


var mediaMaches = null;
var interval= setInterval(checkSize, 500);
interval;

function checkSize() {
    MM = window.matchMedia("(orientation: portrait), (max-width : 750px)").matches;
    if(MM != mediaMaches){
        mediaMaches = window.matchMedia("(orientation: portrait), (max-width : 750px)").matches;       
        
        if (typeof initCrousel === "function") { 
            initCrousel(mediaMaches);
        }
        if (typeof buildPage === "function") { 
            buildPage(mediaMaches);
        }
        checkBtnOnResize(mediaMaches);
    }
}

checkSize();