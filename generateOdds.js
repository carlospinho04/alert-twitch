
var static_dates = [
	"Sun, Feb 19 2017",
	"Sun, Feb 19 2017",
	"Sun, Feb 19 2017",
	"Mon, Feb 20 2017",
	"Mon, Feb 21 2017"
]

var static_hour = [
	"6:00PM",
	"9:00PM",
	"11:00PM",
	"3:00PM",
	"6:00PM"
]

function generateTable(){
	console.log("Start")
	var games_list = document.getElementById("UPGames")
	var i = 0;
	$.getJSON("teams.json", function(json) {
    	console.log(json['games']['euw']); // this will show the info it in firebug console
		for(i=0;i<5;i++){
		console.log("for")
		var game_tab = document.createElement("tr")
		/***********************/
			var teamlogo1 = document.createElement("td")

			var img1 = document.createElement("img")
			img1.src = json['games']['euw']['teams'][2*i]['logo'] 
			img1.width = 50
			img1.height = 50
			teamlogo1.className+="logo";

			var teamcells = document.createElement("td")
			teamcells.className+= "teamNames";
			teamcells.id = "game" + i
			teamcells.innerHTML = json['games']['euw']['teams'][2*i]['name'] + " vs " + json['games']['euw']['teams'][2*i+1]['name']
			var teamlogo2 = document.createElement("td")
			var img2 = document.createElement("img")
			img2.src = json['games']['euw']['teams'][2*i+1]['logo'] 
			img2.width = 50
			img2.height = 50
			teamlogo2.className+="logo";

			teamlogo1.appendChild(img1)
			teamlogo2.appendChild(img2)

			/*= document.createElement("td")
			var team2 = document.createElement("td")
			var vs = document.createElement("td")
			vs.innerHTML = "vs"
			*/
			var rounds = document.createElement("td")
			rounds.className+= "tableCell";
			rounds.innerHTML = "best of 3"
			var date = document.createElement("td")
			date.className+= "tableCell";
			date.innerHTML = static_dates[i]
			var time = document.createElement("td")
			time.className+= "tableCell";
			time.innerHTML = static_hour[i]
		/***********************/
		game_tab.appendChild(teamlogo1)
		game_tab.appendChild(teamcells)
		game_tab.appendChild(teamlogo2)
		game_tab.appendChild(rounds)
		game_tab.appendChild(date)
		game_tab.appendChild(time)
		games_list.appendChild(game_tab)
	}

	document.body.appendChild(games_list)
});
}

window.addEventListener('load', generateTable);
