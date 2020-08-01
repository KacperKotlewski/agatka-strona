function fullscreenImage(id){
    //$("#image_"+id+ " .overlay").css('visibility', 'hidden');
    //$("#picture"+id).css({'position': 'absolute', 'z-index': '50'});
    //$("#image_"+id+ " .picFill").css({'position': 'absolute', 'z-index': '50'});
    //$("#picture"+id).css({'position': 'fixed', 'z-index': '50', "top":"0", "left":"0"});
    $("#imageFullscreen #imageContainer").css({"background-image": ( $("#picture"+id).css("background-image") )});
    $("#imageFullscreen").css({"visibility": "visible"});
}
function closeGallery(){
    $("#imageFullscreen").css({"visibility": "hidden"});
}