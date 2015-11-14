var updateResults = function() {
  // doesn't do anything yet
}

var search = function() {
  var search_string = document.getElementById("search_input").value.trim();
  if (search_string.length === 0) {
    // change this to show message to the user, hopefully
    console.log("Please enter a search string!");
    document.getElementById("error_message").setAttribute("visibility", "visible");
  } else {
    xhttp = new XMLHttpRequest();
    // unsure how to send a request to Django server
    xhttp.open("POST", "127.0.0.1:8000", true);
    xhttp.send(search_string);
  }
};

document.getElementById("search_bar").onkeypress = function(e) {
  var key = e.keyCode || e.which;
  // i.e., if the key is 'Enter'
  if (key == '13') {
    search();
  }
};