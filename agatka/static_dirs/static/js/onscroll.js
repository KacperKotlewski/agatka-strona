function onscrollDo(whereScroll) {    
    document.body.scrollTo(0, parseInt(($(whereScroll).offset().top)));
}

var toScroll = ["#main","#carouselExampleIndicators"];
var weAreOn = 0;

$('body').on( 'DOMMouseScroll, mousewheel', function ( event ) {
if( event.originalEvent.detail > 0 || event.originalEvent.wheelDelta < 0 ) {
    weAreOn++;
    if(weAreOn >= toScroll.length) weAreOn = toScroll.length-1;
    console.log(toScroll[weAreOn]);
    onscrollDo(toScroll[weAreOn]);
   } else {
    weAreOn--;
    if(weAreOn< 0) weAreOn = 0;
    console.log(toScroll[weAreOn]);
    onscrollDo(toScroll[weAreOn]);
   }
   
return false;
});