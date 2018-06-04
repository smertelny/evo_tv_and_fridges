from django.views import generic
from django.db.models import F
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from .models import Product

@method_decorator(ensure_csrf_cookie, name="dispatch")
class IndexView(generic.ListView):
    template_name = "core/index.html"
    queryset = Product.objects.all()

    def get_ordering(self):
        if self.request.GET.get("sort") == "true":
            return "-clicks"
        else:
            return self.ordering



class ProductDetailView(generic.DetailView):
    template_name = "core/details.html"
    context_object_name = "product"
    model = Product

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)
        obj = Product.objects.get(pk=self.kwargs['pk'])
        obj.clicks = F('clicks') + 1
        obj.save()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)


class TvListView(generic.ListView):
    template_name = "core/index.html"
    queryset = Product.objects.filter(type__name="Tv")

    def get_ordering(self):
        if self.request.GET.get("sort") == "true":
            return "-clicks"
        else:
            return self.ordering


class FridgeListView(generic.ListView):
    template_name = "core/index.html"
    queryset = Product.objects.filter(type__name="Fridge")

    def get_ordering(self):
        if self.request.GET.get("sort") == "true":
            return "-clicks"
        else:
            return self.ordering

@ensure_csrf_cookie
def increase(request, pk):
    try:
        prod = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"error": "object does not exists"})

    prod.clicks = F("clicks") + 1
    prod.save()
    return JsonResponse({"clicks": str(Product.objects.get(pk=pk).clicks)})