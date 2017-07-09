(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $name = $('#id_name');
        var $email = $('#id_email');
        var $phone = $('#id_phone');
        var $department = $('#id_department');
        var $is_active = $('#id_is_active');

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
                        d.email = $email.val();
                        d.phone = $phone.val();
                        d.department = $department.val();
                        d.is_active = $is_active.val();
                    }
                }
            });

            $name.on('keyup', table.draw);
            $email.on('keyup', table.draw);
            $phone.on('keyup', table.draw);
            $department.on('change', table.draw);
            $is_active.on('change', table.draw);

        };

        function getButtons(urls) {
            var $container = $('<div>', {'class': 'table-buttons'});

            var $detail_button = $('<a>', {
                'class': 'btn btn-sm btn-info icon',
                'href': urls.detail_url,
                'html': $('<i>', {'class': 'fa fa-search'})
            });

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

            $container.append($detail_button);
            $container.append($update_button);
            $container.append($delete_button);

            return $container;
        }

        return content;
    }

    window.UserListView = library();
})(window);