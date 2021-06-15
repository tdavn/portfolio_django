from django.urls import path
from .views import BlgHomeView, BlgDetailView, AddBlgPostView, EditBlgPostView
from .views import DeleteBlgPostView, BlgCategoryView  # LikeView,  # AddCategoryView

urlpatterns = [
path('', BlgHomeView.as_view(), name='blg_index'),
path('blg/<int:pk>', BlgDetailView.as_view(), name='blg_detail'),
path('add_post/', AddBlgPostView.as_view(), name='blg_add'),
# path('add_category/', AddCategoryView.as_view(), name='add_category'),
path('blg_post/edit/<int:pk>', EditBlgPostView.as_view(), name='blg_edit'),
path('blg_post/<int:pk>/remove', DeleteBlgPostView.as_view(), name='blg_delete'),
path('blg_category/<str:cats>/', BlgCategoryView, name='blg_category'),
]
