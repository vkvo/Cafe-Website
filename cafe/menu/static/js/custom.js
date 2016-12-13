function slideShow() {
	var images = ['../static/images/b1.jpg', '../static/images/b2.jpg', '../static/images/b3.jpg', '../static/images/b4.jpg']
		setInterval(function() {
			document.body.style.backgroundImage="url("+images[0]+")";

			var firstValue = images.shift();
			images.push(firstValue);

		}, 5000);
}
slideShow();
