

var lastImgCount_Gallery = 0;
var how_many_load_at_once_Gallery = 8
var interval_loading_circle = null



function fullscreenImage(id){
    AddToUrl(id);
    ajax_show_image(id);
}
function ajax_show_image(id) {
    
    $.ajax({
        type: 'GET',
        url: 'image',
        data: {'id' : id},
        success: function (data) {
            {
                $("#imageFullscreen #imgGrids #imageContainer2").css("background-image", "url(\""+ data.img +"\")");
                $("#imageFullscreen").css({"display": "block"});
                var item1 = $("#imageFullscreen").find("#imgGrids")[ 0 ];
                var item2 = $(item1).find("#imageContainer2")[0];
                var item3 = $(item1).find("#image_id")[0];
                $(item3).val(id)
                $(item1).css({"visibility": "visible"})
                AddImageBar(id)
            }
        }
    });
}
function closeImage(){
    var item = $("#imageFullscreen").find("#galleryGrid")[ 0 ];
    if($(item).css("visibility") == "hidden")
        $("#imageFullscreen").css({"display": "none"});
    var item1 = $("#imageFullscreen").find("#imgGrids")[ 0 ];
    $(item1).css({"visibility": "hidden"})
    $($("#imageFullscreen #imgGrids #imageContainer3")[0]).empty()
}


function AddImageBar(id, count=6, dont_take_base_id=true){
    $($("#imageFullscreen #imgGrids #imageContainer3")[0]).empty()
    start_id = GetNextImageId(id, next=false, move_by=parseInt((count/2)))
    createImageBar = function(img_id) {
        return '<div class=""> <div class="square2 image autofill hoverZoom1x25 hoverGreyout" id="img_gal_obj">'+
                '<div id="image_'+img_id+'" class="imgCanvas">'+
                    '<div class="imgContain">'+
                        '<div class="overlay pointer" onclick="fullscreenImage('+img_id+')"></div>' +
                        '<div class="picFill" id="picture'+img_id+'">'+
            '</div></div></div></div></div>';
    }
    let id_to_add = start_id
    let img_con = ($("#imageFullscreen #imgGrids #imageContainer3")[0]);
    for (let index = 0; index < count; index++) {
        if (id_to_add == id && dont_take_base_id){
            index-=1;
        }
        else{
            image = $.parseHTML(createImageBar(id_to_add));
            $($(image).find(".picFill")[0]).css("background-image", $("#picture"+id_to_add).css("background-image")); //style="background-image: '+( $("#picture"+img_id).css("background-image") )+';"
            $(img_con).append($(image));
        }
        id_to_add = GetNextImageId(id_to_add)
    }
}

function GetNextImageId(id, next=true, move_by=1){
    gallery = $("#galleryGrid #imgGallery")[0];
    i = 0
    totalCount = $(gallery).find(".picFill").length
    var newPic
    $(gallery).children().each(function () {
        if (typeof($(this).find("#picture"+id)[0]) != "undefined"){
            which_image = 0
            if (next){
                if (i>totalCount-1-move_by)
                    which_image = -(1-move_by)
                else
                    which_image = i-(-move_by)
            }
            else{
                if (i<-(0-move_by))
                    which_image = totalCount-move_by
                else
                    which_image = i-move_by
            }
            
            newPic = 0-(-($(gallery).find(".picFill")[which_image].id).slice(7))
            return true;
        }
        i++;
    });
    return newPic
}

function NextImageInGallery(next=true){
    id = 0-(-$("#imgGrids #image_id")[0].value)
    closeImage()
    ajax_show_image( GetNextImageId(id, next) )
}

$(document).ready(function() {
    $("#imageContainer2").on('touchend',function(){
         let dir = isSwipeingObject("#imageContainer2");
         if(dir == "left"){
            NextImageInGallery(next=true)
         }
         else if(dir == "right"){
            NextImageInGallery(next=false)
         }
     });
 });


function fullscreenGroupGallery(id){
    AddToUrl(id);
    ajax_show_group_gallery(id);
}
function ajax_show_group_gallery(id) {
    $.ajax({
        type: 'GET',
        url: 'images_group_gallery',
        data: {'id' : id},
        success: function (data) {
            $("#imageFullscreen").css({"display": "block"});
            if (data["fail"] == "No images"){
                ajax_show_image(id)
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
    empty_loading_images()
    var item1 = $(item0).find("#imageContainer1")[0]
    $(item1).empty()
    $("#imageFullscreen").css({"display": "none"});
    $(item0).css({"visibility": "hidden"});
}



function closeFullscreen(){
    BackOnceUrl()
    if($("#imageFullscreen #imgGrids").css("visibility") == "visible"){
        closeImage()
    }else{
        closeGallery()
    }
}



function ajaxGetImagesToGallery(id){
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
        ajaxGetImagesToGallery(id);
    }
}
function startBuildingGallery(id=null){
    interval_loading_circle = setInterval(function(){loading_images(id)}, 1000);
}









function checkOnLoadGallery(group=null, image=null){
    if(group != null){
        ajax_show_group_gallery(group)
    }
    if(image != null){
        ajax_show_image(image)
    }

}




function AddToUrl(url_addition) {
    url = window.location.href
    new_url = url
    if (url.indexOf("/portfolio") > -1 || url.indexOf("/home") > -1){
        new_url =  url + "/" + url_addition
    }else{
        new_url =  url + "home/" + url_addition
    }
    window.history.replaceState(null, null, new_url);
}
function BackOnceUrl() {
    url = window.location.href
    url_len_to_cut = url.length - ("/"+url.split("/").slice(-1)[0]).length;
    new_url =  url.substring(0, url_len_to_cut );
    window.history.replaceState(null, null, new_url);
}