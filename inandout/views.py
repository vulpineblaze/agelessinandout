from django.shortcuts import render , get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader

from inandout.models import *

from inandout.forms import *

from django.core.exceptions import ValidationError, ObjectDoesNotExist


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    """ """
    context = {}
    return render(request, 'inandout/home.html', context)


def product_index(request):
    """ """


    product_list = Product.objects.all()

    context = {'product_list': product_list}
    return render(request, 'inandout/product_index.html', context)




def blog_index(request):
    """ """


    blog_list = Blog.objects.all()

    context = {'blog_list': blog_list}
    return render(request, 'inandout/blog_index.html', context)




def testamonial_index(request):
    """ """


    testamonial_list = Testamonial.objects.all()

    context = {'testamonial_list': testamonial_list}
    return render(request, 'inandout/testamonial_index.html', context)



# def index(request):
#     """ """
#     node_list = []
#     latest_node_list = Node.objects.order_by('-date_updated')
#     template = loader.get_template('core/index.html')

#     for node in latest_node_list:
#         for child in node.node_set.all():
#             if(child.name == "flags"):
#                 node_list.append(node.pk)

#     queryset = Node.objects.filter(pk__in=node_list) 
#     latest_node_list = queryset   

#     context = {'latest_node_list': latest_node_list}
#     return render(request, 'core/index.html', context)

#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # return HttpResponse(template.render(context))

#     # output = ', '.join([p.name for p in latest_node_list])
#     # return HttpResponse(output)

# # def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]

def product_detail(request, product_id):
    """ """

    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inandout/product_detail.html', {'product': product})



def blog_detail(request, blog_id):
    """ """

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'inandout/blog_detail.html', {'blog': blog})



def testamonial_detail(request, testa_id):
    """ """

    testamonial = get_object_or_404(Testamonial, pk=testa_id)
    return render(request, 'inandout/testamonial_detail.html', {'testamonial': testamonial})


# def detail(request, node_id):
#     """ """

#     node = get_object_or_404(Node, pk=node_id)
#     return render(request, 'core/detail.html', {'node': node})

#     # try:
#  #        node = Node.objects.get(pk=node_id)
#  #    except Node.DoesNotExist:
#  #        raise Http404
#  #    return render(request, 'core/detail.html', {'node': node})

#     # return HttpResponse("You're looking at node %s." % node_id)





def contact_us(request):
    """ """
    context = {}
    return render(request, 'inandout/contact_us.html', context)

def about_us(request):
    """ """
    context = {}
    return render(request, 'inandout/about_us.html', context)
