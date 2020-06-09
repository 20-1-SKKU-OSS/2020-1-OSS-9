import shutil
import textwrap

# Base class for exceptions
# 예외처리 Base 클래스
class MusicbotException(Exception):
    def __init__(self, message, *, expire_in=0):
        super().__init__(message) # ???
        self._message = message
        self.expire_in = expire_in

    @property
    def message(self):
        return self._message

    @property
    def message_no_format(self):
        return self._message

# Something went wrong during the processing of a command
# 유저 커맨드가 잘못된 경우
class CommandError(MusicbotException):
    pass

# Something went wrong during the processing of a song/ytdl stuff
# song/ytdl 추출하는 부분에서 잘못된 경우
class ExtractionError(MusicbotException):
    pass

# The no processing entry type failed and an entry was a playlist/vice versa
# TODO: Add typing options instead of is_playlist
class WrongEntryTypeError(ExtractionError):
    def __init__(self, message, is_playlist, use_url):
        super().__init__(message)
        self.is_playlist = is_playlist
        self.use_url = use_url

# FFmpeg complained about something
# FFmpeg 관련 오류(Error 수준)
class FFmpegError(MusicbotException):
    pass

# FFmpeg complained about something but we don't care
# FFmpeg 관련 오류(Warning 수준)
class FFmpegWarning(MusicbotException):
    pass

# Some issue retrieving something from Spotify's API
# Spotify API 데이터 추출 오류
class SpotifyError(MusicbotException):
    pass

# The user doesn't have permission to use a command
# 해당 명령어에 대한 유저 권한 오류
class PermissionsError(CommandError):
    @property
    def message(self):
        return "You don't have permission to use that command.\nReason: " + self._message + "\n명령어에 대한 권한이 없습니다.\n 상세: " + self.message

# Error with pretty formatting for hand-holding users through various errors
class HelpfulError(MusicbotException):
    def __init__(self, issue, solution, *, preface="An error has occured:", footnote='', expire_in=0):
        self.issue = issue
        self.solution = solution
        self.preface = preface
        self.footnote = footnote
        self.expire_in = expire_in
        self._message_fmt = "\n{preface}\n{problem}\n\n{solution}\n\n{footnote}"

    @property
    def message(self):
        return self._message_fmt.format(
            preface  = self.preface,
            problem  = self._pretty_wrap(self.issue,    "  Problem:"),
            solution = self._pretty_wrap(self.solution, "  Solution:"),
            footnote = self.footnote
        )

    @property
    def message_no_format(self):
        return self._message_fmt.format(
            preface  = self.preface,
            problem  = self._pretty_wrap(self.issue,    "  Problem:", width=None),
            solution = self._pretty_wrap(self.solution, "  Solution:", width=None),
            footnote = self.footnote
        )

    @staticmethod
    def _pretty_wrap(text, pretext, *, width=-1):
        if width is None:
            return '\n'.join((pretext.strip(), text))
        elif width == -1:
            pretext = pretext.rstrip() + '\n'
            width = shutil.get_terminal_size().columns

        lines = textwrap.wrap(text, width=width - 5)
        lines = (('    ' + line).rstrip().ljust(width-1).rstrip() + '\n' for line in lines)

        return pretext + ''.join(lines).rstrip()

class HelpfulWarning(HelpfulError):
    pass

# Base class for control signals
# 시그널 처리 Base 클래스
class Signal(Exception):
    pass

# signal to restart the bot
# 봇 초기화 시그널
class RestartSignal(Signal):
    pass

# signal to end the bot "gracefully"
# 봇 종료 시그널 (강제종료 제외)
class TerminateSignal(Signal):
    pass
