from django.urls import path
from  .views import TodoList, delete_all, delete_completed, delete_todo, mark_completed, mark_uncompleted

app_name = "todoapp"

urlpatterns = [
    path("", TodoList.as_view(), name='home'),
    path("delete_all/", delete_all, name="delete_all"),
    path("delete_completed/", delete_completed, name="delete_completed"),
    path("delete/<int:todo_id>/", delete_todo, name="delete"),
    path("mark_completed/<int:todo_id>/", mark_completed, name="completed"),
    path("mark_uncompleted/<int:todo_id>/", mark_uncompleted, name="uncompleted"),
    #path("<int:pk>/delete/", DeleteView.as_view(), name='delete_todo')
]