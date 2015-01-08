from django.shortcuts import render , get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import *

from inandout.models import *

from inandout.forms import *

from django.core.exceptions import ValidationError, ObjectDoesNotExist


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


import json

import os
import logging
import httplib2

from apiclient.discovery import build
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from ageless import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from django.utils.html import escape


from itertools import chain




# Create your views here.
def home(request):
    """ """
    frontpage = get_object_or_404(FrontPage, pk=1)
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')

    product_list = Product.objects.filter(is_active=True, frontpage=True).order_by('-priority','-created')
    blog_list = Blog.objects.filter(is_active=True, frontpage=True).order_by('-priority','-created')
    testamonial_list = Testamonial.objects.filter(is_active=True, frontpage=True).order_by('-priority','-created')


    page_object_list = PageObject.objects.filter(is_active=True, page='FP').order_by('-priority','-created')

    object_list = sorted(
        chain(product_list, page_object_list, blog_list, testamonial_list),
        key=lambda instance: instance.priority, reverse=True)

    # if request.user.is_authenticated:
    #     # print request.user.keys() #
    #     print dir(request.user)
    #     print str("pk: ")+str(request.user.pk)
    #     print str("id: ")+str(request.user.id)
    #     print str("user: ")+str(request.user.username )
    #     print dir(request.session)
    #     print request.session.keys()
    #     #request.user.save()


    context = {'frontpage':frontpage,
                'basepage':basepage,
                'object_list':object_list,
                'brand_list':brand_list
                }
    return render_to_response('inandout/home.html', context, RequestContext(request))


def product_index(request):
    """ """


    basepage =  BasePage.objects.order_by('?')[0]
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')
    product_list = Product.objects.filter(is_active=True).order_by('-priority','-created')

    context = {'product_list': product_list,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/product_index.html', context)




def blog_index(request):
    """ """

    basepage =  BasePage.objects.order_by('?')[0]
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')
    blog_list = Blog.objects.filter(is_active=True).order_by('-priority','-created')

    context = {'blog_list': blog_list,'basepage':basepage,'brand_list':brand_list}
    return render(request, 
                'inandout/blog_index.html', 
                context)




def testamonial_index(request):
    """ """


    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')
    testamonial_list = Testamonial.objects.filter(is_active=True).order_by('-priority','-created')

    context = {'testamonial_list': testamonial_list,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/testamonial_index.html', context)



# def index(request):  ###
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
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/product_detail.html', context)



def blog_detail(request, blog_id):
    """ """
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')

    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/blog_detail.html', context)



def testamonial_detail(request, testa_id):
    """ """
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')

    testamonial = get_object_or_404(Testamonial, pk=testa_id)
    context = {'testamonial': testamonial,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/testamonial_detail.html', context)


def brand_list(request, brand_id):
    """ """
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')

    brand = get_object_or_404(Product, pk=brand_id)

    product_list = Product.objects.filter(brand=brand)

    context = {'product_list': product_list,'basepage':basepage,'brand_list':brand_list}
    return render(request, 'inandout/product_index.html', context)






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
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')
    object_list = PageObject.objects.filter(is_active=True, page='CT').order_by('-priority','-created')

    context = {'basepage':basepage,'object_list':object_list,'brand_list':brand_list}
    return render(request, 'inandout/contact_us.html', context)

def about_us(request):
    """ """
    basepage =  get_object_or_404(BasePage, pk=1)
    brand_list = Brand.objects.filter(is_active=True).order_by('-priority','-created')
    object_list = PageObject.objects.filter(is_active=True, page='AU').order_by('-priority','-created')



    context = {'basepage':basepage,'object_list':object_list,'brand_list':brand_list}
    return render(request, 'inandout/about_us.html', context)



























# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    """
    Non-Class-based view for User log out
    """
    # Since we know the user is logged in, we can now just log them out. ###
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')




CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/plus.me',
    redirect_uri='http://ageless.yourcompusolutions.com/oauth2callback')


@login_required
def index(request):
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  credential = storage.get()
  if credential is None or credential.invalid == True:
    FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                   request.user)
    authorize_url = FLOW.step1_get_authorize_url()
    return HttpResponseRedirect(authorize_url)
  else:
    http = httplib2.Http()
    http = credential.authorize(http)
    service = build("plus", "v1", http=http)
    activities = service.activities()
    activitylist = activities.list(collection='public',
                                   userId='me').execute()
    logging.info(activitylist)

    datadump = []

    people_service = service.people()
    people_document = people_service.get(userId='me').execute()
    # # print 'Display name: %s' % people_document.get('displayName')
    # # print 'url: %s' % people_document.get('url')
    # # print people_document.keys()
    #item_list = people_document.keys()
    # datadump.append(people_service.list(collection='visible',userId='me'))
    for item in people_document:
        datadump.append(str(item) + " , " + str(people_document.get(item)) + ".\n")

    # for item in people_service.list(collection='private',userId='me').execute():
    #     datadump.append(str(item) + " , " + str(service.get(item)) + ".\n")

    # people_service = service.people()
    # people_document = people_service.get(userId='me').execute()
    # # print 'Display name: %s' % people_document.get('displayName')
    # # print 'url: %s' % people_document.get('url')
    # # print people_document.keys()
    # item_list = people_document.keys()
    # for item in item_list:
    #     print str(item) + " , " + str(people_document.get(item)) + ".\n"


    return render_to_response('inandout/welcome.html', {
                'activitylist': activitylist, 'datadump':datadump
                })


@login_required
def auth_return(request):
  if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'],
                                 request.user):
    return  HttpResponseBadRequest()
  credential = FLOW.step2_exchange(request.REQUEST)
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  storage.put(credential)
  return HttpResponseRedirect("/")


def gplus_login(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        # print request.POST.items()
        # strip_tags(form.cleaned_data['message'])
        dump_list = []

        post_dict = request.POST.dict()
        for item in post_dict:
            # print item ," | ", post_dict[item]
            if "emails" and "value" in item and ".com" and "@" in post_dict[item]:
                response_data['email'] = escape(post_dict[item])
                # dump_list.append(item) ##
            if "name" and "givenName" in item:
                response_data['firstname'] = escape(post_dict[item])
                # dump_list.append([item,post_dict[item]])   
            if "name" and "familyName" in item:
                response_data['lastname'] = escape(post_dict[item])
                # dump_list.append([item,post_dict[item]])  
            if "[id]"  in item:
                response_data['username'] = escape(post_dict[item])
                response_data['password'] = escape(post_dict[item])
                # dump_list.append([item,post_dict[item]])    

        # print "The whole damn thing: ", request.POST
        # post = Post(text=post_text, author=request.user) ##
        # post.save()

        # response_data['result'] = 'Create post successful!'
        # response_data['postpk'] = post.pk
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username ##
        if (response_data['email']
                and response_data['firstname']
                and response_data['lastname']
                and response_data['username']
                and response_data['password']):

# #        fields = ('username',
#                 'first_name' ,
#                 'last_name', 
#                 'email', 
#                 'confirm_email', 
#                 'password', 
#                 'confirm_password' )

            user_form = UserForm({'username':response_data['username'],
                'first_name':response_data['firstname'] ,
                'last_name':response_data['lastname'], 
                'email':response_data['email'], 
                'confirm_email':response_data['email'], 
                'password':response_data['password'], 
                'confirm_password':response_data['username']})

            if user_form.is_valid():
                user_is_unique = False
                try:
                    username = User.objects.get(username=user_form.cleaned_data['username'])
                except ObjectDoesNotExist:
                    user_is_unique = True

                if user_is_unique: #// Make new User
                    user = user_form.save()
                    
                    # Now we hash the password with the set_password method.
                    # Once hashed, we can update the user object.
                    user.set_password(user.password)
                    user.save()

                else:# // Login as existing User
                    user = authenticate(username=response_data['username'],
                                     password=response_data['password'])

                    # If we have a User object, the details are correct.
                    # If None (Python's way of representing the absence of a value), no user
                    # with matching credentials was found.
                    if user:
                        # Is the account active? It could have been disabled.
                        if user.is_active:
                            # If the account is valid and active, we can log the user in.
                            # We'll send the user back to the homepage.
                            login(request, user)
                            return HttpResponseRedirect('/')
                        else:
                            # An inactive account was used - no logging in!
                            response_text = "<h1><a href='/'>Your account is not enabled. </a></h1>"
                            response_text += "<BR> Please contact the administrator."
                            return HttpResponse(response_text)
                    else:
                        # Bad login details were provided. So we can't log the user in.
                        print "Invalid login details: {0}, {1}".format(username, password)
                        return HttpResponse("<a href='/'>Invalid login details supplied for "+username+".</a>")


        response_data['dump'] = escape(dump_list)
        # print dump_list

        return HttpResponse("Logged In!")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )