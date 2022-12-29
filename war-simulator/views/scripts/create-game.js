// Constante où on stock le host du serveur contenant l'api (http://localhost:5000)
const host = window.location.protocol + "//" + window.location.host;
// url complète de l'api create-game
const url = host + "/create-game";
// Au chargement de la page, on ajoute un listener au formulaire create-game-form,
// à la soumission la fonction create_game(event) sera appelée
window.onload = function () {
 const createGameForm = document.getElementById("create-game-form");
 if (createGameForm != null) {
 createGameForm.addEventListener("submit", create_game);
 }
};
async function create_game(event) {
 event.preventDefault();
 console.log("start request")
 // Récupérer l'objet qui représente le fomulaire concerné
 const form = event.currentTarget;
 const formData = new FormData(form);
 // Récupérer l'objet contenant les données de notre formulaire
 // notez que les attributs name des elements html du formulaire doivent
 // contenir les mêmes noms attendus par l’api
 const plainFormData = Object.fromEntries(formData.entries());
 const formDataJsonString = JSON.stringify(plainFormData);
 // Appel de l'API create-game qui se fait en asynchrone
 // le await pour stocker le résultat dans response quand il sera reçu
 const response = await postData(url, formDataJsonString)
 // Récupérer l'element html identifié par "create-game-result"
 // afin de mettre le message de retour de l'api
 const resultCreateGame = document.getElementById("create-game-result");
 let h1 = document.createElement('H1');
 resultCreateGame.appendChild(h1)
 if (!response.ok) {
 // le await est ajouté ici parceque response est un objet qu'on recevra plutard en
asynchrone
 const error = await response.json();
 console.log(error)
 h1.innerHTML = "Erreur: " + error.message;
 h1.className = "error";
 } else {
 const gameId = await response.json();
 h1.innerHTML = "Partie créée avec l'id : " + gameId + "<br>";
 // Dans l'element html qui contient le résultat on ajoute un lien
 // pour diriger l'utilisateur vers la page de gestion de création des vaisseaux
 // avec l'id de la partie créée :
 // http://localhost:5000/views/manage_fleet.html?game-id=4&player-name=Tatanor
 let linkToVessels = document.createElement("a");
 const playerName = document.getElementById("player-name").value;
 linkToVessels.href = "manage_fleet.html?game-id=" + gameId + "&player-name=" +
playerName;
 linkToVessels.text = "Créer votre flotte !"
 h1.appendChild(linkToVessels);
 h1.className = "success";
 }
 // on récupère l'objet représentant le formulaire et le masquer
 // on aurait pu utiliser l'objet form récupéré plus haut avec : const form =
event.currentTarget;
 const createGameForm = document.getElementById("create-game-form");
 createGameForm.style.visibility = "hidden";
 // On affiche la balise résultat
 resultCreateGame.style.visibility = "visible";
}
// Fonction pour appeler l'api en POST avec les données data
// les appels api sont toujours en asynchrone en javascript
// afin de ne pas bloquer le navigateur dans l'attente de la réponse
async function postData(url = '', data) {
 const fetchOptions = {
 method: "POST",
 headers: {
 "Content-Type": "application/json",
 "Accept": "application/json"
 },
 body: data,
 };
 return fetch(url, fetchOptions);
}