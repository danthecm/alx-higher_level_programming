$('DIV#toggle_header').bind('click', handleClick);

function handleClick () {
  $('header').toggleClass('red green');
}
