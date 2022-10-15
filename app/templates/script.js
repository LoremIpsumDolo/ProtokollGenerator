function edit(ele) {
	// I hate JS
	let eleText = document.getElementById(ele);
	let InputField = document.getElementById(ele + "_edit");
	// toggle input visibility
	InputField.classList.toggle("invisible");

	// event listener because no button
	InputField.addEventListener("keypress", function (event) {

		if ( event.key === "Enter" ) {
			event.preventDefault();
			// change Text
			eleText.innerText = InputField.value;
			// toggle input visibility again
			InputField.classList.toggle("invisible");
		}
	});
}



