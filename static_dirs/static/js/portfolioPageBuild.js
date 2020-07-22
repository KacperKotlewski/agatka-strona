function buildPage(mediaMaches){
    
    $("#imgGallery").empty();  
      
    var imagePerRow = 3;
    if(mediaMaches) imagePerRow = 2;

    for (var i=0; i < Math.ceil((photoArrayPortfolio.length)/imagePerRow); i++) { 
        $articleCount = 0;
    
        var res = "<div class='imgRow'>";
        for (j=0; j < imagePerRow; j++) { 
            if((j+(i*imagePerRow))<photoArrayPortfolio.length){
                res += "<article><div class='image autofill hoverZoom1x25 hoverGreyout'>"+
                "<div class='imgCanvas'><div class='imgContain'>"+
                "<div class='overlay' onclick='openGallery("+(j+(i*imagePerRow)).toString()+")'></div>"+
                "<div class='picFill' id='picture"+(j+(i*imagePerRow)).toString()+"' style='background-image: url(\"pic/" + photoArrayPortfolio[j+(i*imagePerRow)] + "\");'></div>"+
                "</div></div></div></article>";
            }
        }
        res += "</div>";
    
        $('#imgGallery').append(res);
    }
}
buildPage(mediaMaches);