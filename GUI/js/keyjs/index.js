$(function() {
  
 // $('textarea').focus();
  
  var $caps = $('.capslock'),
      $char = $('.char');
  
  $caps.click(function() {
    if($caps.hasClass('on')) {
      $('.char,.capslock').each(function() {
        $(this).text($(this).text().toLowerCase());
      });
    $caps.removeClass('on');
      
    } else {
      $('.char,.capslock').each(function() {
        $(this).text($(this).text().toUpperCase());
      });
      $caps.addClass('on');
    }
  });
  
  $('li').click(function() {
    var t = this;
     $(this).addClass('touch');
     setTimeout(function() {
       $(t).removeClass('touch');
     },100);
  });
  
  var lastFocus,
      selectionStart,
      selectionEnd;

  $('textarea,input').on('focus', function() {
    $('textarea,input').removeClass('focus');
    $(this).addClass('focus');
  });
  
  $('textarea,input').on('blur', function() {
    lastFocus = this;
    selStart = this.selectionStart;
    selEnd = this.selectionEnd;
  });
  
  $('.char').click(function() {
    var char = $(this).text();
    sendChar(char);
  });
  
  $('.return').click(function() {
    sendChar('\n');
  });
  
  $('.space').click(function() {
    sendChar(' ');
  });
  
  $('.backspace').click(function() {
    backspace();
  });
  
  $('.tab').click(function() {
    tab();
  });
  
  function tab() {
    var $inputs = $('textarea,input');
    var currIndex = parseInt($(lastFocus).attr('tabIndex'));
    var highestIndex = -1;
    var selected = false;
    $inputs.each(function() {
      var index = parseInt($(this).attr('tabIndex'));
      if(index > highestIndex) {
        highestIndex = index;
      }
      if(index === currIndex+1) {
        $(this).focus();
        selected = true;
      }
    });
        
    if(!selected && currIndex === highestIndex) {
      $inputs.each(function() {
        var index = parseInt($(this).attr('tabIndex'));
        if(index === 1) {
          $(this).focus();
        }
      });
    }    
  }
  
  function backspace() {
     var orig = $(lastFocus).val();
     var updated = orig.substring(0, selStart-1) + orig.substring(selEnd, orig.length);
     $(lastFocus).val(updated);
     selEnd = --selStart;
     $(lastFocus).focus();
     lastFocus.selectionStart = selStart;
     lastFocus.selectionEnd = selEnd;
  }
  
  function sendChar(char) {
    var orig = $(lastFocus).val();
    var updated =  orig.substring(0, selStart) + char + orig.substring(selEnd, orig.lenght);
    $(lastFocus).val(updated);
    selEnd=++selStart;
    $(lastFocus).focus();
    lastFocus.selectionStart = selStart;
    lastFocus.selectionEnd = selEnd;
  };
  
});

document.getElementById("keyboard").focus();