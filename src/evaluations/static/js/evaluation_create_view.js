(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $computed_summary = $('#computed_summary');
        var $evaluations = $('.evaluation');

        content.setup = function () {
            $evaluations.on('change', function () {
                var sum = 0;
                $evaluations.each(function () {
                    sum += +$(this).val();
                });
                console.log(sum);
                console.log(sum / 11);

                var label = get_label(Math.round(sum / 11));
                console.log(Math.round(sum / 11));
                $computed_summary.text(label);
            });
            $evaluations.trigger('change');
        };

        function get_label(sum) {
            switch (sum) {
                case 1:
                    return 'Consistently below expectations';
                case 2:
                    return 'Below expectations';
                case 3:
                    return 'Meets expectations';
                case 4:
                    return 'Exceeds expectations';
                case 5:
                    return 'Consistently exceeds expectations';
                default:
                    return '';
            }
        }

        return content;
    }

    window.EvaluationCreateView = library();
})(window);