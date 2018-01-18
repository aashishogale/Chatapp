function checkvalid() {

	if (document.getElementById("id_username").value == "") {

		//alert("Cannot leave firstname this field blank");
		/*	document.getElementById("fname").height="30%"*/
		document.getElementById("usernameerror").innerHTML = "cannot leave this blank";
		return false;
	}
	var regex = /^[a-zA-Z0-9]{2,30}$/;
	var ctrl = document.getElementById("id_username");

	if (regex.test(ctrl.value) != true) {
		document.getElementById("usernameerror").innerHTML = "pls enter correct name";
		return false;
	}

	if (document.getElementById("id_username").value == "") {

		//alert("Cannot leave firstname this field blank");
		/*	document.getElementById("fname").height="30%"*/
		document.getElementById("usernameerror").innerHTML = "cannot leave this blank";
		return false;
	}
	regex = /^[a-zA-Z ]{2,30}$/;
	ctrl = document.getElementById("id_firstname");
	if (ctrl.value == "") {

		//alert("Cannot leave firstname this field blank");
		/*	document.getElementById("fname").height="30%"*/
		document.getElementById("firstnameerror").innerHTML = "cannot leave this blank";
		return false;
	}
	if (regex.test(ctrl.value) != true) {
		document.getElementById("firstnameerror").innerHTML = "pls enter correct name";
		return false;
	}


	ctrl = document.getElementById("id_lastname");
	if (document.getElementById("id_lastname").value == "") {

		//alert("Cannot leave firstname this field blank");
		/*	document.getElementById("fname").height="30%"*/
		document.getElementById("lastnameerror").innerHTML = "cannot leave this blank";
		return false;
	}
	if (regex.test(ctrl.value) != true) {
		document.getElementById("lastnameerror").innerHTML = "pls enter correct name";
		return false;
	}

	regex = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/
	ctrl = document.getElementById("id_email");
	if (document.getElementById("id_email").value == "") {
		document.getElementById("emailerror").innerHTML = "pls enter correct value";
		//alert("Cannot leave email field blank");
		return false;
	}
	if (regex.test(ctrl.value) != true) {
		document.getElementById("emailerror").innerHTML = "pls enter correct email";
		return false;
	}

	if (document.getElementById("id_password").value == "") {
		//alert("Cannot leave password field blank");
		document.getElementById("passworderror").innerHTML = "pls enter password";
		return false;
	}
	if (document.getElementById("id_password").value.length < 4
		|| document.getElementById("id_password").value.length > 20) {
		document.getElementById("passworderror").innerHTML = "pls enter password with correct length";
		//alert("pls enter correct number of character for password");
		return false;
	}
	return true;
}