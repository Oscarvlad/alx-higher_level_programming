/*
  toggles the class of the HTML tag HEADER to red (#FF0000)
  when the user clicks on the tag DIV#toggle_header
*/
const header = $('HEADER');
const divTog = $('DIV#toggle_header');

if (!header.hasClass('red') && !header.hasClass('green')) {
  header.addClass('red');
  header.removeClass('green');
}

divTog.click(() => {
  if (header.hasClass('red')) {
    header.addClass('green');
    header.removeClass('red');
  } else {
    header.addClass('red');
    header.removeClass('green');
  }
});
