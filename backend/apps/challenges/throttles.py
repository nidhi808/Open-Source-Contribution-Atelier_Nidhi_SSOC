from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.exceptions import Throttled, APIException


class SandboxThrottled(Throttled):
    """Custom Throttled exception that allows dictionary details and sets wait time."""
    def __init__(self, wait=None, detail=None, code=None):
        self.wait = wait
        APIException.__init__(self, detail, code)


class SandboxAnonRateThrottle(AnonRateThrottle):
    """Rate limit anonymous users: 10 requests/minute by IP."""
    scope = "sandbox_anon"

    def throttle_failure(self):
        raise SandboxThrottled(
            wait=self.wait(),
            detail={
                "error": "Rate limit exceeded.",
                "message": "You can only execute 10 sandbox requests per minute. Please wait before retrying.",
                "type": "rate_limit_exceeded",
            }
        )


class SandboxUserRateThrottle(UserRateThrottle):
    """Rate limit authenticated users: 10 requests/minute by user ID."""
    scope = "sandbox_user"

    def throttle_failure(self):
        raise SandboxThrottled(
            wait=self.wait(),
            detail={
                "error": "Rate limit exceeded.",
                "message": "You can only execute 10 sandbox requests per minute. Please wait before retrying.",
                "type": "rate_limit_exceeded",
            }
        )
