function closePopup(){
    $("#popoutWindow").remove();
}

function ajaxSqlAdd(type, parentId=null, id = null, htmlId = null){
    data = (type=="category"?sqlCat(id, parentId):(type=="folder"?sqlFold(id, parentId):sqlPic(id, parentId)));
    $.ajax({
        type: 'POST',
        url: 'php/ajax/addAndEditItems.php',
        data: data,
        success: function(resp){
            if(parentId != null){
                var rawData = JSON.parse(resp);
                
                if(id != null && id != ""){
                    upadteExist(htmlId, data);
                }else{
                    appendNew(type, parentId, rawData["id"]);
                }
            }
            closePopup();
        },
        fail: function(){
            alert('request failed');
        }
    });
}
function appendNew(type, parentId, id){
    
    $.ajax({
        type: 'POST',
        url: 'administratorPages/itemListElement.php',
        data: {"id": id, "type" : type, "parentId" : parentId},
        success: function(resp){   
            var data = JSON.parse(resp);
            $("#addNew"+parentId).remove();
            $("#addNew"+parentId).remove();
            $("#"+parentId).append(data["html"]);
        }
    });
}
function upadteExist(htmlId, data){    
    $("#"+htmlId).find(".name")[0].innerText =(data["name"]);
    $("#"+htmlId).find(".desc")[0].innerText =(data["desc"]);
}

function sqlPic(id = null, parentId=null, htmlId = null){
    var data = sqlData(id, parentId, htmlId);
    data["type"] = "picture";
    return data;
}
function sqlFold(id = null, parentId=null, htmlId = null){
    var data = sqlData(id, parentId, htmlId);
    data["type"] = "folder";
    return data;
}
function sqlCat(id = null, parentId=null, htmlId = null){
    var data = sqlData(id, parentId, htmlId);
    data["type"] = "category";
    return data;
}

function sqlData(id = null, parentId=null, htmlId = null) {
    var data = {};
    data["name"] = $("#popName").val();
    data["link"] = $("#popLink").val();
    data["desc"] = $("#popDesc").val();
    data["url"] = "";
    data["date"] = $("#popDate").val();
    
    if(id != null && id != "")
        data["id"] = id;
    if(parentId != null && parentId != ""){
        
        data["parentId"] = parentId;
        var pos = 0;
        var set = false;
        var folder_id = "";
        var group_id = "";
        for (let index = 0; index < parentId.length; index++) {
            const element = parentId.charAt(index);
            if (element == "-") {
                pos++;
                set = true;
            }else if(element == "_"){
                set = false;
            }else if(set == true){
                if(pos == 1) {
                    group_id += element;
                }
                else if(pos == 2) {
                    folder_id += element;
                }
            }
        }
        if(folder_id != ""){
            data["folder_id"] = folder_id;
        }
        if(group_id != ""){
            data["group_id"] = group_id;  
        }  
    }else{
        data["parentId"] = "itemList";
    }
    if(htmlId != null)
        data["htmlId"] = htmlId;
    return data;
}

function onGetSingleFile(){
    var fullPath = $("#popFile").val();
    if (fullPath) {
        var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        var filename = fullPath.substring(startIndex);
        if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
            filename = filename.substring(1);
        }
        var endIndex = (filename.indexOf('.png') >= 0 ? filename.lastIndexOf('.png') : (filename.indexOf('.jpeg') >= 0 ?filename.lastIndexOf('.jpeg'):null));
        
        $("#popFileLabel").html(filename);

        if (endIndex != 0) {
            filename = filename.substring(0, endIndex);
        }
        if($("#popName").val() == ""){
            $("#popName").val(filename);
            OnNameEdit('photo');
        }
    }
}

function onGetMultipleFile(){
    var files = $("#popFiles")[0]["files"];
    console.log(files);
    console.log($("#popFiles"));
    
    $("#pictureList").empty();
    for (let index = 0; index < files.length; index++) {
        const file = files[index];
        console.log(file);
        var fullPath = file["name"];
        if (fullPath) {
            var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
            var filename = fullPath.substring(startIndex);
            if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
                filename = filename.substring(1);
            }
            var endIndex = (filename.indexOf('.png') >= 0 ? filename.lastIndexOf('.png') : (filename.indexOf('.jpeg') >= 0 ?filename.lastIndexOf('.jpeg'):null));
            
            var shortFileName;
            if (endIndex != 0) {
                shortFileName = filename.substring(0, endIndex);
            }
            var hiddenName="<input type='hidden' id='fileName' value='"+shortFileName+"'/>";
            var hiddenLink="<input type='hidden' id='fileLink' value='"+FriendlyLinkValid('photo', shortFileName)+"'/>";
            var listElement="<li id='fileToAdd"+index+"' class='btn'>"+filename+hiddenName+hiddenLink+"</li>";
            $("#pictureList").append(listElement);
        }
    }
}

function OnNameEdit(type) {
    if($("#popLink").val() == ""){
        $("#popLink").val($("#popName").val());
        FriendlyLinkValid(type);
    }
}

function FriendlyLinkValid(type, value = null){
    var link = value;
    if(value == null){
        link = $("#popLink").val();
    }
    var unsafeChars = ["<", ">", "[", "]", "{", "}", "|", "\\", "^", "%", "$", "&", "#", "=", ";", ":", ",", "+", "/", "?", "@"];
    var safeLink= "";
    for (let index = 0; index < link.length; index++) {
        const char = link.charAt(index);
        let isSafe=true;
        for (let i = 0; i < unsafeChars.length; i++) {
            const unsafeChar = unsafeChars[i];
            if(unsafeChar == char){
                isSafe=false;
                break;
            }
        }
        if(char == " "){
            safeLink+="_";
        }
        else if(isSafe==true){
            safeLink+=char;
        }
    }
    if(CheckFriendlyLinkInSql(type, safeLink)){
        var i = 0;
        var temp = safeLink+"-"+(i.toString());
        while (CheckFriendlyLinkInSql(type, temp)) {
            i++;
            temp = safeLink+"-"+(i.toString());
        }
        safeLink = temp;
    }
    if(value == null){
        $("#popLink").val(safeLink);
    }else{
        return safeLink;  
    }
}

function CheckFriendlyLinkInSql(type, link) {
    var resp = $.ajax({
        type: 'POST',
        url: 'php/ajax/checkFriendlyLink.php',
        data: {"type": type, "link": link},
        async: false,
        success: function(resp){
            //console.log(resp);
            var rawData = JSON.parse(resp);
            //console.log(rawData);
        }
    });
    return JSON.parse(resp.responseText)["exist"];
}

function CheckWindowValidation() {
    var disabled = false;
    var req = $(".required");
    for (let index = 0; index < req.length; index++) {
        const element = req[index];        
        if(element.value == null || element.value == ""){
            disabled = true;
            break;
        }
    }
    $("#windowAddButton").prop( "disabled", disabled );
}

var windowInterval = setInterval(CheckWindowValidation, 100);
windowInterval;