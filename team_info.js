const URL_TeamInfo = "http://127.0.0.1:5000/get_players_from_team";
const ev_teaminfo = "GET_TEAM_INFO";

(function()
{
	//automatically called as soon as the javascript is loaded
	window.addEventListener("load", main);
}());

function main(){
	var team = localStorage.getItem("team");
	console.log(team);
	var region = localStorage.getItem("region");
	team = 'fnatic'
	region = 'euw'

	var menu = document.getElementById("current");
	console.log("Teams - " + region.toUpperCase());
	menu.childNodes[0].innerText = "Teams - " + region.toUpperCase();
	var displayTeamInfo = function(ev) {
		document.removeEventListener(ev_teaminfo, displayTeamInfo);
		var teams = ev.response;
		console.log(teams);
		/*Object.entries(teams).forEach(
    	([key, value]) => addListToHTML(key, value)
		);*/
	}
	document.addEventListener(ev_teaminfo, displayTeamInfo);
	getTeamInfo(team, region);

}

function addListToHTML(key, value){
	var teams_list = document.getElementById("teams");
	var team_li = document.createElement("li");
	var team_div = document.createElement("div");
	var team_image = document.createElement("img");
	team_image.src = value;
	var team_p = document.createElement("p");
	team_p.innerHTML = key;
	team_div.appendChild(team_image);
	team_div.appendChild(team_p);
	team_li.appendChild(team_div);
	team_li.id = key;
	teams_list.appendChild(team_li);
}

function getTeamInfo(team, region){
	var params = '{"team_name":"' + team + '", "region": "' + region + '"}';
	httpGet(URL_TeamInfo, params, ev_teaminfo);
}

function httpGet(url, data, type){
	var XHR = new XMLHttpRequest();
	XHR.onreadystatechange = function() {
		if (XHR.readyState === 4 && XHR.status === 200) {
			var response = XHR.response;
			var ev = new Event(type);
			ev.response = response;
			document.dispatchEvent(ev);
		}
	}
	XHR.open('POST', url, true);
	XHR.setRequestHeader("Content-type", "application/json; charset=utf-8");
	XHR.setRequestHeader("Access-Control-Allow-Origin", "*");
	XHR.setRequestHeader("Access-Control-Allow-Credentials", "true");
	XHR.responseType = "json";
	XHR.send(data);
}

function myFunction() {
	document.getElementById("myDropdown").classList.toggle("show");
}
