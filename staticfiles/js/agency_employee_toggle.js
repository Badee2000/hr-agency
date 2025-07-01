(function ($) {
  $(document).ready(function () {
    function toggleAgencyEmployeeInline() {
      var selectedRole = $("#id_role").val();
      if (selectedRole === "agency_employee") {
        $(".agency-employee-inline").show();
      } else {
        $(".agency-employee-inline").hide();
      }
    }

    // Initial run
    toggleAgencyEmployeeInline();

    // Run on change
    $("#id_role").change(function () {
      toggleAgencyEmployeeInline();
    });
  });
})(django.jQuery);
