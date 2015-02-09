#urls.py

from django.conf.urls import patterns, url

from inandout import views ###

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),

    url(r'^product_index/$', views.product_index, name='product_index'), # ADD NEW PATTERN!

    url(r'^brand_list/(?P<brand_id>\d+)/$', views.brand_list, name='brand_list'),
    url(r'^product_detail/(?P<product_id>\d+)/$', views.product_detail, name='product_detail'),

    url(r'^blog_index/$', views.blog_index, name='blog_index'), # ADD NEW PATTERN!
    url(r'^blog_detail/(?P<blog_id>\d+)/$', views.blog_detail, name='blog_detail'),

    url(r'^testamonial_index/$', views.testamonial_index, name='testamonial_index'), # ADD NEW PATTERN!
    url(r'^testamonial_detail/(?P<testa_id>\d+)/$', views.testamonial_detail, name='testamonial_detail'),

    # # ex: /polls/5/
    # url(r'^(?P<node_id>\d+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # #url(r'^(?P<node_id>\d+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # #url(r'^(?P<node_id>\d+)/vote/$', views.vote, name='vote'),

    # url(r'^index/$', views.index, name='index'), # ADD NEW PATTERN!

    # url(r'^new_node/$', views.new_node, name='new_node'), # 
    # url(r'^new_asset/$', views.new_asset, name='new_asset'), # new_asset
    # url(r'^(?P<node_id>\d+)/new_sub_node/$', views.new_sub_node, name='new_sub_node'), # new_sub_node


    # url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
) 