SetArray();

var imageArray = [];

function addToCarusel(item, index){
    var articles = "";
    item.forEach(pic => {
        articles += "<article><div class='image autofill hoverZoom1x25 hoverGreyout'>"+
        "<div class='imgCanvas'><div class='imgContain'>"+
        "<div class='overlay'></div>"+
        "<div class='picFill' style='background-image: url(" + pic.url +");'></div>"+
        "</div></div></div></article>";
    });
    $('#carouselMain').append('<div class=\"carousel-item '+ (index==0?'active':'') + ' sliderPart\">'
    +
    articles
    +
    '</div>');
    
    $('#carouselMiniButtons').append(
    "<li data-target=\"#carouselExampleIndicators\" data-slide-to="+index+(index==0?'class=\"active\"':'')+" ></li>"
    );
}

function initCrousel(mediaMaches) {
    
    $("#carouselMain").empty();
    $("#carouselMiniButtons").empty();    
    
    if(mediaMaches){
        for (let index = 0; index < imageArray.length; index++) {
            const element = imageArray[index];
            addToCarusel([element], index);
        }
    }else{
        for (let index = 0; index < Math.floor(imageArray.length/3); index++) {
            const element = [imageArray[index*3],imageArray[index*3+1],imageArray[index*3+2]];
            addToCarusel(element, index);
        }
    } 
}

function repeatStringNumTimes(string, times) {
    var repeatedString = "";
    while (times > 0) {
      repeatedString += string;
      times--;
    }
    return repeatedString;
  }

function SetArray(){
    $.ajax({
        type: 'GET',
        url: 'images',
        data: {'count' : 9},
        success: function (data) {
            imageArray = data.imgs;
            initCrousel(mediaMaches);
        }
    });
  }