window.onload = function () {
 const urlParams = new URLSearchParams(window.location.search);
 const gameId = urlParams.get("game-id");
 const playerName = urlParams.get("player-name");
 document.getElementById("game-id").value = gameId;
 document.getElementById("player-name").value = playerName;
}


async function getPlayer(gameId, playerName) {
 const resource_url = host + "/get-player?game_id=" + gameId + "&player_name=" +
playerName;
 const response = await getData(resource_url);
 if (!response.ok) {
 return {player_name: playerName, battle_field: {vessels: []}};
 } else {
 return response.json();
 }
}