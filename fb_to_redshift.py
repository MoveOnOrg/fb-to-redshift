#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Runs all the things. Most of the functions that do the work live elsewhere. 
"""

from fb_tools import create_import_file, upload_to_s3, update_redshift
from time import gmtime, strftime
from settings import test, files_dir, s3_bucket, s3_bucket_dir

def main():
    posts = {}
    posts['interval'] = 'month'
    posts['import_type'] = 'posts'
    posts['filename'] = 'fb_import_posts.csv'
    posts['tablename'] = 'facebook.posts'
    posts['columns'] = [
        'post_id', 'message', 'created_time', 'likes',
        'shares','comments', 'total_reach'
        ]
    posts['primary_key'] = 'post_id'

    videos = {}
    videos['interval'] = False
    videos['import_type'] = 'videos'
    videos['filename'] = 'fb_import_videos.csv'
    videos['tablename'] = 'facebook.videos'
    videos['columns'] = ['video_id', 'title', 'description',
        'created_time', 'video_length', 'likes', 'comments', 'reactions',
        'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers',
        'views_10sec', 'views_30sec', 'views_95pct', 'avg_sec_watched',
        'avg_completion', 'views_autoplayed', 'views_clicked_to_play',
        'views_organic', 'views_organic_unique', 'views_paid',
        'views_paid_unique', 'views_sound_on', 'complete_views',
        'complete_views_unique', 'complete_views_auto_played',
        'complete_views_clicked_to_play', 'complete_views_organic',
        'complete_views_organic_unique', 'complete_views_paid',
        'complete_views_paid_unique', 'views_10s_auto_played',
        'views_10s_clicked_to_play', 'views_10s_organic', 'views_10s_paid',
        'views_10s_sound_on', 'avg_time_watched', 'view_total_time_organic',
        'view_total_time_paid', 'impressions', 'impressions_paid_unique',
        'impressions_paid', 'impressions_organic_unique', 'impressions_organic',
        'impressions_viral_unique', 'impressions_viral', 'impressions_fan_unique',
        'impressions_fan', 'impressions_fan_paid_unique', 'impressions_fan_paid'
        ]
    videos['primary_key'] = 'video_id'

    video_lab_videos = {}
    video_lab_videos['interval'] = False
    video_lab_videos['import_type'] = 'video_lab_videos'
    video_lab_videos['filename'] = 'fb_import_video_lab.csv'
    video_lab_videos['tablename'] = 'facebook.video_lab_videos'
    video_lab_videos['columns'] = ['video_id', 'title', 'description',
        'created_time', 'video_length', 'likes', 'comments', 'reactions',
        'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers',
        'views_10sec', 'views_30sec', 'views_95pct', 'avg_sec_watched',
        'avg_completion', 'views_autoplayed', 'views_clicked_to_play',
        'views_organic', 'views_organic_unique', 'views_paid',
        'views_paid_unique', 'views_sound_on', 'complete_views',
        'complete_views_unique', 'complete_views_auto_played',
        'complete_views_clicked_to_play', 'complete_views_organic',
        'complete_views_organic_unique', 'complete_views_paid',
        'complete_views_paid_unique', 'views_10s_auto_played',
        'views_10s_clicked_to_play', 'views_10s_organic', 'views_10s_paid',
        'views_10s_sound_on', 'avg_time_watched', 'view_total_time_organic',
        'view_total_time_paid', 'impressions', 'impressions_paid_unique',
        'impressions_paid', 'impressions_organic_unique', 'impressions_organic',
        'impressions_viral_unique', 'impressions_viral', 'impressions_fan_unique',
        'impressions_fan', 'impressions_fan_paid_unique', 'impressions_fan_paid'
        ]
    video_lab_videos['primary_key'] = 'video_id'
    video_lab_videos['list_id'] = '1563848167245359'

    video_lab_videos_2 = {}
    video_lab_videos_2['interval'] = False
    video_lab_videos_2['import_type'] = 'video_lab_videos'
    video_lab_videos_2['filename'] = 'fb_import_video_lab_2.csv'
    video_lab_videos_2['tablename'] = 'facebook.video_lab_videos'
    video_lab_videos_2['columns'] = ['video_id', 'title', 'description',
        'created_time', 'video_length', 'likes', 'comments', 'reactions',
        'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers',
        'views_10sec', 'views_30sec', 'views_95pct', 'avg_sec_watched',
        'avg_completion', 'views_autoplayed', 'views_clicked_to_play',
        'views_organic', 'views_organic_unique', 'views_paid',
        'views_paid_unique', 'views_sound_on', 'complete_views',
        'complete_views_unique', 'complete_views_auto_played',
        'complete_views_clicked_to_play', 'complete_views_organic',
        'complete_views_organic_unique', 'complete_views_paid',
        'complete_views_paid_unique', 'views_10s_auto_played',
        'views_10s_clicked_to_play', 'views_10s_organic', 'views_10s_paid',
        'views_10s_sound_on', 'avg_time_watched', 'view_total_time_organic',
        'view_total_time_paid', 'impressions', 'impressions_paid_unique',
        'impressions_paid', 'impressions_organic_unique', 'impressions_organic',
        'impressions_viral_unique', 'impressions_viral', 'impressions_fan_unique',
        'impressions_fan', 'impressions_fan_paid_unique', 'impressions_fan_paid'
        ]
    video_lab_videos_2['primary_key'] = 'video_id'
    video_lab_videos_2['list_id'] = '1225720367451359'

    data_types = [posts, videos, video_lab_videos, video_lab_videos_2]

    print()
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    for item in data_types:
        if test:
            item['tablename'] += '_test'
        if 'list_id' in item:
            create_import_file(item.get('interval'), item.get('import_type'),
                item.get('filename'), item.get('list_id')
                )
        else:
            create_import_file(item.get('interval'), item.get('import_type'),
                item.get('filename')
                )
        print("created %s " %(files_dir + item.get('filename')) 
        
        upload_to_s3(item.get('filename'))
        print("uploaded %s to s3 bucket s3://%s" %(files_dir + item.get('filename'), s3_bucket + '/' + s3_bucket_dir)
        
        update_redshift(item.get('tablename'), item.get('columns'), 
            item.get('primary_key'), item.get('filename'))
        print("updated redshift table " + item.get('tablename'))

if __name__=='__main__':
   main()
