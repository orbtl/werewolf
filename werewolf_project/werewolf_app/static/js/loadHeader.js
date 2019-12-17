$(document).ready(function(){
    $('#header').load('/home/header');
    var gameID = $('#gameIDInput').val();
    $('#nightPhaseDiv').load('/home/game/' + gameID + '/nightPhase');
    $('#dayPhaseDiv').load('/home/dayPhase');
})