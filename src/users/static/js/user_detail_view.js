(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $submited_from = $('#id_submited_from');
        var $submited_to = $('#id_submited_to');

        content.setup = function (url) {
            var table = $('#table').DataTable({
                responsive: true,
                order: [[2, 'desc']],
                columnDefs: [{
                    orderable: false,
                    targets: -1,
                    className: 'text-right',
                    render: function (data, type, row) {
                        return getButtons(row[3])[0].outerHTML;
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
                        d.submited_from = $submited_from.val();
                        d.submited_to = $submited_to.val();
                    }
                }
            });

            $submited_from.on('keyup change', table.draw);
            $submited_to.on('keyup change', table.draw);
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

            if (urls.detail_url) {
                $container.append($detail_button);
            }

            if (urls.update_url) {
                $container.append($update_button);
            }

            if (urls.delete_url) {
                $container.append($delete_button);
            }

            return $container;
        }

        return content;
    }

    window.UserDetailView = library();
})(window);