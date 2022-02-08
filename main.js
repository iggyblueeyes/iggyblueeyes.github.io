// pass

function setNav(id, url) {
    document.getElementById(id).onclick = function() {
	window.open(url);
    }
}

setNav("home", "https://iggyblueeyes.github.io")
