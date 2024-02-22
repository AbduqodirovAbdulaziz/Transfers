from django.contrib import admin
from django.urls import path
from statsAPP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='home'),
                  path('about/', about, name='about'),
                  path('tryouts/', tryouts, name='tryouts'),
                  path('stats/', stats, name='stats'),
                  # path('countries/', countries, name='countries'),

                  path('clubs/', clubs, name='clubs'),
                  path('latest_transfers/', latest_transfers, name='latest_transfers'),
                  path('players/', players, name='players'),
                  path('<str:country_name>/clubs/', country_clubs),
                  path('katta_players/', katta_players, name='u-20 players'),

                  path('seasons/', seasons, name='seasons'),

                  path('<str:club_name>/player/', clubs_player, name='clubs_player'),

                  path('birinchi/', birinchi, name='birinchi'),
                  path('ikkinchi/', ikkinchi, name='ikkinchi'),
                  path('uchinchi/', uchinchi, name='uchinchi'),
                  path('tortinchi/', tortinchi, name='tortinchi'),

                  path('accurate_predictions/', accurate_predictions),
                  path('top_50_clubs/', top_50_clubs),
                  path('transfers_record/', transfers_record),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
