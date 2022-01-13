from yt_stats import YTstats

api_key = 'AIzaSyAARWd4u9zkHEIhst5pLp59BIqa51m3Izg'

channel_id = 'UCUvvj5lwue7PspotMDjk5UA'   # meet kevin
channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'   # python_engineer

yt = YTstats(api_key,channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
