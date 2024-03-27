handleSubmit = () => {
  let placa = document.getElementById("placa");
  let cedula = document.getElementById("cedula");
  let form = document.getElementById("form");
  if (validator(cedula, placa)) {
    disableButtons();
    spinner();
    form.submit();
  } else {
    alert("Favor de revisar el formulario");
    form.reportValidity();
  }
};

handleValidateAllRedirect = () => {
  disableButtons();
  spinner();
};

validator = (cedula, placa) => {
  let strRegex = new RegExp(/^[a-z0-9]+$/i);

  isValidPlaca = false;
  isValidCedula = false;

  if (cedula.value == "") {
    cedula.setCustomValidity("El campo no puede estar vacio.");
    isValidCedula = false;
  } else if (cedula.value.length < 9 || cedula.value.length > 11) {
    cedula.setCustomValidity(
      "El campo Cedula/RNC debe contener entre 9 y 11 caracteres."
    );
    isValidCedula = false;
  } else {
    isValidCedula = true;
  }

  if (placa.value == "") {
    placa.setCustomValidity("El campo no puede estar vacio.");
    isValidPlaca = false;
  } else if (placa.value.length != 7 || !strRegex.test(placa.value)) {
    placa.setCustomValidity("El campo Placa debe contener solo 7 caracteres.");
    isValidPlaca = false;
  } else {
    placa.setCustomValidity("");
    isValidPlaca = true;
  }

  if (!isValidCedula || !isValidPlaca) {
    return false;
  }
  return true;
};

spinner = () => {
  let spinner = document.getElementById("spinner");
  spinner.style.display = "block";
};

disableButtons = () => {
  document.getElementById("submitBtn").disabled = true;
  document.getElementById("validateAll").classList.add("disabled");
};
