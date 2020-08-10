var isVisable = false;
function menuBtn(btn){
    if(!isVisable){
        $('menu').css('display', 'flex');
        $(btn).addClass( "hovered" );
        isVisable = true;
    } else {
        $('menu').css('display', 'none');
        $(btn).removeClass( "hovered" );
        isVisable = false;
    }
}

function checkBtnOnResize(mediaMaches) {
    if(!mediaMaches){
        $('menu').css('display', 'flex');
        $('#menubutton').addClass( "hovered" );
        isVisable = true;
    }else{
        $('menu').css('display', 'none');
        $('#menubutton').removeClass( "hovered" );
        isVisable = false;
    }
}