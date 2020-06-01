# OSS 9조

# static page 주소

https://20-1-skku-oss.github.io/2020-1-OSS-9/

# 팀원

번역:	이민규, 윤재식

git 저장소 관리:	임유진, 이황근

소스 코드 분석:	윤형호, 윤재식

소스 코드 추가:	윤형호, 이민규, 임유진, 이황근

# MusicBot

[![GitHub stars](https://img.shields.io/github/stars/Just-Some-Bots/MusicBot.svg)](https://github.com/Just-Some-Bots/MusicBot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Just-Some-Bots/MusicBot.svg)](https://github.com/Just-Some-Bots/MusicBot/network)
[![Python version](https://img.shields.io/badge/python-3.5%2C%203.6%2C%203.7-blue.svg)](https://python.org)
[![Discord](https://discordapp.com/api/guilds/129489631539494912/widget.png?style=shield)](https://discord.gg/bots)

MusicBot is the original Discord music bot written for [Python](https://www.python.org "Python homepage") 3.5+, using the [discord.py](https://github.com/Rapptz/discord.py) library. It plays requested songs from YouTube and other services into a Discord server (or multiple servers). Besides, if the queue becomes empty MusicBot will play through a list of existing songs with configuration. The bot features a permission system allowing owners to restrict commands to certain people. As well as playing songs, MusicBot is capable of streaming live media into a voice channel (experimental).

MusicBot은 현재 Discord에서 가장 널리 쓰이고 있는 음악재생 봇으로 discord.py 라이브러리를 통해 [Python](https://www.python.org "Python homepage") 3.5 이상의 버전에서의 사용을 지원합니다. MusicBot은 사용자로부터 입력을 받아 YouTube와 같은 미디어 서비스 플랫폼에서 재생되는 미디어 파일 및 음악들을 Discord 서버를 통해 재생합니다. 설정을 통해 재생목록이 비어있는 경우에도 특정 음악을 재생하게 할 수 있으며, 접근권한 설정을 통해 다른 사용자의 명령어을 제한하는 기능 또한 제공하고 있습니다.
(실험중인 기능) MusicBot은 음악 재생과 더불어, 라이브 미디어 재생 기능 또한 제공하고 있습니다. 

![Main](https://i.imgur.com/FWcHtcS.png)

## Setup
Setting up the MusicBot is relatively painless - just follow one of the [guides](https://just-some-bots.github.io/MusicBot/). After that, configure the bot to ensure its connection to Discord.

The main configuration file is `config/options.ini`, but it is not included by default. Simply make a copy of `example_options.ini` and rename it to `options.ini`. See `example_options.ini` for more information about configurations.

MusicBot 설치는 아주 간단한 [가이드](https://just-some-bots.github.io/MusicBot/)만 따르면 가능합니다. 이후, Discord 서버와의 연결을 통해 몇 가지 초기 설정이 필요합니다.

초기 설정을 위해 수정해야 할 파일은 `config/options.ini` 이며, 기본 다운로드 파일에 포함되어 있지 않으므로 `example_options.ini`파일을 복사하여 진행하여 주시기 바랍니다. `example_options.ini`파일에 더욱 다양한 예시들이 제공되어 있으니 설치시 참고하시기 바랍니다.

### Commands

There are many commands that can be used with the bot. Most notably, the `play <url>` command (preceded by your command prefix) will download, process, and play a song from YouTube or a similar site. A full list of commands is available [here](https://just-some-bots.github.io/MusicBot/using/commands/ "Commands").

MusicBot은 매우 다양한 명령어들을 제공하고 있으며, 가장 자주 사용하게 될 명령어로는 `play <url>`이 있습니다. 해당 명령어를 통해 <url>에 해당하는 미디어 파일을 Discord 서버를 통해 다운로드 및 재생할 수 있습니다. 기타 명령어는 [여기](https://just-some-bots.github.io/MusicBot/using/commands/ "Commands")를 참고하시기 바랍니다.

### Further reading

* [Support Discord server](https://discord.gg/bots)
* [Project license](LICENSE)
