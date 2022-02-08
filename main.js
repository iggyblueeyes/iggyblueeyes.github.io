// pass

function resize() {
    if (window.innerWidth < 500) {
        document.body.style.width = String(0.90*window.innerWidth) + "px"; 
    } else {
	document.body.style.width = String(0.6*window.innerWidth) + "px";
    }
    console.log(document.body.style.width)
}

window.addEventListener("resize", resize)

resize()
