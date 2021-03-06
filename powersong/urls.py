from django.conf.urls import url
from django.contrib import admin

from powersong.view_oauth import strava_oauth, lastfm_oauth, spotify_oauth, spotify_refresh_token_endpoint
from powersong.view_home import index, home, logout, demo
from powersong.view_tops import top, top_song_artist, top_activities, top_global_song_artist
from powersong.view_detail import activity, song, artist, artists, songs
from powersong.view_main import about, get_sync_progress, sync, sync_spotify, resync_last_fm, resync_spotify, detailed, global_top, send_song_info_to_strava
from powersong.view_settings import setting, flag_activity, flag_artist, flag_song, flag_effort, remove_spotify, remove_lastfm, delete_account
from powersong.view_webhooks import strava_webhooks_callback
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
	url(r'^$', index, name='index'),

    url(r'^demo/', demo),
    
    url(r'^home/', home),
    url(r'^sync/', sync),
    url(r'^sync_spotify/', sync_spotify),
    url(r'^about/', about),
    url(r'^settings/', setting),
    url(r'^logout/', logout),
    url(r'^top/', top),
    url(r'^top_song_artist/', top_song_artist),
    url(r'^top_global/', top_global_song_artist),
    url(r'^top_activities/', top_activities),
    
    url(r'^detailed/', detailed),
    url(r'^global/', global_top),
    url(r'^artists/', artists),
    url(r'^songs/', songs),
    
    url(r'^activity/(?P<activity_id>.*)/', activity),
    url(r'^flag_activity/(?P<activity_id>.*)/', flag_activity),   
    url(r'^flag_effort/(?P<effort_id>.*)/', flag_effort),
    

    url(r'^song/(?P<song_id>.*)/', song),
    url(r'^flag_song/(?P<song_id>.*)/', flag_song),

    url(r'^artist/(?P<artist_id>.*)/', artist),
    url(r'^flag_artist/(?P<artist_id>.*)/', flag_artist),

    url(r'^get_sync_progress/', get_sync_progress),

    url(r'^resync_last_fm/(?P<activity_id>.*)/', resync_last_fm),
    url(r'^resync_spotify/(?P<activity_id>.*)/', resync_spotify),
    url(r'^send_song_info_to_strava/(?P<activity_id>.*)/', send_song_info_to_strava),

    url(r'^strava_webhooks/', strava_webhooks_callback),

    url(r'^strava_oauth_callback/', strava_oauth),
    url(r'^strava_oauth_refresh/', spotify_refresh_token_endpoint),

    url(r'^lastfm_oauth_callback/', lastfm_oauth),
    url(r'^spotify_oauth_callback/', spotify_oauth),

    url(r'^remove_lastfm/', remove_lastfm),
    url(r'^remove_spotify/', remove_spotify), 
    url(r'^delete_account/', delete_account), 
    
    url(r'^admin/', admin.site.urls),

    url(r'^async_include/', include('async_include.urls', namespace="async_include")),
]

#urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
