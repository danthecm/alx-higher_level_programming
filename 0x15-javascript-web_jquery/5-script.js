$('DIV#add_item').bind('click', handleClick);

function handleClick () {
  $('UL.my_list').append($('<li></li>').text('Item'));
}
