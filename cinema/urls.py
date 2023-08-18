from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("Genres", GenreViewSet)
router.register("Movie", MovieViewSet)
router.register("CinemaHall", CinemaHallViewSet)

app_name = "cinema"
