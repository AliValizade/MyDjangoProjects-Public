# from django.shortcuts import render, get_object_or_404
#
# from orders.models import Order
#
#
# def payment_process(request):
#     # Get order_id from session to pay
#     order_id = request.session.get('order_id')
#     # Get the order object
#     order = get_object_or_404(Order, id=order_id)
#
#     total_price = order.get_total_price()
