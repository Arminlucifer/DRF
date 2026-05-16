from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]


class UserQuerySetMixin():

    user_field = 'owner'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)

        if not user.is_authenticated:
            return qs.none()
        lookupdata = {self.user_field: user}  # 1
        # lookupdata = {"owner": user} # 2

        return qs.filter(**lookupdata)  # 1
        # return qs.filter(**lookupdata) #2
        # return qs.filter(**{self.user_field: user}) # 3
