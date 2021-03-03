//function to request a new game
function requestNewGame() {
  $.ajax({
  
    data : { numberOfPins : $('#numberOfPins').val(), numberOfColors : $('#numberOfColors').val()},
    type: 'POST', url: '/newGame'})
    .done(function(data){
      
      //when the return JSON-string contains the Key "error"
      //make the number of pins and colors boxes empty
      if(data.error){
        alert("input invalid");
        $('#numberOfPins').text("");
        $('#numberOfColors').text("");
      }
      
      //fill the textboxes with the appropriate data
      else {  
        $('#numberOfGuesses').val(data.numberOfGuesses) // will always be zero
        $('#solution').val("") // will always be zero
        $('#previousGuessesBody').empty(); //empty the table with previous guesses
      }
    });	
}

//----------------------------------------------------------------------------------------

function makeNewGuess() {
  var guessText = $('#nextGuess').val();
    $.ajax({
      data : { guess : $('#nextGuess').val()},
      type: 'POST', url: '/evaluate'})
      .done(function(data){
        
        if(data.error){
          alert("something went wrong");
        }
        else { 
          //add a new line in the table with the result of the last guess
          $('#previousGuessesBody').append(`<tr><td class="text-center">${guessText}</td><td>${data.correct}</td><td>${data.wrongPlace}</td>`);
          //place number of guesses in corresponding textbox
          $('#numberOfGuesses').val(data.numberOfGuesses);
          //empty the nexthguess textbox
          //$('#nextGuess').val('');
        }
      });	
}

//----------------------------------------------------------------------------------------

function getSolution() {
  $.ajax({
    type: 'POST', url: '/solution'})
    .done(function(data){
      
      if(data.error){
        alert("something went wrong");
      }
      else { 
        //place number of guesses in corresponding textbox
        $('#numberOfGuesses').val(data.numberOfGuesses);
        //place solution in solution textbox
        $('#nextGuess').val('');
        //empty the nexthguess textbox
        $('#solution').val(data.solution);
      }
    });	
}

//----------------------------------------------------------------------------------------
$(document).ready(function(){
  //ask for a new game when the page reloads
  requestNewGame();
  
  //when the new game button is pressed, start requestNewGame function
  $('#newGame').click(function(){
      requestNewGame();
    });
   
  //send guess request when guess button is pressed
  $('#makeGuess').click(function(){
    makeNewGuess();
    });

  //send guess request when enter key is pressed in guess textbox
  $('#nextGuess').bind("enterKey",function(e){
    makeNewGuess();
   });
  
  // binds enter keypress to 
  $('#nextGuess').keyup(function(e){
    if(e.keyCode == 13)
      {
        $(this).trigger("enterKey");
      }
  });
  
  $('#getSolution').click(function(){
    getSolution();
  });

});
