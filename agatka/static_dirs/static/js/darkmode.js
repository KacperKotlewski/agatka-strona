
var alternative_logo = null;
var logo = null;

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

  if ( alternative_logo != null)
  {
    $("#logo").css("background-image", 'url(' + logo + ')');
  }
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

  if ( alternative_logo != null)
  {
    $("#logo").css("background-image", 'url(' + alternative_logo + ')');
  }
}



function ajaxUpdateDisplayMode()
{    
  $.ajax({
    type: 'GET',
    url: '/SetDarkMode',
    data: {'isDark' : isDark}
});
}