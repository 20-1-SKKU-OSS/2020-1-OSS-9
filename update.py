#!/usr/bin/env python3

import os
import subprocess
import sys

def y_n(q):
    while True:
        ri = input('{} (y/n): '.format(q))
        if ri.lower() in ['yes', 'y']: return True
        elif ri.lower() in ['no', 'n']: return False

def update_deps():
    print("Attempting to update dependencies...")
    print("종속성을 업데이트하는 중...")

    try:
        subprocess.check_call('"{}" -m pip install --no-warn-script-location --user -U -r requirements.txt'.format(sys.executable), shell=True)
    except subprocess.CalledProcessError:
        raise OSError("Could not update dependencies. You will need to run '\"{0}\" -m pip install -U -r requirements.txt' yourself.".format(sys.executable))

def finalize():
    try:
        from musicbot.constants import VERSION
        print('The current MusicBot version is {0}.'.format(VERSION))
        print('현재 MusicBot 버전은 {0}.'.format(VERSION))
    except Exception:
        print('There was a problem fetching your current bot version. The installation may not have completed correctly.')
        print('현재 봇 버전을 가져오는 중 문제가 발생하였습니다. 설치가 올바르게 완료되지 않았을 수 있다.')

    print("Done!")
    print("완료!")

def main():
    print('Starting...')
    print('시작중....')

    # Make sure that we're in a Git repository
    # Git 저장소에 있는지 확인
    
    if not os.path.isdir('.git'):
        raise EnvironmentError("This isn't a Git repository.")

    # Make sure that we can actually use Git on the command line
    # because some people install Git Bash without allowing access to Windows CMD
    # 커맨드 라인에서 (Git)을 실제로 사용할 것
    # 일부 사용자가 Windows CMD에 액세스하지 않고 Git Bash를 설치하기 때문에
    try:
        subprocess.check_call('git --version', shell=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise EnvironmentError("Couldn't use Git on the CLI. You will need to run 'git pull' yourself.")

    print("Passed Git checks...")
    print("Git 확인...")

    # Check that the current working directory is clean
    # 현재 작업 디렉토리가 깨끗한지 확인
    sp = subprocess.check_output('git status --porcelain', shell=True, universal_newlines=True)
    if sp:
        oshit = y_n('You have modified files that are tracked by Git (e.g the bot\'s source files).\n'
                    'Should we try resetting the repo? You will lose local modifications.')
        if oshit:
            try:
                subprocess.check_call('git reset --hard', shell=True)
            except subprocess.CalledProcessError:
                raise OSError("Could not reset the directory to a clean state.")
        else:
            wowee = y_n('OK, skipping bot update. Do you still want to update dependencies?')
            if wowee:
                update_deps()
            else:
                finalize()
            return

    print("Checking if we need to update the bot...")

    
    try:
        subprocess.check_call('git pull', shell=True)
    except subprocess.CalledProcessError:
        raise OSError("Could not update the bot. You will need to run 'git pull' yourself.")

    update_deps()
    finalize()

if __name__ == '__main__':
    main()
