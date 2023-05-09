from rest_framework.exceptions import ValidationError


class ConflictError(ValidationError):
    status_code = 409
    default_detail = "Conflict Error"


class ErrorForbidden(ValidationError):
    status_code = 403
    default_detail = "Request Declined"
