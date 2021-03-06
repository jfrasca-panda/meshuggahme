#!/usr/bin/env python

import os

os.environ['MESHUGGAME_AVCONV_PATH'] = '/usr/bin/avconv'
os.environ['MESHUGGAME_YTDL_PATH'] = '/home/phaedrus/repos/meshuggahme/muxer/youtube-dl'
os.environ['MUSHUGGAME_DL_PATH'] = '/home/phaedrus/tmp/meshuggame/dl'
os.environ['MUSHUGGAME_OUTPUT_PATH'] = '/home/phaedrus/tmp/meshuggame/out'

from muxer import Muxer

gojira = 'https://www.youtube.com/watch?v=BGHlZwMYO9g'
spears = 'https://www.youtube.com/watch?v=LOZuxwVk7TU'

if __name__ == '__main__':
    gojira_muxer = Muxer(yt_url=gojira)
    spears_muxer = Muxer(yt_url=spears)

    gojira_muxer.download_video()
    spears_muxer.download_video()

    gojira_muxer.demux()
    spears_muxer.demux()

    spears_muxer.remux(gojira_muxer.get_audio_file())


