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
    console.log($(item1).css({"visibility": "hidden"}))
}




function fullscreenGroupGallery(id){
    $.ajax({
        type: 'GET',
        url: 'images_group_gallery',
        data: {'id' : id},
        success: function (data) {
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
    console.log($(item0));
    $(item0).css({"visibility": "hidden"});
}



function closeFullscreen(){
    if($("#imageFullscreen #imgGrids").css("visibility") == "visible"){
        closeImage()
    }else{
        closeGallery()
    }
}