var photoArrayPortfolio = []
var lastImgCount = 0;
var how_many_load_at_once = 6
function ajaxGetImages(cat=null){
    var image_before_ajax = photoArrayPortfolio.length
    let count = photoArrayPortfolio.length -(-how_many_load_at_once);

    if (count != lastImgCount){
        lastImgCount = count;

        data = {'count' : count};

        if(cat != null){
            data['category'] = cat;
        }
        
        $.ajax({
            type: 'GET',
            url: '/images',
            data: data,
            success: function (data) {
                photoArrayPortfolio = data.imgs;
                if(count != photoArrayPortfolio.length) empty_loading();
                buildPage(mediaMaches, load_only=(photoArrayPortfolio.length-image_before_ajax));
            }
        });
    } else empty_loading();
    
}

function empty_loading(){
    $("#loadingCircle").remove();
    //$("#loadingCircle").append("<span>Nie ma więcej zdjęć</span>");
}

function buildPage(mediaMaches, load_only=null){
    var photos  = photoArrayPortfolio;
    if (load_only == null)
        $("#imgGallery #images").empty();
    else
        photos = photos.slice(-load_only)
      
    var imagePerRow = 3;
    if(mediaMaches) imagePerRow = 2;

    for (var i=0; i < Math.ceil((photos.length)/imagePerRow); i++) { 
        $articleCount = 0;
    
        var res = "<div class='imgRow'>";
        for (j=0; j < imagePerRow; j++) { 
            if((j+(i*imagePerRow))<photos.length){
                res += "<article><div class='image autofill hoverZoom1x25 hoverGreyout'>"+
                "<div id='image_"+(j+(i*imagePerRow)).toString()+"' class='imgCanvas'><div class='imgContain'>"+
                "<div class='overlay pointer' onclick='fullscreenImage("+(j+(i*imagePerRow)).toString()+")'></div>"+
                "<div class='picFill' id='picture"+(j+(i*imagePerRow)).toString()+"' style='background-image: url(\"" + photos[j+(i*imagePerRow)].url + "\");'></div>"+
                "</div></div></div></article>";
            }
        }
        res += "</div>";
    
        $('#imgGallery #images').append(res);
    }
}


function loading(cat=null) {
    var load = document.querySelector("#loadingCircle i");
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
