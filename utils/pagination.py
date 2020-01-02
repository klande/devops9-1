from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """
    # 重写分页类，默认page_size为5，即按照每页5条分页。
    # 可以通过传参给page_size设置，当page_size小于等于0时显示所有数据，即不分页
    """
    page_size = 5                          # 默认按照每页5条分页
    page_size_query_param = 'page_size'    # 规定每页条数分页规则的参数
    page_query_param = "page"              # 目标页面的参数
    max_page_size = 10                     # 最大页码限制

    # "http://123.56.73.115:8001/api/user/?page=2&page_size=3", 每页3条，显示第2页
    # “http://123.56.73.115:8001/api/user/?page_size = 0”， 列出所有数据，比较危险
    def get_page_size(self, request):
            page_size = int(request.query_params.get('page_size', self.page_size))
            if page_size > 0:
                if page_size > 10:
                    page_size = 10
                return page_size
            else:
                pass
