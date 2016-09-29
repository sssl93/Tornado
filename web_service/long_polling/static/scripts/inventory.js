$(document).ready(function () {
    document.session = $('#session').val();

    setTimeout(requestInventory, 100);
    //var execHandle = setInterval(requestInventory, 1000);  //周期任务 每一秒执行

    $('#add-button').click(function (event) {
        jQuery.ajax({
            url: '//localhost:8000/cart',         //请求的url地址
            type: 'POST',
            data: {                                               //请求的参数
                session: document.session,
                action: 'add'
            },
            dataType: 'json',
            beforeSend: function (xhr, settings) {              //请求前的处理
                $(event.target).attr('disabled', 'disabled');   //给当前事件添加disable属性
            },
            success: function (data, status, xhr) {                 //请求成功时的处理；complete: function()请求完成时的处理；error: function() 请求出错时的处理
                $('#add-to-cart').hide();
                $('#remove-from-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });

    $('#remove-button').click(function (event) {
        jQuery.ajax({
            url: '//localhost:8000/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'remove'
            },
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function (data, status, xhr) {
                $('#remove-from-cart').hide();
                $('#add-to-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });
});

function requestInventory() {
    jQuery.getJSON('//localhost:8000/cart/status', {session: document.session},
        function (data, status, xhr) {
            $('#count').html(data['inventoryCount']);
            setTimeout(requestInventory, 0);
        }
    );
}