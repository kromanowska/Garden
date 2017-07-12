(function (window) {
    'use strict';

    function library() {
        var content = {};

        content.setup = function (csrfToken) {
            setup_csrf_token(csrfToken);
            setup_datepicker();
            setup_chosen();
            $(':checkbox').checkboxpicker();
        };

        function setup_csrf_token(csrfToken) {
            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    if (!csrf_safe_method(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader('X-CSRFToken', csrfToken);
                    }
                }
            });
        }

        function csrf_safe_method(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        function setup_datepicker() {
            $('.datepicker').datepicker({
                format: 'yyyy-mm-dd',
                weekStart: 1,
                todayBtn: "linked",
                daysOfWeekHighlighted: "0,6",
                calendarWeeks: true,
                autoclose: true,
                todayHighlight: true
            });
        }

        function setup_chosen() {
            $("select.chosen-field").chosen({
                no_results_text: 'No results match',
                inherit_select_classes: true,
                placeholder_text_multiple: " ",
                width: "auto"
            });
        }

        return content;
    }

    window.Common = library();
})(window);