

var lastImgCount_Gallery = 0;
var how_many_load_at_once_Gallery = 4
var interval_loading_circle = null



function fullscreenImage(id){
    //$("#image_"+id+ " .overlay").css('visibility', 'hidden');
    //$("#picture"+id).css({'position': 'absolute', 'z-index': '50'});
    //$("#image_"+id+ " .picFill").css({'position': 'absolute', 'z-index': '50'});
    //$("#picture"+id).css({'position': 'fixed', 'z-index': '50', "top":"0", "left":"0"});
    $("#imageFullscreen #imgGrids #imageContainer2").css({"background-image": ( $("#picture"+id).css("background-image") )});
    $("#imageFullscreen").css({"display": "block"});
    var item1 = $("#imageFullscreen").find("#imgGrids")[ 0 ];
    var item2 = $(item1).find("#imageContainer2")[0];
    $(item1).css({"visibility": "visible"})
}
function closeImage(){
    var item = $("#imageFullscreen").find("#galleryGrid")[ 0 ];
    if($(item).css("visibility") == "hidden")
        $("#imageFullscreen").css({"display": "none"});
    var item1 = $("#imageFullscreen").find("#imgGrids")[ 0 ];
    $(item1).css({"visibility": "hidden"})
}




function fullscreenGroupGallery(id){
    $.ajax({
        type: 'GET',
        url: 'images_group_gallery',
        data: {'id' : id},
        success: function (data) {
            console.log(data);
            $("#imageFullscreen").css({"display": "block"});
            if (data["fail"] == "No images"){
                fullscreenImage(id)
            } else{
                var item1 = $("#imageFullscreen").find("#galleryGrid")[ 0 ];
                var item2 = $(item1).find("#imageContainer1")[0];
                $(item2).append(data.html)
                $(item1).css({"visibility": "visible"})
                var img = $(item2).find(".image")
            }
        }
    });
}
function closeGallery(){
    var item0 = $("#imageFullscreen").find("#galleryGrid")[ 0 ];
    var item1 = $(item0).find("#imgGallery")[0]
    $(item1).remove()
    $("#imageFullscreen").css({"display": "none"});
    $(item0).css({"visibility": "hidden"});
    empty_loading_images()
}



function closeFullscreen(){
    if($("#imageFullscreen #imgGrids").css("visibility") == "visible"){
        closeImage()
    }else{
        closeGallery()
    }
}



function ajaxGetImagesToGallery(id){
    var image_before_ajax = lastImgCount_Gallery
    let count = lastImgCount_Gallery -(-how_many_load_at_once_Gallery);

    data = {'count' : how_many_load_at_once_Gallery, "start_at" : lastImgCount_Gallery};
    lastImgCount_Gallery = count;

    if(id != null)
        data['id'] = id;
    $.ajax({
        type: 'GET',
        url: 'images_group_gallery',
        data: data,
        success: function (data) {
            html = data.html
            console.log(data);
            if((($(html).length +1)/2) < how_many_load_at_once_Gallery) {
                empty_loading_images();
            }
            $("#imageContainer1 #imgGallery").append(html)
        }
    });    
}








function empty_loading_images(){
    $("#imageContainer1 #loadingCircle").remove();
    //$("#loadingCircle").append("<span>Nie ma więcej zdjęć</span>");
    clearInterval(interval_loading_circle);
    photoArrayGallery = []
    lastImgCount_Gallery = 0
}

function loading_images(id=null) {
    var load = document.querySelector("#imageContainer1 #loadingCircle i");
    if (load != null){
        var bounding = load.getBoundingClientRect();
        if (
            bounding.top >= 0 &&
            bounding.left >= 0 &&
            bounding.right <= (window.innerWidth || document.documentElement.clientWidth) &&
            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
        ) {
            ajaxGetImagesToGallery(id);
        }
    }
}
function startBuildingGallery(id=null){
    interval_loading_circle = setInterval(function(){loading_images(id)}, 500);
}