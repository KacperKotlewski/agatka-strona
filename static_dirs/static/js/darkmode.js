function darkmodeSet(){
  if(!isDark){
    switchFromDark();
  } else {
    switchFromLight();
  }
}

function darkmodeSwitch(){
  if(isDark){
    switchFromDark();
    isDark = false;
  } else {
    switchFromLight();
    isDark = true;
  }
  ajaxUpdateDisplayMode();
}


function switchFromDark() {
  $( ".darkMode" ).each(function( index ) {
    $(this).removeClass( "darkMode" )
    $(this).addClass( "lightMode" )
  });

  $( ".darkModeMenu" ).each(function( index ) {
    $(this).removeClass( "darkModeMenu" )
    $(this).addClass( "lightModeMenu" )
  });
  
  $("#darkMode").removeClass('icon-sun-inv');
  $("#darkMode").addClass('icon-moon-inv');
  $("#darkModeSpan").text('Tryb ciemny');
}

function switchFromLight() {
  $( ".lightMode" ).each(function( index ) {
    $(this).removeClass( "lightMode" )
    $(this).addClass( "darkMode" )            
  });

  $( ".lightModeMenu" ).each(function( index ) {
      $(this).removeClass( "lightModeMenu" )
      $(this).addClass( "darkModeMenu" )            
  });

  $("#darkMode").removeClass('icon-moon-inv');
  $("#darkMode").addClass('icon-sun-inv');
  $("#darkModeSpan").text('Tryb jasny');
}



function ajaxUpdateDisplayMode()
{    
  $.ajax({
    type: 'GET',
    url: 'SetDarkMode',
    dataType: "json",
    data: {'isDark' : isDark},
    success: function (data) {
      console.log(data);
    },
    error: function (jqXHR, exception) {
      var msg = '';
      if (jqXHR.status === 0) {
          msg = 'Not connect.\n Verify Network.';
      } else if (jqXHR.status == 404) {
          msg = 'Requested page not found. [404]';
      } else if (jqXHR.status == 500) {
          msg = 'Internal Server Error [500].';
      } else if (exception === 'parsererror') {
          msg = 'Requested JSON parse failed.';
      } else if (exception === 'timeout') {
          msg = 'Time out error.';
      } else if (exception === 'abort') {
          msg = 'Ajax request aborted.';
      } else {
          msg = 'Uncaught Error.\n' + jqXHR.responseText;
      }
      alert(msg);
    },
});
}