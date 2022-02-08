// pass

function setNav(id, url) {
    document.getElementById(id).onclick = function() {
	window.location = url;
    }
}

setNav("home", "https://iggyblueeyes.github.io")
