
function expandUl(id){
    var elem=$("#"+id.toString());
    var ul = elem.find( "ul" )[0];
    var button = elem.find( "i" )[0];
    
    if(ul.style.display == "none"){
        ul.style.display = "block";
        button.classList.remove("icon-right-open");
        button.classList.add("icon-down-open");
    }else{
        ul.style.display = "none";
        button.classList.add("icon-right-open");
        button.classList.remove("icon-down-open");
    }
    
}
function getSelected(){
    selected = [];
    checkboxes = $(".checkbox");
    for(i = 0; i<checkboxes.length; i++){
        if(checkboxes[i].checked == true){
            par = checkboxes[i].parentElement;
            info = {"type" : "", "sqlId" : "", "htmlId" : ""};            
            for (j = 0; j < par.childNodes.length; j++) {                
                if (par.childNodes[j].name == "type") {
                    info['type'] = par.childNodes[j].value;
                }
                if (par.childNodes[j].name == "sqlId") {
                    info['sqlId'] = par.childNodes[j].value;
                }
                if (par.childNodes[j].name == "htmlId") {
                    info['htmlId'] = par.childNodes[j].value;
                }
            }
            selected.push(info);
        }
    }
        
    return selected;
}
function deleteSelected(){
    var tableOfSelected = getSelected();      
    for (i = 0; i < tableOfSelected.length; i++) {
        $("#"+tableOfSelected[i]['htmlId']).addClass("ToDelete");
    }
    window.setTimeout( function(){
        if(confirm("czy na pewno chcesz usunąć ten obiekty"))
        {
            for (i = 0; i < tableOfSelected.length; i++) {
                ajaxDelForce(tableOfSelected[i]['type'], tableOfSelected[i]['sqlId'], tableOfSelected[i]['htmlId']);
            }
        }else{
            for (i = 0; i < tableOfSelected.length; i++) {
                $("#"+tableOfSelected[i]['htmlId']).removeClass("ToDelete");
            }
        }
    }, 50 );
}



function ajaxDelete(type, sqlId, htmlId) {
    $("#"+htmlId).addClass("ToDelete");
    window.setTimeout( function(){
        if(confirm("czy na pewno chcesz usunąć ten obiekt"))
        {
            ajaxDelForce(type, sqlId, htmlId);
        }else{
            $("#"+htmlId).removeClass("ToDelete");
        }
    }, 50 );
}
function ajaxDelForce(type, sqlId, htmlId) {
    $.ajax({
        type: 'POST',
        url: 'php/ajax/removeSql.php',
        data: {"type": type, "id": sqlId},
        success: function(){
            $("#"+htmlId).remove();
        }
    });
}
function ajaxOpenEdit(type, sqlId, parentId, htmlId) {
    var URL = (type=="category"?"administratorPages/category.php":
            (type=="folder"?"administratorPages/folder.php":
            "administratorPages/picture.php"));
    $.ajax({
        type: 'POST',
        url: URL,
        data: {"id": sqlId, "parentId" : parentId, "htmlId" : htmlId},
        success: function(resp){    
            var data = JSON.parse(resp); 
            $("body").append("<div id='popoutWindow'>"+data["html"]+"</div>");           
        }
    });
}

function ajaxOpenNew(type, parentId = null) {    
    var URL = (type=="category"?"administratorPages/category.php":
            (type=="folder"?"administratorPages/folder.php":
            (type=="photos"?"administratorPages/pictures.php":
            "administratorPages/picture.php")));

    var data = {};
    if(parentId != null){
        data = {"parentId":parentId};
    }
    $.ajax({
        type: 'POST',
        url: URL,
        data: data,
        success: function(resp){
            var data = JSON.parse(resp);
            $("body").append("<div id='popoutWindow'>"+data["html"]+"</div>");            
        }
    });
}