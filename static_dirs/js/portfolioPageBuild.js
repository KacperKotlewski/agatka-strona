const HOW_MANY_LOAD_AT_ONCE = 6

var photoArrayPortfolio = []
var lastImgCount = 0;


function ajaxGetImages(cat=null){
    data = {}
    if(cat != null)
        data['category'] = cat;
    $.ajax({
        type: 'GET',
        url: '/images_from_groups',
        data: data,
        success: function (data) {
            photoArrayPortfolio = photoArrayPortfolio.concat(data.grps);
        }
    });    
}
function delete_loading(){
    c = lastImgCount + HOW_MANY_LOAD_AT_ONCE
    if(c >= photoArrayPortfolio.length) {
        empty_loading();
        c = null;
    }
}

function empty_loading(){
    $("#container #loadingCircle").remove();
    //$("#loadingCircle").append("<span>Nie ma więcej zdjęć</span>");
}

function buildPage(mediaMaches, load_count=null, galleryOnClick = false){
    var photos  = photoArrayPortfolio;
    
    if (load_count != null)
    {
        lastImgCount = load_count + HOW_MANY_LOAD_AT_ONCE
        photos = photos.slice(load_count, lastImgCount)
      
        var imagePerRow = 3;
        if(mediaMaches) imagePerRow = 2;

        for (var i=0; i < Math.ceil((photos.length)/imagePerRow); i++) { 
            $articleCount = 0;
        
            var res = "<div class='imgRow'>";
            for (j=0; j < imagePerRow; j++) { 
                if((j+(i*imagePerRow))<photos.length){
                    res += "<article><div class='image autofill hoverZoom1x25 hoverGreyout'>"+
                    "<div id='image_"+photos[j+(i*imagePerRow)].id.toString()+"' class='imgCanvas'><div class='imgContain'>";

                    if(galleryOnClick)
                        res += "<div class='overlay pointer' onclick='fullscreenGroupGallery(";
                    else
                        res += "<div class='overlay pointer' onclick='fullscreenImage(";
                    res +=photos[j+(i*imagePerRow)].id.toString()+")'><div class='gallery_name'><span>"+photos[j+(i*imagePerRow)].name.toString()+"</span></div></div>";
                    res += "<div class='picFill' id='picture"+photos[j+(i*imagePerRow)].id.toString()+"' style='background-image: url(\"" + photos[j+(i*imagePerRow)].url + "\");'></div>"+
                    "</div></div></div></article>";
                }
            }
            res += "</div>";
        
            $('#imgGallery #images').append(res);
        }
    }
}


function loading(cat=null) {
    var load = document.querySelector("#container #loadingCircle i");
    if (load != null){
        var bounding = load.getBoundingClientRect();
        if (
            bounding.top >= 0 &&
            bounding.left >= 0 &&
            bounding.right <= (window.innerWidth || document.documentElement.clientWidth) &&
            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
        ) {
            delete_loading()
            buildPage(mediaMaches, load_count=lastImgCount, galleryOnClick=true)
        }
    }
}
function startBuildingPage(cat=null){
    if (photoArrayPortfolio.length == 0)
        ajaxGetImages(cat);
    setInterval(function(){loading(cat)}, 500);
}
