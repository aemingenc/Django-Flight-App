from rest_framework import permissions


class IsStuffOrReadOnly(permissions.IsAdminUser):

#Bu method IsAdminUserinbir metodu user varmı varsada staff mı ona bakar biz bunu override ettik
    def has_permission(self, request, view):
#eger methodlar safe metodlardansa(get,head,options) izin ver 
#diğerlerindense(put,fatch,post) kullanıcı  staff sa izin ver
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)