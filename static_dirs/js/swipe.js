document.addEventListener('touchstart', handleTouchStart, false);        
document.addEventListener('touchmove', handleTouchMove, false);

var xDown = null;                                                        
var yDown = null;
var lastMove = null;

function getTouches(evt) {
  return evt.touches ||             // browser API
         evt.originalEvent.touches; // jQuery
}                                                     

function handleTouchStart(evt) {
    const firstTouch = getTouches(evt)[0];                                      
    xDown = firstTouch.clientX;                                      
    yDown = firstTouch.clientY;                                      
};                                                

function handleTouchMove(evt) {
    if ( ! xDown || ! yDown ) {
        return;
    }

    var xUp = evt.touches[0].clientX;                                    
    var yUp = evt.touches[0].clientY;

    var xDiff = xDown - xUp;
    var yDiff = yDown - yUp;

    lastMove = swipeReturn(xDiff, yDiff);                              
};
function swipeReturn(xDiff, yDiff)
{
    let val = null;
    if ( Math.abs( xDiff ) > Math.abs( yDiff ) ) {
        if ( xDiff > 0 ) {
            val = "left";
        } else {
            val = "right";
        }                       
    } else {
        if ( yDiff > 0 ) {
            val = "up";
        } else { 
            val = "down";
        }                                                                 
    }
    let pos = {"x":xDown, "y":yDown};
    xDown = null;
    yDown = null;     
    return {"pos":pos, "direction":val};
}

function isSwipeingObject(objName){
    var obj = document.querySelector(objName);
    if (obj != null && lastMove != null){
        var bounding = obj.getBoundingClientRect();
        if (
            bounding.top <= lastMove["pos"]["y"] &&
            bounding.left <= lastMove["pos"]["x"] &&
            bounding.right >= lastMove["pos"]["x"] &&
            bounding.bottom >= lastMove["pos"]["y"]
        ) {
            return lastMove["direction"];
        }
    }
}