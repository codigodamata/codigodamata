function CPF_valido(cpf_requerido) {
  var [raw, valid] = cpf_requerido.split("-");

  raw = raw.replace(/\./g, "");

  const arrayOfDigits = Array.from(String(raw), Number);

  var lista1 = [];


  for (let i = 0; i <= 8; i++) {
    lista1[i] = arrayOfDigits[i] * (10 - i);

  }
  var val1;

  val1 = lista1.reduce((a, b) => a + b, 0);
  var resto1 = val1 % 11;
  if (resto1 < 2) var dig1 = 0;
  else if (resto1 >= 2) var dig1 = 11 - resto1;

  arrayOfDigits.push(dig1);
  var lista2 = [];
  for (let i = 0; i <= 9; i++) {
    lista2[i] = arrayOfDigits[i] * (11 - i);
  }
  var val2;

  val2 = lista2.reduce((a, b) => a + b, 0);
  var resto2 = val2 % 11;
  if (resto2 < 2) var dig2 = 0;
  else if (resto2 >= 2) var dig2 = 11 - resto2;
  arrayOfDigits.push(dig2);

  var concate = `${dig1}${dig2}`;
  if (concate == valid) return true; //alert('qualquer coisa ai');
  else if (concate != valid) return false; //alert("errrou");
}
