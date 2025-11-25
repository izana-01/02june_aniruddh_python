// Simple form validation to avoid JS errors during development
document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('patientForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    // basic client-side checks: required fields
    var required = ['id_first_name', 'id_email', 'id_confirm_email', 'id_phone', 'id_age'];
    var ok = true;
    required.forEach(function (id) {
      var el = document.getElementById(id);
      var err = document.querySelector('.error[data-for="' + id.replace('id_','') + '"]');
      if (!el) return;
      if (!el.value.trim()) {
        ok = false;
        if (err) err.textContent = 'This field is required';
      } else if (err) {
        err.textContent = '';
      }
    });

    // check email match
    var email = document.getElementById('id_email');
    var confirm = document.getElementById('id_confirm_email');
    var emailErr = document.querySelector('.error[data-for="confirm_email"]');
    if (email && confirm && email.value && confirm.value && email.value !== confirm.value) {
      ok = false;
      if (emailErr) emailErr.textContent = 'Emails do not match';
    }

    if (!ok) e.preventDefault();
  });
});
