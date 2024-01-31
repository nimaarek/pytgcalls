from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioQuality
from pytgcalls.types import Browsers
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality
from pytgcalls.types.raw import AudioParameters
from pytgcalls.types.raw import VideoParameters

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
remote = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'
call_py.join_group_call(
    -1001234567890,
    MediaStream(
        remote,
        AudioParameters.from_quality(AudioQuality.HIGH),
        VideoParameters.from_quality(VideoQuality.HD_720p),
        headers={
            'User-Agent': Browsers().chrome_windows,
        },
    ),
)
idle()
