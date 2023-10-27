from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *  # import wildly
from api.v1.views.states import *  # import wildly
from api.v1.views.cities import *  # import wildly
from api.v1.views.amenities import *  # import wildly
from api.v1.views.users import *  # import wildly
from api.v1.views.places import *  # import wildly
from api.v1.views.places_reviews import *  
from api.v1.views.places_amenities import *
