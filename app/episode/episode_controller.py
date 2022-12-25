from flask import Blueprint
from app.episode.episode_client import EpisodeClient
from app.episode.episode_service import EpisodeService

episodes_page = Blueprint('episodes_page', __name__)

@episodes_page.route('/episodes')
def get_episodes():
    return EpisodeService.data_episode(EpisodeClient.base_url(), EpisodeClient.end_point_episode())
