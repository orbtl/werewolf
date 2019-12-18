$(document).ready(function(){
    $('#header').load('/home/header');
    var gameID = $('#gameIDInput').val();
    var prevPhase = $('#hunterPrevPhase').val();
    var profileUserID = $('#profileUserID').val();
    $('#nightPhaseDiv').load('/home/game/' + gameID + '/nightPhase');
    $('#dayPhaseDiv').load('/home/game/' + gameID + '/dayPhase');
    $('#hunterPhaseDiv').load('/home/game/' + gameID + '/hunterPhase/' + prevPhase);
    $('#playerInfoDiv').load('/home/game/' + gameID + '/playerInfo');
    $('#postGameInfo').load('/home/game/' + gameID + '/postGameInfo');
    $('#profileGraphDiv').load('/home/users/' + profileUserID + '/graph');
    $('#mainIndexGraphDiv').load('/home/indexGraph');
})