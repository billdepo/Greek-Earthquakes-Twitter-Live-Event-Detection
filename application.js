
$(document).ready(function(){ //$( document ).ready() will only run once the page Document
                              //Object Model (DOM) is ready for JavaScript code to execute

    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 6){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string); // using jQuery to add content to "log" div of html
        //https://stackoverflow.com/questions/18808626/how-to-write-inside-a-div-box-with-javascript
    });

});