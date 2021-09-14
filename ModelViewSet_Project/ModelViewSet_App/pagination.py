
from rest_framework.pagination import (
    PageNumberPagination, LimitOffsetPagination,CursorPagination )

class UserPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'number'
    page_query_param = 'mypage'
    last_page_strings = ('endpage',)
    max_page_size = 4



# class UserPagination(LimitOffsetPagination):
#    default_limit = 3  #  displaying [1, 2, 3]  from  [1, 2, 3 , 4 , 5 , 6 , 7]
#    limit_query_param  = 'mylimit'  # limit is  default value
#    offset_query_param = 'myoffset'  # offset is  default value
#    max_limit = 4



# class UserPagination(CursorPagination):
#    page_size = 3  #  3  records displaying on page
#    ordering = ['-salary1']  #  based on salary sorting in desending order.
#    # ordering = ['-created'] # default value



