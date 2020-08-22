function openGallery(count) {
    ajaxGallery(count, function(res, status){
        var data = JSON.parse(res);
        $("body").append(data.html);
    });
}

function closeGallery() {
    $("body").children("#galleryMain").eq(0).remove();
}

function nextPhoto(id){
    ajaxGallery(id, function(res, status){
        var data = JSON.parse(res);
        $("#galleryGrid").children("#galleryImagePresent").eq(0).remove();
        $("#galleryGrid").append(data.image);
        $(".left").children(".galleryButton").eq(0).remove();
        $(".left").append(data.changeImg["left"]);
        $(".right").children(".galleryButton").eq(0).remove();
        $(".right").append(data.changeImg["right"]);
    });
}

function ajaxGallery(id, func) {
    var image = $(("#picture"+id.toString())).css('background-image');

    $.ajax({
        type: 'POST',
        url: 'php/ajax/gallery.php',
        data: {"image": image, "id": id},
        success: function(res, status){
            try {
                func(res, status)
            } catch (error) {
                null
            }
        }
    });
}