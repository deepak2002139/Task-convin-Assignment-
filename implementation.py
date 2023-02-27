from django.http import HttpResponseBadRequest
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow

def GoogleCalendarRedirectView(request):
    state = request.session['state']
    flow = Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        state=state,
        redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/')
    flow.fetch_token(authorization_response=request.get_full_path())
    credentials = flow.credentials
    if not credentials:
        return HttpResponseBadRequest('Failed to retrieve access token.')
    # Use the credentials to get the list of events in the user's calendar
    # ...
    return HttpResponse('Events retrieved successfully.')
