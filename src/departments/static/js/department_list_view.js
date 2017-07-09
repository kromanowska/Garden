(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $name = $('#id_name');
        var $abbreviation = $('#id_abbreviation');
        var $is_active = $('#id_is_active');
        var $manager = $('#id_manager');
        var $deputy_manager = $('#id_deputy_manager');

        content.setup = function (url) {
            var table = $('#table').DataTable({
                responsive: true,
                order: [[0, 'asc']],
                columnDefs: [{
                    orderable: false,
                    targets: -1,
                    className: 'text-right',
                    render: function (data, type, row) {
                        return getButtons(row[5])[0].outerHTML;
                    }
                }],
                iDisplayLength: 20,
                bLengthChange: false,
                dom: 'lrt<"row"<"col-sm-6"i><"col-sm-6"p>>',
                processing: true,
                serverSide: true,
                sServerMethod: 'POST',
                ajax: {
                    url: url,
                    data: function (d) {
                        d.name = $name.val();
                        d.abbreviation = $abbreviation.val();
                        d.is_active = $is_active.val();
                        d.manager = $manager.val();
                        d.deputy_manager = $deputy_manager.val();
                    }
                }
            });

            $name.on('keyup', table.draw);
            $abbreviation.on('keyup', table.draw);
            $is_active.on('change', table.draw);
            $manager.on('keyup', table.draw);
            $deputy_manager.on('keyup', table.draw);
        };

        function getButtons(urls) {
            var $container = $('<div>', {'class': 'table-buttons'});

            var $update_button = $('<a>', {
                'class': 'btn btn-sm btn-primary icon',
                'href': urls.update_url,
                'html': $('<i>', {'class': 'fa fa-pencil'})
            });

            var $delete_button = $('<a>', {
                'class': 'btn btn-sm btn-danger icon',
                'href': urls.delete_url,
                'html': $('<i>', {'class': 'fa fa-times'})
            });

            $container.append($update_button);
            $container.append($delete_button);

            return $container;
        }

        return content;
    }

    window.DepartmentListView = library();
})(window);