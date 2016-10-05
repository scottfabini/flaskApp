from flask import Blueprint

main = Blueprint('main', __name__)

# this import is at the end due to an otherwise circular dependency
from . import views, errors
