document.getElementById('patientForm').addEventListener('submit', function (e) {
  let valid = true;
  const errors = {};

  const firstName = document.getElementById('id_first_name').value.trim();
  const email = document.getElementById('id_email').value.trim();
  const confirmEmail = document.getElementById('id_confirm_email').value.trim();
  const phone = document.getElementById('id_phone').value.trim();
  const age = parseInt(document.getElementById('id_age').value.trim());

  if (!firstName) errors.first_name = 'First name is required';
  if (!email.match(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/)) errors.email = 'Invalid email';
  if (email !== confirmEmail) errors.confirm_email = 'Emails must match';
  if (!phone.match(/^[0-9\\-+\\s()]{6,20}$/)) errors.phone = 'Invalid phone';
  if (isNaN(age) || age <= 0 || age > 120) errors.age = 'Invalid age';

  document.querySelectorAll('.error').forEach(e => e.textContent = '');
  Object.keys(errors).forEach(key => {
    document.querySelector(`.error[data-for=\"${key}\"]`).textContent = errors[key];
    valid = false;
  });

  if (!valid) e.preventDefault();
});
