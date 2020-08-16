var photoArrayPortfolio = []
var lastImgCount = 0;
var how_many_load_at_once = 6
function ajaxGetImages(cat=null){
    var image_before_ajax = photoArrayPortfolio.length
    let count = photoArrayPortfolio.length -(-how_many_load_at_once);

    data = {'count' : how_many_load_at_once, "start_at" : lastImgCount};
    lastImgCount = count;

    if(cat != null)
        data['category'] = cat;
    $.ajax({
        type: 'GET',
        url: '/images_from_groups',
        data: data,
        success: function (data) {
            console.log(data);
            photoArrayPortfolio = photoArrayPortfolio.concat(data.grps);
            c = data.grps.length
            if(c == 0) {
                empty_loading();
                c = null;
            }
            buildPage(mediaMaches, load_only=c, galleryOnClick=true);
        }
    });    
}

function empty_loading(){
    $("#container #loadingCircle").remove();
    //$("#loadingCircle").append("<span>Nie ma więcej zdjęć</span>");
}

function buildPage(mediaMaches, load_only=null, galleryOnClick = false){
    var photos  = photoArrayPortfolio;
    if (load_only != null)
    {
        photos = photos.slice(-load_only)
      
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
                        res += "<div class='overlay pointer' onclick='fullscreenGroupGallery("+photos[j+(i*imagePerRow)].id.toString()+")'></div>";
                    else
                        res += "<div class='overlay pointer' onclick='fullscreenImage("+photos[j+(i*imagePerRow)].id.toString()+")'></div>";
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
            ajaxGetImages(cat);
        }
    }
}
function startBuildingPage(cat=null){
    setInterval(function(){loading(cat)}, 500);
}
